# -*- coding: utf-8 -*-
# Copyright 2016-2018 Julien Danjou
# Copyright 2017 Elisey Zanko
# Copyright 2016 Étienne Bersac
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

try:
    from inspect import iscoroutinefunction
except ImportError:
    iscoroutinefunction = None

try:
    import tornado
except ImportError:
    tornado = None

import sys
import threading
import typing as t
import warnings
from abc import ABCMeta, abstractmethod
from concurrent import futures


from pip._vendor import six

from pip._vendor.tenacity import _utils

# Import all built-in retry strategies for easier usage.
from .retry import retry_base  # noqa
from .retry import retry_all  # noqa
from .retry import retry_always  # noqa
from .retry import retry_any  # noqa
from .retry import retry_if_exception  # noqa
from .retry import retry_if_exception_type  # noqa
from .retry import retry_if_not_result  # noqa
from .retry import retry_if_result  # noqa
from .retry import retry_never  # noqa
from .retry import retry_unless_exception_type  # noqa
from .retry import retry_if_exception_message  # noqa
from .retry import retry_if_not_exception_message  # noqa

# Import all nap strategies for easier usage.
from .nap import sleep  # noqa
from .nap import sleep_using_event  # noqa

# Import all built-in stop strategies for easier usage.
from .stop import stop_after_attempt  # noqa
from .stop import stop_after_delay  # noqa
from .stop import stop_all  # noqa
from .stop import stop_any  # noqa
from .stop import stop_never  # noqa
from .stop import stop_when_event_set  # noqa

# Import all built-in wait strategies for easier usage.
from .wait import wait_chain  # noqa
from .wait import wait_combine  # noqa
from .wait import wait_exponential  # noqa
from .wait import wait_fixed  # noqa
from .wait import wait_incrementing  # noqa
from .wait import wait_none  # noqa
from .wait import wait_random  # noqa
from .wait import wait_random_exponential  # noqa
from .wait import wait_random_exponential as wait_full_jitter  # noqa

# Import all built-in before strategies for easier usage.
from .before import before_log  # noqa
from .before import before_nothing  # noqa

# Import all built-in after strategies for easier usage.
from .after import after_log  # noqa
from .after import after_nothing  # noqa

# Import all built-in after strategies for easier usage.
from .before_sleep import before_sleep_log  # noqa
from .before_sleep import before_sleep_nothing  # noqa


WrappedFn = t.TypeVar("WrappedFn", bound=t.Callable)


@t.overload
def retry(fn):
    # type: (WrappedFn) -> WrappedFn
    """Type signature for @retry as a raw decorator."""
    pass


@t.overload
def retry(*dargs, **dkw):  # noqa
    # type: (...) -> t.Callable[[WrappedFn], WrappedFn]
    """Type signature for the @retry() decorator constructor."""
    pass


def retry(*dargs, **dkw):  # noqa
    """Wrap a function with a new `Retrying` object.

    :param dargs: positional arguments passed to Retrying object
    :param dkw: keyword arguments passed to the Retrying object
    """
    # support both @retry and @retry() as valid syntax
    if len(dargs) == 1 and callable(dargs[0]):
        return retry()(dargs[0])
    else:

        def wrap(f):
            if isinstance(f, retry_base):
                warnings.warn(
                    (
                        "Got retry_base instance ({cls}) as callable argument, "
                        + "this will probably hang indefinitely (did you mean "
                        + "retry={cls}(...)?)"
                    ).format(cls=f.__class__.__name__)
                )
            if iscoroutinefunction is not None and iscoroutinefunction(f):
                r = AsyncRetrying(*dargs, **dkw)
            elif (
                tornado
                and hasattr(tornado.gen, "is_coroutine_function")
                and tornado.gen.is_coroutine_function(f)
            ):
                r = TornadoRetrying(*dargs, **dkw)
            else:
                r = Retrying(*dargs, **dkw)

            return r.wraps(f)

        return wrap


class TryAgain(Exception):
    """Always retry the executed function when raised."""


NO_RESULT = object()


class DoAttempt(object):
    pass


class DoSleep(float):
    pass


class BaseAction(object):
    """Base class for representing actions to take by retry object.

    Concrete implementations must define:
    - __init__: to initialize all necessary fields
    - REPR_ATTRS: class variable specifying attributes to include in repr(self)
    - NAME: for identification in retry object methods and callbacks
    """

    REPR_FIELDS = ()
    NAME = None

    def __repr__(self):
        state_str = ", ".join(
            "%s=%r" % (field, getattr(self, field)) for field in self.REPR_FIELDS
        )
        return "%s(%s)" % (type(self).__name__, state_str)

    def __str__(self):
        return repr(self)


class RetryAction(BaseAction):
    REPR_FIELDS = ("sleep",)
    NAME = "retry"

    def __init__(self, sleep):
        self.sleep = float(sleep)


_unset = object()


def _first_set(first, second):
    return second if first is _unset else first


class RetryError(Exception):
    """Encapsulates the last attempt instance right before giving up."""

    def __init__(self, last_attempt):
        self.last_attempt = last_attempt
        super(RetryError, self).__init__(last_attempt)

    def reraise(self):
        if self.last_attempt.failed:
            raise self.last_attempt.result()
        raise self

    def __str__(self):
        return "{0}[{1}]".format(self.__class__.__name__, self.last_attempt)


class AttemptManager(object):
    """Manage attempt context."""

    def __init__(self, retry_state):
        self.retry_state = retry_state

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, BaseException):
            self.retry_state.set_exception((exc_type, exc_value, traceback))
            return True  # Swallow exception.
        else:
            # We don't have the result, actually.
            self.retry_state.set_result(None)


class BaseRetrying(object):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        sleep=sleep,
        stop=stop_never,
        wait=wait_none(),
        retry=retry_if_exception_type(),
        before=before_nothing,
        after=after_nothing,
        before_sleep=None,
        reraise=False,
        retry_error_cls=RetryError,
        retry_error_callback=None,
    ):
        self.sleep = sleep
        self.stop = stop
        self.wait = wait
        self.retry = retry
        self.before = before
        self.after = after
        self.before_sleep = before_sleep
        self.reraise = reraise
        self._local = threading.local()
        self.retry_error_cls = retry_error_cls
        self.retry_error_callback = retry_error_callback

        # This attribute was moved to RetryCallState and is deprecated on
        # Retrying objects but kept for backward compatibility.
        self.fn = None

    def copy(
        self,
        sleep=_unset,
        stop=_unset,
        wait=_unset,
        retry=_unset,
        before=_unset,
        after=_unset,
        before_sleep=_unset,
        reraise=_unset,
        retry_error_cls=_unset,
        retry_error_callback=_unset,
    ):
        """Copy this object with some parameters changed if needed."""
        return self.__class__(
            sleep=_first_set(sleep, self.sleep),
            stop=_first_set(stop, self.stop),
            wait=_first_set(wait, self.wait),
            retry=_first_set(retry, self.retry),
            before=_first_set(before, self.before),
            after=_first_set(after, self.after),
            before_sleep=_first_set(before_sleep, self.before_sleep),
            reraise=_first_set(reraise, self.reraise),
            retry_error_cls=_first_set(retry_error_cls, self.retry_error_cls),
            retry_error_callback=_first_set(
                retry_error_callback, self.retry_error_callback
            ),
        )

    def __repr__(self):
        attrs = dict(
            _utils.visible_attrs(self, attrs={"me": id(self)}),
            __class__=self.__class__.__name__,
        )
        return (
            "<%(__class__)s object at 0x%(me)x (stop=%(stop)s, "
            "wait=%(wait)s, sleep=%(sleep)s, retry=%(retry)s, "
            "before=%(before)s, after=%(after)s)>"
        ) % (attrs)

    @property
    def statistics(self):
        """Return a dictionary of runtime statistics.

        This dictionary will be empty when the controller has never been
        ran. When it is running or has ran previously it should have (but
        may not) have useful and/or informational keys and values when
        running is underway and/or completed.

        .. warning:: The keys in this dictionary **should** be some what
                     stable (not changing), but there existence **may**
                     change between major releases as new statistics are
                     gathered or removed so before accessing keys ensure that
                     they actually exist and handle when they do not.

        .. note:: The values in this dictionary are local to the thread
                  running call (so if multiple threads share the same retrying
                  object - either directly or indirectly) they will each have
                  there own view of statistics they have collected (in the
                  future we may provide a way to aggregate the various
                  statistics from each thread).
        """
        try:
            return self._local.statistics
        except AttributeError:
            self._local.statistics = {}
            return self._local.statistics

    def wraps(self, f):
        """Wrap a function for retrying.

        :param f: A function to wraps for retrying.
        """

        @_utils.wraps(f)
        def wrapped_f(*args, **kw):
            return self(f, *args, **kw)

        def retry_with(*args, **kwargs):
            return self.copy(*args, **kwargs).wraps(f)

        wrapped_f.retry = self
        wrapped_f.retry_with = retry_with

        return wrapped_f

    def begin(self, fn):
        self.statistics.clear()
        self.statistics["start_time"] = _utils.now()
        self.statistics["attempt_number"] = 1
        self.statistics["idle_for"] = 0
        self.fn = fn

    def iter(self, retry_state):  # noqa
        fut = retry_state.outcome
        if fut is None:
            if self.before is not None:
                self.before(retry_state)
            return DoAttempt()

        is_explicit_retry = retry_state.outcome.failed and isinstance(
            retry_state.outcome.exception(), TryAgain
        )
        if not (is_explicit_retry or self.retry(retry_state=retry_state)):
            return fut.result()

        if self.after is not None:
            self.after(retry_state=retry_state)

        self.statistics["delay_since_first_attempt"] = retry_state.seconds_since_start
        if self.stop(retry_state=retry_state):
            if self.retry_error_callback:
                return self.retry_error_callback(retry_state=retry_state)
            retry_exc = self.retry_error_cls(fut)
            if self.reraise:
                raise retry_exc.reraise()
            six.raise_from(retry_exc, fut.exception())

        if self.wait:
            sleep = self.wait(retry_state=retry_state)
        else:
            sleep = 0.0
        retry_state.next_action = RetryAction(sleep)
        retry_state.idle_for += sleep
        self.statistics["idle_for"] += sleep
        self.statistics["attempt_number"] += 1

        if self.before_sleep is not None:
            self.before_sleep(retry_state=retry_state)

        return DoSleep(sleep)

    def __iter__(self):
        self.begin(None)

        retry_state = RetryCallState(self, fn=None, args=(), kwargs={})
        while True:
            do = self.iter(retry_state=retry_state)
            if isinstance(do, DoAttempt):
                yield AttemptManager(retry_state=retry_state)
            elif isinstance(do, DoSleep):
                retry_state.prepare_for_next_attempt()
                self.sleep(do)
            else:
                break

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    def call(self, *args, **kwargs):
        """Use ``__call__`` instead because this method is deprecated."""
        warnings.warn(
            "'call()' method is deprecated. " + "Use '__call__()' instead",
            DeprecationWarning,
        )
        return self.__call__(*args, **kwargs)


class Retrying(BaseRetrying):
    """Retrying controller."""

    def __call__(self, fn, *args, **kwargs):
        self.begin(fn)

        retry_state = RetryCallState(retry_object=self, fn=fn, args=args, kwargs=kwargs)
        while True:
            do = self.iter(retry_state=retry_state)
            if isinstance(do, DoAttempt):
                try:
                    result = fn(*args, **kwargs)
                except BaseException:  # noqa: B902
                    retry_state.set_exception(sys.exc_info())
                else:
                    retry_state.set_result(result)
            elif isinstance(do, DoSleep):
                retry_state.prepare_for_next_attempt()
                self.sleep(do)
            else:
                return do


class Future(futures.Future):
    """Encapsulates a (future or past) attempted call to a target function."""

    def __init__(self, attempt_number):
        super(Future, self).__init__()
        self.attempt_number = attempt_number

    @property
    def failed(self):
        """Return whether a exception is being held in this future."""
        return self.exception() is not None

    @classmethod
    def construct(cls, attempt_number, value, has_exception):
        """Construct a new Future object."""
        fut = cls(attempt_number)
        if has_exception:
            fut.set_exception(value)
        else:
            fut.set_result(value)
        return fut


class RetryCallState(object):
    """State related to a single call wrapped with Retrying."""

    def __init__(self, retry_object, fn, args, kwargs):
        #: Retry call start timestamp
        self.start_time = _utils.now()
        #: Retry manager object
        self.retry_object = retry_object
        #: Function wrapped by this retry call
        self.fn = fn
        #: Arguments of the function wrapped by this retry call
        self.args = args
        #: Keyword arguments of the function wrapped by this retry call
        self.kwargs = kwargs

        #: The number of the current attempt
        self.attempt_number = 1
        #: Last outcome (result or exception) produced by the function
        self.outcome = None
        #: Timestamp of the last outcome
        self.outcome_timestamp = None
        #: Time spent sleeping in retries
        self.idle_for = 0
        #: Next action as decided by the retry manager
        self.next_action = None

    @property
    def seconds_since_start(self):
        if self.outcome_timestamp is None:
            return None
        return self.outcome_timestamp - self.start_time

    def prepare_for_next_attempt(self):
        self.outcome = None
        self.outcome_timestamp = None
        self.attempt_number += 1
        self.next_action = None

    def set_result(self, val):
        ts = _utils.now()
        fut = Future(self.attempt_number)
        fut.set_result(val)
        self.outcome, self.outcome_timestamp = fut, ts

    def set_exception(self, exc_info):
        ts = _utils.now()
        fut = Future(self.attempt_number)
        _utils.capture(fut, exc_info)
        self.outcome, self.outcome_timestamp = fut, ts


if iscoroutinefunction:
    from pip._vendor.tenacity._asyncio import AsyncRetrying

if tornado:
    from pip._vendor.tenacity.tornadoweb import TornadoRetrying
