"""
Customized Mixin2to3 support:

 - adds support for converting doctests
"""

import warnings
from distutils.util import Mixin2to3 as _Mixin2to3
from distutils import log
from lib2to3.refactor import RefactoringTool, get_fixers_from_package

import setuptools
from ._deprecation_warning import SetuptoolsDeprecationWarning


class DistutilsRefactoringTool(RefactoringTool):
    def log_error(self, msg, *args, **kw):
        log.error(msg, *args)

    def log_message(self, msg, *args):
        log.info(msg, *args)

    def log_debug(self, msg, *args):
        log.debug(msg, *args)


class Mixin2to3(_Mixin2to3):
    def run_2to3(self, files, doctests=False):
        # See of the distribution option has been set, otherwise check the
        # setuptools default.
        if self.distribution.use_2to3 is not True:
            return
        if not files:
            return

        warnings.warn(
            "2to3 support is deprecated. If the project still "
            "requires Python 2 support, please migrate to "
            "a single-codebase solution or employ an "
            "independent conversion process.",
            SetuptoolsDeprecationWarning)
        log.info("Fixing " + " ".join(files))
        self.__build_fixer_names()
        self.__exclude_fixers()
        if doctests:
            if setuptools.run_2to3_on_doctests:
                r = DistutilsRefactoringTool(self.fixer_names)
                r.refactor(files, write=True, doctests_only=True)
        else:
            _Mixin2to3.run_2to3(self, files)

    def __build_fixer_names(self):
        if self.fixer_names:
            return
        self.fixer_names = []
        for p in setuptools.lib2to3_fixer_packages:
            self.fixer_names.extend(get_fixers_from_package(p))
        if self.distribution.use_2to3_fixers is not None:
            for p in self.distribution.use_2to3_fixers:
                self.fixer_names.extend(get_fixers_from_package(p))

    def __exclude_fixers(self):
        excluded_fixers = getattr(self, 'exclude_fixers', [])
        if self.distribution.use_2to3_exclude_fixers is not None:
            excluded_fixers.extend(self.distribution.use_2to3_exclude_fixers)
        for fixer_name in excluded_fixers:
            if fixer_name in self.fixer_names:
                self.fixer_names.remove(fixer_name)
