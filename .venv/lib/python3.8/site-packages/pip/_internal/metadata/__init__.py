from typing import List, Optional

from .base import BaseDistribution, BaseEnvironment


def get_default_environment():
    # type: () -> BaseEnvironment
    """Get the default representation for the current environment.

    This returns an Environment instance from the chosen backend. The default
    Environment instance should be built from ``sys.path`` and may use caching
    to share instance state accorss calls.
    """
    from .pkg_resources import Environment

    return Environment.default()


def get_environment(paths):
    # type: (Optional[List[str]]) -> BaseEnvironment
    """Get a representation of the environment specified by ``paths``.

    This returns an Environment instance from the chosen backend based on the
    given import paths. The backend must build a fresh instance representing
    the state of installed distributions when this function is called.
    """
    from .pkg_resources import Environment

    return Environment.from_paths(paths)


def get_wheel_distribution(wheel_path, canonical_name):
    # type: (str, str) -> BaseDistribution
    """Get the representation of the specified wheel's distribution metadata.

    This returns a Distribution instance from the chosen backend based on
    the given wheel's ``.dist-info`` directory.

    :param canonical_name: Normalized project name of the given wheel.
    """
    from .pkg_resources import Distribution

    return Distribution.from_wheel(wheel_path, canonical_name)
