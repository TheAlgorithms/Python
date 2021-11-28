"""
A module that implements tooling to enable easy warnings about deprecations.
"""

import logging
import warnings
from typing import Any, Optional, TextIO, Type, Union

from pip._vendor.packaging.version import parse

from pip import __version__ as current_version

DEPRECATION_MSG_PREFIX = "DEPRECATION: "


class PipDeprecationWarning(Warning):
    pass


_original_showwarning = None  # type: Any


# Warnings <-> Logging Integration
def _showwarning(
    message,  # type: Union[Warning, str]
    category,  # type: Type[Warning]
    filename,  # type: str
    lineno,  # type: int
    file=None,  # type: Optional[TextIO]
    line=None,  # type: Optional[str]
):
    # type: (...) -> None
    if file is not None:
        if _original_showwarning is not None:
            _original_showwarning(message, category, filename, lineno, file, line)
    elif issubclass(category, PipDeprecationWarning):
        # We use a specially named logger which will handle all of the
        # deprecation messages for pip.
        logger = logging.getLogger("pip._internal.deprecations")
        logger.warning(message)
    else:
        _original_showwarning(message, category, filename, lineno, file, line)


def install_warning_logger():
    # type: () -> None
    # Enable our Deprecation Warnings
    warnings.simplefilter("default", PipDeprecationWarning, append=True)

    global _original_showwarning

    if _original_showwarning is None:
        _original_showwarning = warnings.showwarning
        warnings.showwarning = _showwarning


def deprecated(reason, replacement, gone_in, issue=None):
    # type: (str, Optional[str], Optional[str], Optional[int]) -> None
    """Helper to deprecate existing functionality.

    reason:
        Textual reason shown to the user about why this functionality has
        been deprecated.
    replacement:
        Textual suggestion shown to the user about what alternative
        functionality they can use.
    gone_in:
        The version of pip does this functionality should get removed in.
        Raises errors if pip's current version is greater than or equal to
        this.
    issue:
        Issue number on the tracker that would serve as a useful place for
        users to find related discussion and provide feedback.

    Always pass replacement, gone_in and issue as keyword arguments for clarity
    at the call site.
    """

    # Construct a nice message.
    #   This is eagerly formatted as we want it to get logged as if someone
    #   typed this entire message out.
    sentences = [
        (reason, DEPRECATION_MSG_PREFIX + "{}"),
        (gone_in, "pip {} will remove support for this functionality."),
        (replacement, "A possible replacement is {}."),
        (
            issue,
            (
                "You can find discussion regarding this at "
                "https://github.com/pypa/pip/issues/{}."
            ),
        ),
    ]
    message = " ".join(
        template.format(val) for val, template in sentences if val is not None
    )

    # Raise as an error if it has to be removed.
    if gone_in is not None and parse(current_version) >= parse(gone_in):
        raise PipDeprecationWarning(message)

    warnings.warn(message, category=PipDeprecationWarning, stacklevel=2)
