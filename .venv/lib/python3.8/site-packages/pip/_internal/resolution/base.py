from typing import Callable, List

from pip._internal.req.req_install import InstallRequirement
from pip._internal.req.req_set import RequirementSet

InstallRequirementProvider = Callable[[str, InstallRequirement], InstallRequirement]


class BaseResolver:
    def resolve(self, root_reqs, check_supported_wheels):
        # type: (List[InstallRequirement], bool) -> RequirementSet
        raise NotImplementedError()

    def get_installation_order(self, req_set):
        # type: (RequirementSet) -> List[InstallRequirement]
        raise NotImplementedError()
