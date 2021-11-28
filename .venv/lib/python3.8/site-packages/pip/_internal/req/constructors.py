"""Backing implementation for InstallRequirement's various constructors

The idea here is that these formed a major chunk of InstallRequirement's size
so, moving them and support code dedicated to them outside of that class
helps creates for better understandability for the rest of the code.

These are meant to be used elsewhere within pip to create instances of
InstallRequirement.
"""

import logging
import os
import re
from typing import Any, Dict, Optional, Set, Tuple, Union

from pip._vendor.packaging.markers import Marker
from pip._vendor.packaging.requirements import InvalidRequirement, Requirement
from pip._vendor.packaging.specifiers import Specifier
from pip._vendor.pkg_resources import RequirementParseError, parse_requirements

from pip._internal.exceptions import InstallationError
from pip._internal.models.index import PyPI, TestPyPI
from pip._internal.models.link import Link
from pip._internal.models.wheel import Wheel
from pip._internal.pyproject import make_pyproject_path
from pip._internal.req.req_file import ParsedRequirement
from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils.filetypes import is_archive_file
from pip._internal.utils.misc import is_installable_dir
from pip._internal.utils.urls import path_to_url
from pip._internal.vcs import is_url, vcs

__all__ = [
    "install_req_from_editable", "install_req_from_line",
    "parse_editable"
]

logger = logging.getLogger(__name__)
operators = Specifier._operators.keys()


def _strip_extras(path):
    # type: (str) -> Tuple[str, Optional[str]]
    m = re.match(r'^(.+)(\[[^\]]+\])$', path)
    extras = None
    if m:
        path_no_extras = m.group(1)
        extras = m.group(2)
    else:
        path_no_extras = path

    return path_no_extras, extras


def convert_extras(extras):
    # type: (Optional[str]) -> Set[str]
    if not extras:
        return set()
    return Requirement("placeholder" + extras.lower()).extras


def parse_editable(editable_req):
    # type: (str) -> Tuple[Optional[str], str, Set[str]]
    """Parses an editable requirement into:
        - a requirement name
        - an URL
        - extras
        - editable options
    Accepted requirements:
        svn+http://blahblah@rev#egg=Foobar[baz]&subdirectory=version_subdir
        .[some_extra]
    """

    url = editable_req

    # If a file path is specified with extras, strip off the extras.
    url_no_extras, extras = _strip_extras(url)

    if os.path.isdir(url_no_extras):
        setup_py = os.path.join(url_no_extras, 'setup.py')
        setup_cfg = os.path.join(url_no_extras, 'setup.cfg')
        if not os.path.exists(setup_py) and not os.path.exists(setup_cfg):
            msg = (
                'File "setup.py" or "setup.cfg" not found. Directory cannot be '
                'installed in editable mode: {}'
                .format(os.path.abspath(url_no_extras))
            )
            pyproject_path = make_pyproject_path(url_no_extras)
            if os.path.isfile(pyproject_path):
                msg += (
                    '\n(A "pyproject.toml" file was found, but editable '
                    'mode currently requires a setuptools-based build.)'
                )
            raise InstallationError(msg)

        # Treating it as code that has already been checked out
        url_no_extras = path_to_url(url_no_extras)

    if url_no_extras.lower().startswith('file:'):
        package_name = Link(url_no_extras).egg_fragment
        if extras:
            return (
                package_name,
                url_no_extras,
                Requirement("placeholder" + extras.lower()).extras,
            )
        else:
            return package_name, url_no_extras, set()

    for version_control in vcs:
        if url.lower().startswith(f'{version_control}:'):
            url = f'{version_control}+{url}'
            break

    link = Link(url)

    if not link.is_vcs:
        backends = ", ".join(vcs.all_schemes)
        raise InstallationError(
            f'{editable_req} is not a valid editable requirement. '
            f'It should either be a path to a local project or a VCS URL '
            f'(beginning with {backends}).'
        )

    package_name = link.egg_fragment
    if not package_name:
        raise InstallationError(
            "Could not detect requirement name for '{}', please specify one "
            "with #egg=your_package_name".format(editable_req)
        )
    return package_name, url, set()


def deduce_helpful_msg(req):
    # type: (str) -> str
    """Returns helpful msg in case requirements file does not exist,
    or cannot be parsed.

    :params req: Requirements file path
    """
    msg = ""
    if os.path.exists(req):
        msg = " The path does exist. "
        # Try to parse and check if it is a requirements file.
        try:
            with open(req) as fp:
                # parse first line only
                next(parse_requirements(fp.read()))
                msg += (
                    "The argument you provided "
                    "({}) appears to be a"
                    " requirements file. If that is the"
                    " case, use the '-r' flag to install"
                    " the packages specified within it."
                ).format(req)
        except RequirementParseError:
            logger.debug(
                "Cannot parse '%s' as requirements file", req, exc_info=True
            )
    else:
        msg += f" File '{req}' does not exist."
    return msg


class RequirementParts:
    def __init__(
            self,
            requirement,  # type: Optional[Requirement]
            link,         # type: Optional[Link]
            markers,      # type: Optional[Marker]
            extras,       # type: Set[str]
    ):
        self.requirement = requirement
        self.link = link
        self.markers = markers
        self.extras = extras


def parse_req_from_editable(editable_req):
    # type: (str) -> RequirementParts
    name, url, extras_override = parse_editable(editable_req)

    if name is not None:
        try:
            req = Requirement(name)  # type: Optional[Requirement]
        except InvalidRequirement:
            raise InstallationError(f"Invalid requirement: '{name}'")
    else:
        req = None

    link = Link(url)

    return RequirementParts(req, link, None, extras_override)


# ---- The actual constructors follow ----


def install_req_from_editable(
    editable_req,  # type: str
    comes_from=None,  # type: Optional[Union[InstallRequirement, str]]
    use_pep517=None,  # type: Optional[bool]
    isolated=False,  # type: bool
    options=None,  # type: Optional[Dict[str, Any]]
    constraint=False,  # type: bool
    user_supplied=False,  # type: bool
):
    # type: (...) -> InstallRequirement

    parts = parse_req_from_editable(editable_req)

    return InstallRequirement(
        parts.requirement,
        comes_from=comes_from,
        user_supplied=user_supplied,
        editable=True,
        link=parts.link,
        constraint=constraint,
        use_pep517=use_pep517,
        isolated=isolated,
        install_options=options.get("install_options", []) if options else [],
        global_options=options.get("global_options", []) if options else [],
        hash_options=options.get("hashes", {}) if options else {},
        extras=parts.extras,
    )


def _looks_like_path(name):
    # type: (str) -> bool
    """Checks whether the string "looks like" a path on the filesystem.

    This does not check whether the target actually exists, only judge from the
    appearance.

    Returns true if any of the following conditions is true:
    * a path separator is found (either os.path.sep or os.path.altsep);
    * a dot is found (which represents the current directory).
    """
    if os.path.sep in name:
        return True
    if os.path.altsep is not None and os.path.altsep in name:
        return True
    if name.startswith("."):
        return True
    return False


def _get_url_from_path(path, name):
    # type: (str, str) -> Optional[str]
    """
    First, it checks whether a provided path is an installable directory
    (e.g. it has a setup.py). If it is, returns the path.

    If false, check if the path is an archive file (such as a .whl).
    The function checks if the path is a file. If false, if the path has
    an @, it will treat it as a PEP 440 URL requirement and return the path.
    """
    if _looks_like_path(name) and os.path.isdir(path):
        if is_installable_dir(path):
            return path_to_url(path)
        raise InstallationError(
            f"Directory {name!r} is not installable. Neither 'setup.py' "
            "nor 'pyproject.toml' found."
        )
    if not is_archive_file(path):
        return None
    if os.path.isfile(path):
        return path_to_url(path)
    urlreq_parts = name.split('@', 1)
    if len(urlreq_parts) >= 2 and not _looks_like_path(urlreq_parts[0]):
        # If the path contains '@' and the part before it does not look
        # like a path, try to treat it as a PEP 440 URL req instead.
        return None
    logger.warning(
        'Requirement %r looks like a filename, but the '
        'file does not exist',
        name
    )
    return path_to_url(path)


def parse_req_from_line(name, line_source):
    # type: (str, Optional[str]) -> RequirementParts
    if is_url(name):
        marker_sep = '; '
    else:
        marker_sep = ';'
    if marker_sep in name:
        name, markers_as_string = name.split(marker_sep, 1)
        markers_as_string = markers_as_string.strip()
        if not markers_as_string:
            markers = None
        else:
            markers = Marker(markers_as_string)
    else:
        markers = None
    name = name.strip()
    req_as_string = None
    path = os.path.normpath(os.path.abspath(name))
    link = None
    extras_as_string = None

    if is_url(name):
        link = Link(name)
    else:
        p, extras_as_string = _strip_extras(path)
        url = _get_url_from_path(p, name)
        if url is not None:
            link = Link(url)

    # it's a local file, dir, or url
    if link:
        # Handle relative file URLs
        if link.scheme == 'file' and re.search(r'\.\./', link.url):
            link = Link(
                path_to_url(os.path.normpath(os.path.abspath(link.path))))
        # wheel file
        if link.is_wheel:
            wheel = Wheel(link.filename)  # can raise InvalidWheelFilename
            req_as_string = f"{wheel.name}=={wheel.version}"
        else:
            # set the req to the egg fragment.  when it's not there, this
            # will become an 'unnamed' requirement
            req_as_string = link.egg_fragment

    # a requirement specifier
    else:
        req_as_string = name

    extras = convert_extras(extras_as_string)

    def with_source(text):
        # type: (str) -> str
        if not line_source:
            return text
        return f'{text} (from {line_source})'

    def _parse_req_string(req_as_string: str) -> Requirement:
        try:
            req = Requirement(req_as_string)
        except InvalidRequirement:
            if os.path.sep in req_as_string:
                add_msg = "It looks like a path."
                add_msg += deduce_helpful_msg(req_as_string)
            elif ('=' in req_as_string and
                  not any(op in req_as_string for op in operators)):
                add_msg = "= is not a valid operator. Did you mean == ?"
            else:
                add_msg = ''
            msg = with_source(
                f'Invalid requirement: {req_as_string!r}'
            )
            if add_msg:
                msg += f'\nHint: {add_msg}'
            raise InstallationError(msg)
        else:
            # Deprecate extras after specifiers: "name>=1.0[extras]"
            # This currently works by accident because _strip_extras() parses
            # any extras in the end of the string and those are saved in
            # RequirementParts
            for spec in req.specifier:
                spec_str = str(spec)
                if spec_str.endswith(']'):
                    msg = f"Extras after version '{spec_str}'."
                    raise InstallationError(msg)
        return req

    if req_as_string is not None:
        req = _parse_req_string(req_as_string)  # type: Optional[Requirement]
    else:
        req = None

    return RequirementParts(req, link, markers, extras)


def install_req_from_line(
    name,  # type: str
    comes_from=None,  # type: Optional[Union[str, InstallRequirement]]
    use_pep517=None,  # type: Optional[bool]
    isolated=False,  # type: bool
    options=None,  # type: Optional[Dict[str, Any]]
    constraint=False,  # type: bool
    line_source=None,  # type: Optional[str]
    user_supplied=False,  # type: bool
):
    # type: (...) -> InstallRequirement
    """Creates an InstallRequirement from a name, which might be a
    requirement, directory containing 'setup.py', filename, or URL.

    :param line_source: An optional string describing where the line is from,
        for logging purposes in case of an error.
    """
    parts = parse_req_from_line(name, line_source)

    return InstallRequirement(
        parts.requirement, comes_from, link=parts.link, markers=parts.markers,
        use_pep517=use_pep517, isolated=isolated,
        install_options=options.get("install_options", []) if options else [],
        global_options=options.get("global_options", []) if options else [],
        hash_options=options.get("hashes", {}) if options else {},
        constraint=constraint,
        extras=parts.extras,
        user_supplied=user_supplied,
    )


def install_req_from_req_string(
    req_string,  # type: str
    comes_from=None,  # type: Optional[InstallRequirement]
    isolated=False,  # type: bool
    use_pep517=None,  # type: Optional[bool]
    user_supplied=False,  # type: bool
):
    # type: (...) -> InstallRequirement
    try:
        req = Requirement(req_string)
    except InvalidRequirement:
        raise InstallationError(f"Invalid requirement: '{req_string}'")

    domains_not_allowed = [
        PyPI.file_storage_domain,
        TestPyPI.file_storage_domain,
    ]
    if (req.url and comes_from and comes_from.link and
            comes_from.link.netloc in domains_not_allowed):
        # Explicitly disallow pypi packages that depend on external urls
        raise InstallationError(
            "Packages installed from PyPI cannot depend on packages "
            "which are not also hosted on PyPI.\n"
            "{} depends on {} ".format(comes_from.name, req)
        )

    return InstallRequirement(
        req,
        comes_from,
        isolated=isolated,
        use_pep517=use_pep517,
        user_supplied=user_supplied,
    )


def install_req_from_parsed_requirement(
    parsed_req,  # type: ParsedRequirement
    isolated=False,  # type: bool
    use_pep517=None,  # type: Optional[bool]
    user_supplied=False,  # type: bool
):
    # type: (...) -> InstallRequirement
    if parsed_req.is_editable:
        req = install_req_from_editable(
            parsed_req.requirement,
            comes_from=parsed_req.comes_from,
            use_pep517=use_pep517,
            constraint=parsed_req.constraint,
            isolated=isolated,
            user_supplied=user_supplied,
        )

    else:
        req = install_req_from_line(
            parsed_req.requirement,
            comes_from=parsed_req.comes_from,
            use_pep517=use_pep517,
            isolated=isolated,
            options=parsed_req.options,
            constraint=parsed_req.constraint,
            line_source=parsed_req.line_source,
            user_supplied=user_supplied,
        )
    return req


def install_req_from_link_and_ireq(link, ireq):
    # type: (Link, InstallRequirement) -> InstallRequirement
    return InstallRequirement(
        req=ireq.req,
        comes_from=ireq.comes_from,
        editable=ireq.editable,
        link=link,
        markers=ireq.markers,
        use_pep517=ireq.use_pep517,
        isolated=ireq.isolated,
        install_options=ireq.install_options,
        global_options=ireq.global_options,
        hash_options=ireq.hash_options,
    )
