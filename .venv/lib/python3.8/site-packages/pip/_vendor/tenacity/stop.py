# -*- encoding: utf-8 -*-
#
# Copyright 2016–2021 Julien Danjou
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
import abc

from pip._vendor import six


@six.add_metaclass(abc.ABCMeta)
class stop_base(object):
    """Abstract base class for stop strategies."""

    @abc.abstractmethod
    def __call__(self, retry_state):
        pass

    def __and__(self, other):
        return stop_all(self, other)

    def __or__(self, other):
        return stop_any(self, other)


class stop_any(stop_base):
    """Stop if any of the stop condition is valid."""

    def __init__(self, *stops):
        self.stops = stops

    def __call__(self, retry_state):
        return any(x(retry_state) for x in self.stops)


class stop_all(stop_base):
    """Stop if all the stop conditions are valid."""

    def __init__(self, *stops):
        self.stops = stops

    def __call__(self, retry_state):
        return all(x(retry_state) for x in self.stops)


class _stop_never(stop_base):
    """Never stop."""

    def __call__(self, retry_state):
        return False


stop_never = _stop_never()


class stop_when_event_set(stop_base):
    """Stop when the given event is set."""

    def __init__(self, event):
        self.event = event

    def __call__(self, retry_state):
        return self.event.is_set()


class stop_after_attempt(stop_base):
    """Stop when the previous attempt >= max_attempt."""

    def __init__(self, max_attempt_number):
        self.max_attempt_number = max_attempt_number

    def __call__(self, retry_state):
        return retry_state.attempt_number >= self.max_attempt_number


class stop_after_delay(stop_base):
    """Stop when the time from the first attempt >= limit."""

    def __init__(self, max_delay):
        self.max_delay = max_delay

    def __call__(self, retry_state):
        return retry_state.seconds_since_start >= self.max_delay
