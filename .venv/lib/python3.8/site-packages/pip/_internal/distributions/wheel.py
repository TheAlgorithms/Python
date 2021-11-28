from zipfile import ZipFile

from pip._vendor.pkg_resources import Distribution

from pip._internal.distributions.base import AbstractDistribution
from pip._internal.index.package_finder import PackageFinder
from pip._internal.utils.wheel import pkg_resources_distribution_for_wheel


class WheelDistribution(AbstractDistribution):
    """Represents a wheel distribution.

    This does not need any preparation as wheels can be directly unpacked.
    """

    def get_pkg_resources_distribution(self):
        # type: () -> Distribution
        """Loads the metadata from the wheel file into memory and returns a
        Distribution that uses it, not relying on the wheel file or
        requirement.
        """
        # Set as part of preparation during download.
        assert self.req.local_file_path
        # Wheels are never unnamed.
        assert self.req.name

        with ZipFile(self.req.local_file_path, allowZip64=True) as z:
            return pkg_resources_distribution_for_wheel(
                z, self.req.name, self.req.local_file_path
            )

    def prepare_distribution_metadata(self, finder, build_isolation):
        # type: (PackageFinder, bool) -> None
        pass
