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


def before_nothing(retry_state):
    """Before call strategy that does nothing."""


def before_log(logger, log_level):
    """Before call strategy that logs to some logger the attempt."""

    def log_it(retry_state):
        logger.log(
            log_level,
            "Starting call to '%s', this is the %s time calling it.",
            _utils.get_callback_name(retry_state.fn),
            _utils.to_ordinal(retry_state.attempt_number),
        )

    return log_it
