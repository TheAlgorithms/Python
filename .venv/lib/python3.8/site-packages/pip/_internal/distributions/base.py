import abc
from typing import Optional

from pip._vendor.pkg_resources import Distribution

from pip._internal.index.package_finder import PackageFinder
from pip._internal.req import InstallRequirement


class AbstractDistribution(metaclass=abc.ABCMeta):
    """A base class for handling installable artifacts.

    The requirements for anything installable are as follows:

     - we must be able to determine the requirement name
       (or we can't correctly handle the non-upgrade case).

     - for packages with setup requirements, we must also be able
       to determine their requirements without installing additional
       packages (for the same reason as run-time dependencies)

     - we must be able to create a Distribution object exposing the
       above metadata.
    """

    def __init__(self, req):
        # type: (InstallRequirement) -> None
        super().__init__()
        self.req = req

    @abc.abstractmethod
    def get_pkg_resources_distribution(self):
        # type: () -> Optional[Distribution]
        raise NotImplementedError()

    @abc.abstractmethod
    def prepare_distribution_metadata(self, finder, build_isolation):
        # type: (PackageFinder, bool) -> None
        raise NotImplementedError()
