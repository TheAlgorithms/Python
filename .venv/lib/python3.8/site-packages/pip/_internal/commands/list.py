import json
import logging
from optparse import Values
from typing import Iterator, List, Set, Tuple

from pip._vendor.pkg_resources import Distribution

from pip._internal.cli import cmdoptions
from pip._internal.cli.req_command import IndexGroupCommand
from pip._internal.cli.status_codes import SUCCESS
from pip._internal.exceptions import CommandError
from pip._internal.index.collector import LinkCollector
from pip._internal.index.package_finder import PackageFinder
from pip._internal.models.selection_prefs import SelectionPreferences
from pip._internal.network.session import PipSession
from pip._internal.utils.compat import stdlib_pkgs
from pip._internal.utils.misc import (
    dist_is_editable,
    get_installed_distributions,
    tabulate,
    write_output,
)
from pip._internal.utils.packaging import get_installer
from pip._internal.utils.parallel import map_multithread

logger = logging.getLogger(__name__)


class ListCommand(IndexGroupCommand):
    """
    List installed packages, including editables.

    Packages are listed in a case-insensitive sorted order.
    """

    ignore_require_venv = True
    usage = """
      %prog [options]"""

    def add_options(self):
        # type: () -> None
        self.cmd_opts.add_option(
            '-o', '--outdated',
            action='store_true',
            default=False,
            help='List outdated packages')
        self.cmd_opts.add_option(
            '-u', '--uptodate',
            action='store_true',
            default=False,
            help='List uptodate packages')
        self.cmd_opts.add_option(
            '-e', '--editable',
            action='store_true',
            default=False,
            help='List editable projects.')
        self.cmd_opts.add_option(
            '-l', '--local',
            action='store_true',
            default=False,
            help=('If in a virtualenv that has global access, do not list '
                  'globally-installed packages.'),
        )
        self.cmd_opts.add_option(
            '--user',
            dest='user',
            action='store_true',
            default=False,
            help='Only output packages installed in user-site.')
        self.cmd_opts.add_option(cmdoptions.list_path())
        self.cmd_opts.add_option(
            '--pre',
            action='store_true',
            default=False,
            help=("Include pre-release and development versions. By default, "
                  "pip only finds stable versions."),
        )

        self.cmd_opts.add_option(
            '--format',
            action='store',
            dest='list_format',
            default="columns",
            choices=('columns', 'freeze', 'json'),
            help="Select the output format among: columns (default), freeze, "
                 "or json",
        )

        self.cmd_opts.add_option(
            '--not-required',
            action='store_true',
            dest='not_required',
            help="List packages that are not dependencies of "
                 "installed packages.",
        )

        self.cmd_opts.add_option(
            '--exclude-editable',
            action='store_false',
            dest='include_editable',
            help='Exclude editable package from output.',
        )
        self.cmd_opts.add_option(
            '--include-editable',
            action='store_true',
            dest='include_editable',
            help='Include editable package from output.',
            default=True,
        )
        self.cmd_opts.add_option(cmdoptions.list_exclude())
        index_opts = cmdoptions.make_option_group(
            cmdoptions.index_group, self.parser
        )

        self.parser.insert_option_group(0, index_opts)
        self.parser.insert_option_group(0, self.cmd_opts)

    def _build_package_finder(self, options, session):
        # type: (Values, PipSession) -> PackageFinder
        """
        Create a package finder appropriate to this list command.
        """
        link_collector = LinkCollector.create(session, options=options)

        # Pass allow_yanked=False to ignore yanked versions.
        selection_prefs = SelectionPreferences(
            allow_yanked=False,
            allow_all_prereleases=options.pre,
        )

        return PackageFinder.create(
            link_collector=link_collector,
            selection_prefs=selection_prefs,
        )

    def run(self, options, args):
        # type: (Values, List[str]) -> int
        if options.outdated and options.uptodate:
            raise CommandError(
                "Options --outdated and --uptodate cannot be combined.")

        cmdoptions.check_list_path_option(options)

        skip = set(stdlib_pkgs)
        if options.excludes:
            skip.update(options.excludes)

        packages = get_installed_distributions(
            local_only=options.local,
            user_only=options.user,
            editables_only=options.editable,
            include_editables=options.include_editable,
            paths=options.path,
            skip=skip,
        )

        # get_not_required must be called firstly in order to find and
        # filter out all dependencies correctly. Otherwise a package
        # can't be identified as requirement because some parent packages
        # could be filtered out before.
        if options.not_required:
            packages = self.get_not_required(packages, options)

        if options.outdated:
            packages = self.get_outdated(packages, options)
        elif options.uptodate:
            packages = self.get_uptodate(packages, options)

        self.output_package_listing(packages, options)
        return SUCCESS

    def get_outdated(self, packages, options):
        # type: (List[Distribution], Values) -> List[Distribution]
        return [
            dist for dist in self.iter_packages_latest_infos(packages, options)
            if dist.latest_version > dist.parsed_version
        ]

    def get_uptodate(self, packages, options):
        # type: (List[Distribution], Values) -> List[Distribution]
        return [
            dist for dist in self.iter_packages_latest_infos(packages, options)
            if dist.latest_version == dist.parsed_version
        ]

    def get_not_required(self, packages, options):
        # type: (List[Distribution], Values) -> List[Distribution]
        dep_keys = set()  # type: Set[Distribution]
        for dist in packages:
            dep_keys.update(requirement.key for requirement in dist.requires())

        # Create a set to remove duplicate packages, and cast it to a list
        # to keep the return type consistent with get_outdated and
        # get_uptodate
        return list({pkg for pkg in packages if pkg.key not in dep_keys})

    def iter_packages_latest_infos(self, packages, options):
        # type: (List[Distribution], Values) -> Iterator[Distribution]
        with self._build_session(options) as session:
            finder = self._build_package_finder(options, session)

            def latest_info(dist):
                # type: (Distribution) -> Distribution
                all_candidates = finder.find_all_candidates(dist.key)
                if not options.pre:
                    # Remove prereleases
                    all_candidates = [candidate for candidate in all_candidates
                                      if not candidate.version.is_prerelease]

                evaluator = finder.make_candidate_evaluator(
                    project_name=dist.project_name,
                )
                best_candidate = evaluator.sort_best_candidate(all_candidates)
                if best_candidate is None:
                    return None

                remote_version = best_candidate.version
                if best_candidate.link.is_wheel:
                    typ = 'wheel'
                else:
                    typ = 'sdist'
                # This is dirty but makes the rest of the code much cleaner
                dist.latest_version = remote_version
                dist.latest_filetype = typ
                return dist

            for dist in map_multithread(latest_info, packages):
                if dist is not None:
                    yield dist

    def output_package_listing(self, packages, options):
        # type: (List[Distribution], Values) -> None
        packages = sorted(
            packages,
            key=lambda dist: dist.project_name.lower(),
        )
        if options.list_format == 'columns' and packages:
            data, header = format_for_columns(packages, options)
            self.output_package_listing_columns(data, header)
        elif options.list_format == 'freeze':
            for dist in packages:
                if options.verbose >= 1:
                    write_output("%s==%s (%s)", dist.project_name,
                                 dist.version, dist.location)
                else:
                    write_output("%s==%s", dist.project_name, dist.version)
        elif options.list_format == 'json':
            write_output(format_for_json(packages, options))

    def output_package_listing_columns(self, data, header):
        # type: (List[List[str]], List[str]) -> None
        # insert the header first: we need to know the size of column names
        if len(data) > 0:
            data.insert(0, header)

        pkg_strings, sizes = tabulate(data)

        # Create and add a separator.
        if len(data) > 0:
            pkg_strings.insert(1, " ".join(map(lambda x: '-' * x, sizes)))

        for val in pkg_strings:
            write_output(val)


def format_for_columns(pkgs, options):
    # type: (List[Distribution], Values) -> Tuple[List[List[str]], List[str]]
    """
    Convert the package data into something usable
    by output_package_listing_columns.
    """
    running_outdated = options.outdated
    # Adjust the header for the `pip list --outdated` case.
    if running_outdated:
        header = ["Package", "Version", "Latest", "Type"]
    else:
        header = ["Package", "Version"]

    data = []
    if options.verbose >= 1 or any(dist_is_editable(x) for x in pkgs):
        header.append("Location")
    if options.verbose >= 1:
        header.append("Installer")

    for proj in pkgs:
        # if we're working on the 'outdated' list, separate out the
        # latest_version and type
        row = [proj.project_name, proj.version]

        if running_outdated:
            row.append(proj.latest_version)
            row.append(proj.latest_filetype)

        if options.verbose >= 1 or dist_is_editable(proj):
            row.append(proj.location)
        if options.verbose >= 1:
            row.append(get_installer(proj))

        data.append(row)

    return data, header


def format_for_json(packages, options):
    # type: (List[Distribution], Values) -> str
    data = []
    for dist in packages:
        info = {
            'name': dist.project_name,
            'version': str(dist.version),
        }
        if options.verbose >= 1:
            info['location'] = dist.location
            info['installer'] = get_installer(dist)
        if options.outdated:
            info['latest_version'] = str(dist.latest_version)
            info['latest_filetype'] = dist.latest_filetype
        data.append(info)
    return json.dumps(data)
