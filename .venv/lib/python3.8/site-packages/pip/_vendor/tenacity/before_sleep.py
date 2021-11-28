# Copyright 2016 Julien Danjou
# Copyright 2016 Joshua Harlow
# Copyright 2013-2014 Ray Holder
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pip._vendor.tenacity import _utils
from pip._vendor.tenacity.compat import get_exc_info_from_future


def before_sleep_nothing(retry_state):
    """Before call strategy that does nothing."""


def before_sleep_log(logger, log_level, exc_info=False):
    """Before call strategy that logs to some logger the attempt."""

    def log_it(retry_state):
        if retry_state.outcome.failed:
            ex = retry_state.outcome.exception()
            verb, value = "raised", "%s: %s" % (type(ex).__name__, ex)

            if exc_info:
                local_exc_info = get_exc_info_from_future(retry_state.outcome)
            else:
                local_exc_info = False
        else:
            verb, value = "returned", retry_state.outcome.result()
            local_exc_info = False  # exc_info does not apply when no exception

        logger.log(
            log_level,
            "Retrying %s in %s seconds as it %s %s.",
            _utils.get_callback_name(retry_state.fn),
            getattr(retry_state.next_action, "sleep"),
            verb,
            value,
            exc_info=local_exc_info,
        )

    return log_it
