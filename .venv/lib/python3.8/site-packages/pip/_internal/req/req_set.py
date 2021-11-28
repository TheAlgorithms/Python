import logging
from collections import OrderedDict
from typing import Dict, Iterable, List, Optional, Tuple

from pip._vendor.packaging.utils import canonicalize_name

from pip._internal.exceptions import InstallationError
from pip._internal.models.wheel import Wheel
from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils import compatibility_tags

logger = logging.getLogger(__name__)


class RequirementSet:

    def __init__(self, check_supported_wheels=True):
        # type: (bool) -> None
        """Create a RequirementSet.
        """

        self.requirements = OrderedDict()  # type: Dict[str, InstallRequirement]
        self.check_supported_wheels = check_supported_wheels

        self.unnamed_requirements = []  # type: List[InstallRequirement]

    def __str__(self):
        # type: () -> str
        requirements = sorted(
            (req for req in self.requirements.values() if not req.comes_from),
            key=lambda req: canonicalize_name(req.name or ""),
        )
        return ' '.join(str(req.req) for req in requirements)

    def __repr__(self):
        # type: () -> str
        requirements = sorted(
            self.requirements.values(),
            key=lambda req: canonicalize_name(req.name or ""),
        )

        format_string = '<{classname} object; {count} requirement(s): {reqs}>'
        return format_string.format(
            classname=self.__class__.__name__,
            count=len(requirements),
            reqs=', '.join(str(req.req) for req in requirements),
        )

    def add_unnamed_requirement(self, install_req):
        # type: (InstallRequirement) -> None
        assert not install_req.name
        self.unnamed_requirements.append(install_req)

    def add_named_requirement(self, install_req):
        # type: (InstallRequirement) -> None
        assert install_req.name

        project_name = canonicalize_name(install_req.name)
        self.requirements[project_name] = install_req

    def add_requirement(
        self,
        install_req,  # type: InstallRequirement
        parent_req_name=None,  # type: Optional[str]
        extras_requested=None  # type: Optional[Iterable[str]]
    ):
        # type: (...) -> Tuple[List[InstallRequirement], Optional[InstallRequirement]]
        """Add install_req as a requirement to install.

        :param parent_req_name: The name of the requirement that needed this
            added. The name is used because when multiple unnamed requirements
            resolve to the same name, we could otherwise end up with dependency
            links that point outside the Requirements set. parent_req must
            already be added. Note that None implies that this is a user
            supplied requirement, vs an inferred one.
        :param extras_requested: an iterable of extras used to evaluate the
            environment markers.
        :return: Additional requirements to scan. That is either [] if
            the requirement is not applicable, or [install_req] if the
            requirement is applicable and has just been added.
        """
        # If the markers do not match, ignore this requirement.
        if not install_req.match_markers(extras_requested):
            logger.info(
                "Ignoring %s: markers '%s' don't match your environment",
                install_req.name, install_req.markers,
            )
            return [], None

        # If the wheel is not supported, raise an error.
        # Should check this after filtering out based on environment markers to
        # allow specifying different wheels based on the environment/OS, in a
        # single requirements file.
        if install_req.link and install_req.link.is_wheel:
            wheel = Wheel(install_req.link.filename)
            tags = compatibility_tags.get_supported()
            if (self.check_supported_wheels and not wheel.supported(tags)):
                raise InstallationError(
                    "{} is not a supported wheel on this platform.".format(
                        wheel.filename)
                )

        # This next bit is really a sanity check.
        assert not install_req.user_supplied or parent_req_name is None, (
            "a user supplied req shouldn't have a parent"
        )

        # Unnamed requirements are scanned again and the requirement won't be
        # added as a dependency until after scanning.
        if not install_req.name:
            self.add_unnamed_requirement(install_req)
            return [install_req], None

        try:
            existing_req = self.get_requirement(
                install_req.name)  # type: Optional[InstallRequirement]
        except KeyError:
            existing_req = None

        has_conflicting_requirement = (
            parent_req_name is None and
            existing_req and
            not existing_req.constraint and
            existing_req.extras == install_req.extras and
            existing_req.req and
            install_req.req and
            existing_req.req.specifier != install_req.req.specifier
        )
        if has_conflicting_requirement:
            raise InstallationError(
                "Double requirement given: {} (already in {}, name={!r})"
                .format(install_req, existing_req, install_req.name)
            )

        # When no existing requirement exists, add the requirement as a
        # dependency and it will be scanned again after.
        if not existing_req:
            self.add_named_requirement(install_req)
            # We'd want to rescan this requirement later
            return [install_req], install_req

        # Assume there's no need to scan, and that we've already
        # encountered this for scanning.
        if install_req.constraint or not existing_req.constraint:
            return [], existing_req

        does_not_satisfy_constraint = (
            install_req.link and
            not (
                existing_req.link and
                install_req.link.path == existing_req.link.path
            )
        )
        if does_not_satisfy_constraint:
            raise InstallationError(
                "Could not satisfy constraints for '{}': "
                "installation from path or url cannot be "
                "constrained to a version".format(install_req.name)
            )
        # If we're now installing a constraint, mark the existing
        # object for real installation.
        existing_req.constraint = False
        # If we're now installing a user supplied requirement,
        # mark the existing object as such.
        if install_req.user_supplied:
            existing_req.user_supplied = True
        existing_req.extras = tuple(sorted(
            set(existing_req.extras) | set(install_req.extras)
        ))
        logger.debug(
            "Setting %s extras to: %s",
            existing_req, existing_req.extras,
        )
        # Return the existing requirement for addition to the parent and
        # scanning again.
        return [existing_req], existing_req

    def has_requirement(self, name):
        # type: (str) -> bool
        project_name = canonicalize_name(name)

        return (
            project_name in self.requirements and
            not self.requirements[project_name].constraint
        )

    def get_requirement(self, name):
        # type: (str) -> InstallRequirement
        project_name = canonicalize_name(name)

        if project_name in self.requirements:
            return self.requirements[project_name]

        raise KeyError(f"No project with the name {name!r}")

    @property
    def all_requirements(self):
        # type: () -> List[InstallRequirement]
        return self.unnamed_requirements + list(self.requirements.values())
