"""Check a project and backend by attempting to build using PEP 517 hooks.
"""
import argparse
import logging
import os
from os.path import isfile, join as pjoin
from pip._vendor.toml import TomlDecodeError, load as toml_load
import shutil
from subprocess import CalledProcessError
import sys
import tarfile
from tempfile import mkdtemp
import zipfile

from .colorlog import enable_colourful_output
from .envbuild import BuildEnvironment
from .wrappers import Pep517HookCaller

log = logging.getLogger(__name__)


def check_build_sdist(hooks, build_sys_requires):
    with BuildEnvironment() as env:
        try:
            env.pip_install(build_sys_requires)
            log.info('Installed static build dependencies')
        except CalledProcessError:
            log.error('Failed to install static build dependencies')
            return False

        try:
            reqs = hooks.get_requires_for_build_sdist({})
            log.info('Got build requires: %s', reqs)
        except Exception:
            log.error('Failure in get_requires_for_build_sdist', exc_info=True)
            return False

        try:
            env.pip_install(reqs)
            log.info('Installed dynamic build dependencies')
        except CalledProcessError:
            log.error('Failed to install dynamic build dependencies')
            return False

        td = mkdtemp()
        log.info('Trying to build sdist in %s', td)
        try:
            try:
                filename = hooks.build_sdist(td, {})
                log.info('build_sdist returned %r', filename)
            except Exception:
                log.info('Failure in build_sdist', exc_info=True)
                return False

            if not filename.endswith('.tar.gz'):
                log.error(
                    "Filename %s doesn't have .tar.gz extension", filename)
                return False

            path = pjoin(td, filename)
            if isfile(path):
                log.info("Output file %s exists", path)
            else:
                log.error("Output file %s does not exist", path)
                return False

            if tarfile.is_tarfile(path):
                log.info("Output file is a tar file")
            else:
                log.error("Output file is not a tar file")
                return False

        finally:
            shutil.rmtree(td)

        return True


def check_build_wheel(hooks, build_sys_requires):
    with BuildEnvironment() as env:
        try:
            env.pip_install(build_sys_requires)
            log.info('Installed static build dependencies')
        except CalledProcessError:
            log.error('Failed to install static build dependencies')
            return False

        try:
            reqs = hooks.get_requires_for_build_wheel({})
            log.info('Got build requires: %s', reqs)
        except Exception:
            log.error('Failure in get_requires_for_build_sdist', exc_info=True)
            return False

        try:
            env.pip_install(reqs)
            log.info('Installed dynamic build dependencies')
        except CalledProcessError:
            log.error('Failed to install dynamic build dependencies')
            return False

        td = mkdtemp()
        log.info('Trying to build wheel in %s', td)
        try:
            try:
                filename = hooks.build_wheel(td, {})
                log.info('build_wheel returned %r', filename)
            except Exception:
                log.info('Failure in build_wheel', exc_info=True)
                return False

            if not filename.endswith('.whl'):
                log.error("Filename %s doesn't have .whl extension", filename)
                return False

            path = pjoin(td, filename)
            if isfile(path):
                log.info("Output file %s exists", path)
            else:
                log.error("Output file %s does not exist", path)
                return False

            if zipfile.is_zipfile(path):
                log.info("Output file is a zip file")
            else:
                log.error("Output file is not a zip file")
                return False

        finally:
            shutil.rmtree(td)

        return True


def check(source_dir):
    pyproject = pjoin(source_dir, 'pyproject.toml')
    if isfile(pyproject):
        log.info('Found pyproject.toml')
    else:
        log.error('Missing pyproject.toml')
        return False

    try:
        with open(pyproject) as f:
            pyproject_data = toml_load(f)
        # Ensure the mandatory data can be loaded
        buildsys = pyproject_data['build-system']
        requires = buildsys['requires']
        backend = buildsys['build-backend']
        backend_path = buildsys.get('backend-path')
        log.info('Loaded pyproject.toml')
    except (TomlDecodeError, KeyError):
        log.error("Invalid pyproject.toml", exc_info=True)
        return False

    hooks = Pep517HookCaller(source_dir, backend, backend_path)

    sdist_ok = check_build_sdist(hooks, requires)
    wheel_ok = check_build_wheel(hooks, requires)

    if not sdist_ok:
        log.warning('Sdist checks failed; scroll up to see')
    if not wheel_ok:
        log.warning('Wheel checks failed')

    return sdist_ok


def main(argv=None):
    log.warning('pep517.check is deprecated. '
                'Consider switching to https://pypi.org/project/build/')

    ap = argparse.ArgumentParser()
    ap.add_argument(
        'source_dir',
        help="A directory containing pyproject.toml")
    args = ap.parse_args(argv)

    enable_colourful_output()

    ok = check(args.source_dir)

    if ok:
        print(ansi('Checks passed', 'green'))
    else:
        print(ansi('Checks failed', 'red'))
        sys.exit(1)


ansi_codes = {
    'reset': '\x1b[0m',
    'bold': '\x1b[1m',
    'red': '\x1b[31m',
    'green': '\x1b[32m',
}


def ansi(s, attr):
    if os.name != 'nt' and sys.stdout.isatty():
        return ansi_codes[attr] + str(s) + ansi_codes['reset']
    else:
        return str(s)


if __name__ == '__main__':
    main()
