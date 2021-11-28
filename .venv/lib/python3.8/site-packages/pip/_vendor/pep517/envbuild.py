"""Build wheels/sdists by installing build deps to a temporary environment.
"""

import os
import logging
from pip._vendor import toml
import shutil
from subprocess import check_call
import sys
from sysconfig import get_paths
from tempfile import mkdtemp

from .wrappers import Pep517HookCaller, LoggerWrapper

log = logging.getLogger(__name__)


def _load_pyproject(source_dir):
    with open(os.path.join(source_dir, 'pyproject.toml')) as f:
        pyproject_data = toml.load(f)
    buildsys = pyproject_data['build-system']
    return (
        buildsys['requires'],
        buildsys['build-backend'],
        buildsys.get('backend-path'),
    )


class BuildEnvironment(object):
    """Context manager to install build deps in a simple temporary environment

    Based on code I wrote for pip, which is MIT licensed.
    """
    # Copyright (c) 2008-2016 The pip developers (see AUTHORS.txt file)
    #
    # Permission is hereby granted, free of charge, to any person obtaining
    # a copy of this software and associated documentation files (the
    # "Software"), to deal in the Software without restriction, including
    # without limitation the rights to use, copy, modify, merge, publish,
    # distribute, sublicense, and/or sell copies of the Software, and to
    # permit persons to whom the Software is furnished to do so, subject to
    # the following conditions:
    #
    # The above copyright notice and this permission notice shall be
    # included in all copies or substantial portions of the Software.
    #
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    # EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    # MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    # NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    # LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
    # OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    # WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    path = None

    def __init__(self, cleanup=True):
        self._cleanup = cleanup

    def __enter__(self):
        self.path = mkdtemp(prefix='pep517-build-env-')
        log.info('Temporary build environment: %s', self.path)

        self.save_path = os.environ.get('PATH', None)
        self.save_pythonpath = os.environ.get('PYTHONPATH', None)

        install_scheme = 'nt' if (os.name == 'nt') else 'posix_prefix'
        install_dirs = get_paths(install_scheme, vars={
            'base': self.path,
            'platbase': self.path,
        })

        scripts = install_dirs['scripts']
        if self.save_path:
            os.environ['PATH'] = scripts + os.pathsep + self.save_path
        else:
            os.environ['PATH'] = scripts + os.pathsep + os.defpath

        if install_dirs['purelib'] == install_dirs['platlib']:
            lib_dirs = install_dirs['purelib']
        else:
            lib_dirs = install_dirs['purelib'] + os.pathsep + \
                install_dirs['platlib']
        if self.save_pythonpath:
            os.environ['PYTHONPATH'] = lib_dirs + os.pathsep + \
                self.save_pythonpath
        else:
            os.environ['PYTHONPATH'] = lib_dirs

        return self

    def pip_install(self, reqs):
        """Install dependencies into this env by calling pip in a subprocess"""
        if not reqs:
            return
        log.info('Calling pip to install %s', reqs)
        cmd = [
            sys.executable, '-m', 'pip', 'install', '--ignore-installed',
            '--prefix', self.path] + list(reqs)
        check_call(
            cmd,
            stdout=LoggerWrapper(log, logging.INFO),
            stderr=LoggerWrapper(log, logging.ERROR),
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        needs_cleanup = (
            self._cleanup and
            self.path is not None and
            os.path.isdir(self.path)
        )
        if needs_cleanup:
            shutil.rmtree(self.path)

        if self.save_path is None:
            os.environ.pop('PATH', None)
        else:
            os.environ['PATH'] = self.save_path

        if self.save_pythonpath is None:
            os.environ.pop('PYTHONPATH', None)
        else:
            os.environ['PYTHONPATH'] = self.save_pythonpath


def build_wheel(source_dir, wheel_dir, config_settings=None):
    """Build a wheel from a source directory using PEP 517 hooks.

    :param str source_dir: Source directory containing pyproject.toml
    :param str wheel_dir: Target directory to create wheel in
    :param dict config_settings: Options to pass to build backend

    This is a blocking function which will run pip in a subprocess to install
    build requirements.
    """
    if config_settings is None:
        config_settings = {}
    requires, backend, backend_path = _load_pyproject(source_dir)
    hooks = Pep517HookCaller(source_dir, backend, backend_path)

    with BuildEnvironment() as env:
        env.pip_install(requires)
        reqs = hooks.get_requires_for_build_wheel(config_settings)
        env.pip_install(reqs)
        return hooks.build_wheel(wheel_dir, config_settings)


def build_sdist(source_dir, sdist_dir, config_settings=None):
    """Build an sdist from a source directory using PEP 517 hooks.

    :param str source_dir: Source directory containing pyproject.toml
    :param str sdist_dir: Target directory to place sdist in
    :param dict config_settings: Options to pass to build backend

    This is a blocking function which will run pip in a subprocess to install
    build requirements.
    """
    if config_settings is None:
        config_settings = {}
    requires, backend, backend_path = _load_pyproject(source_dir)
    hooks = Pep517HookCaller(source_dir, backend, backend_path)

    with BuildEnvironment() as env:
        env.pip_install(requires)
        reqs = hooks.get_requires_for_build_sdist(config_settings)
        env.pip_install(reqs)
        return hooks.build_sdist(sdist_dir, config_settings)
