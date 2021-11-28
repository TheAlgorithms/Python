import contextlib
import hashlib
import logging
import os
from types import TracebackType
from typing import Dict, Iterator, Optional, Set, Type, Union

from pip._internal.models.link import Link
from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils.temp_dir import TempDirectory

logger = logging.getLogger(__name__)


@contextlib.contextmanager
def update_env_context_manager(**changes):
    # type: (str) -> Iterator[None]
    target = os.environ

    # Save values from the target and change them.
    non_existent_marker = object()
    saved_values = {}  # type: Dict[str, Union[object, str]]
    for name, new_value in changes.items():
        try:
            saved_values[name] = target[name]
        except KeyError:
            saved_values[name] = non_existent_marker
        target[name] = new_value

    try:
        yield
    finally:
        # Restore original values in the target.
        for name, original_value in saved_values.items():
            if original_value is non_existent_marker:
                del target[name]
            else:
                assert isinstance(original_value, str)  # for mypy
                target[name] = original_value


@contextlib.contextmanager
def get_requirement_tracker():
    # type: () -> Iterator[RequirementTracker]
    root = os.environ.get('PIP_REQ_TRACKER')
    with contextlib.ExitStack() as ctx:
        if root is None:
            root = ctx.enter_context(
                TempDirectory(kind='req-tracker')
            ).path
            ctx.enter_context(update_env_context_manager(PIP_REQ_TRACKER=root))
            logger.debug("Initialized build tracking at %s", root)

        with RequirementTracker(root) as tracker:
            yield tracker


class RequirementTracker:

    def __init__(self, root):
        # type: (str) -> None
        self._root = root
        self._entries = set()  # type: Set[InstallRequirement]
        logger.debug("Created build tracker: %s", self._root)

    def __enter__(self):
        # type: () -> RequirementTracker
        logger.debug("Entered build tracker: %s", self._root)
        return self

    def __exit__(
        self,
        exc_type,  # type: Optional[Type[BaseException]]
        exc_val,  # type: Optional[BaseException]
        exc_tb  # type: Optional[TracebackType]
    ):
        # type: (...) -> None
        self.cleanup()

    def _entry_path(self, link):
        # type: (Link) -> str
        hashed = hashlib.sha224(link.url_without_fragment.encode()).hexdigest()
        return os.path.join(self._root, hashed)

    def add(self, req):
        # type: (InstallRequirement) -> None
        """Add an InstallRequirement to build tracking.
        """

        assert req.link
        # Get the file to write information about this requirement.
        entry_path = self._entry_path(req.link)

        # Try reading from the file. If it exists and can be read from, a build
        # is already in progress, so a LookupError is raised.
        try:
            with open(entry_path) as fp:
                contents = fp.read()
        except FileNotFoundError:
            pass
        else:
            message = '{} is already being built: {}'.format(
                req.link, contents)
            raise LookupError(message)

        # If we're here, req should really not be building already.
        assert req not in self._entries

        # Start tracking this requirement.
        with open(entry_path, 'w', encoding="utf-8") as fp:
            fp.write(str(req))
        self._entries.add(req)

        logger.debug('Added %s to build tracker %r', req, self._root)

    def remove(self, req):
        # type: (InstallRequirement) -> None
        """Remove an InstallRequirement from build tracking.
        """

        assert req.link
        # Delete the created file and the corresponding entries.
        os.unlink(self._entry_path(req.link))
        self._entries.remove(req)

        logger.debug('Removed %s from build tracker %r', req, self._root)

    def cleanup(self):
        # type: () -> None
        for req in set(self._entries):
            self.remove(req)

        logger.debug("Removed build tracker: %r", self._root)

    @contextlib.contextmanager
    def track(self, req):
        # type: (InstallRequirement) -> Iterator[None]
        self.add(req)
        yield
        self.remove(req)
