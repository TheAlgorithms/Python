"""Nicer log formatting with colours.

Code copied from Tornado, Apache licensed.
"""
# Copyright 2012 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import sys

try:
    import curses
except ImportError:
    curses = None


def _stderr_supports_color():
    color = False
    if curses and hasattr(sys.stderr, 'isatty') and sys.stderr.isatty():
        try:
            curses.setupterm()
            if curses.tigetnum("colors") > 0:
                color = True
        except Exception:
            pass
    return color


class LogFormatter(logging.Formatter):
    """Log formatter with colour support
    """
    DEFAULT_COLORS = {
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 1,
    }

    def __init__(self, color=True, datefmt=None):
        r"""
        :arg bool color: Enables color support.
        :arg string fmt: Log message format.
        It will be applied to the attributes dict of log records. The
        text between ``%(color)s`` and ``%(end_color)s`` will be colored
        depending on the level if color support is on.
        :arg dict colors: color mappings from logging level to terminal color
        code
        :arg string datefmt: Datetime format.
        Used for formatting ``(asctime)`` placeholder in ``prefix_fmt``.
        .. versionchanged:: 3.2
        Added ``fmt`` and ``datefmt`` arguments.
        """
        logging.Formatter.__init__(self, datefmt=datefmt)
        self._colors = {}
        if color and _stderr_supports_color():
            # The curses module has some str/bytes confusion in
            # python3. Until version 3.2.3, most methods return
            # bytes, but only accept strings. In addition, we want to
            # output these strings with the logging module, which
            # works with unicode strings. The explicit calls to
            # unicode() below are harmless in python2 but will do the
            # right conversion in python 3.
            fg_color = (curses.tigetstr("setaf") or
                        curses.tigetstr("setf") or "")
            if (3, 0) < sys.version_info < (3, 2, 3):
                fg_color = str(fg_color, "ascii")

            for levelno, code in self.DEFAULT_COLORS.items():
                self._colors[levelno] = str(
                    curses.tparm(fg_color, code), "ascii")
            self._normal = str(curses.tigetstr("sgr0"), "ascii")

            scr = curses.initscr()
            self.termwidth = scr.getmaxyx()[1]
            curses.endwin()
        else:
            self._normal = ''
            # Default width is usually 80, but too wide is
            # worse than too narrow
            self.termwidth = 70

    def formatMessage(self, record):
        mlen = len(record.message)
        right_text = '{initial}-{name}'.format(initial=record.levelname[0],
                                               name=record.name)
        if mlen + len(right_text) < self.termwidth:
            space = ' ' * (self.termwidth - (mlen + len(right_text)))
        else:
            space = '  '

        if record.levelno in self._colors:
            start_color = self._colors[record.levelno]
            end_color = self._normal
        else:
            start_color = end_color = ''

        return record.message + space + start_color + right_text + end_color


def enable_colourful_output(level=logging.INFO):
    handler = logging.StreamHandler()
    handler.setFormatter(LogFormatter())
    logging.root.addHandler(handler)
    logging.root.setLevel(level)
