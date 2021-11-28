import sys
import textwrap
from optparse import Values
from typing import List

from pip._internal.cli.base_command import Command
from pip._internal.cli.status_codes import SUCCESS
from pip._internal.utils.misc import get_prog

BASE_COMPLETION = """
# pip {shell} completion start{script}# pip {shell} completion end
"""

COMPLETION_SCRIPTS = {
    'bash': """
        _pip_completion()
        {{
            COMPREPLY=( $( COMP_WORDS="${{COMP_WORDS[*]}}" \\
                           COMP_CWORD=$COMP_CWORD \\
                           PIP_AUTO_COMPLETE=1 $1 2>/dev/null ) )
        }}
        complete -o default -F _pip_completion {prog}
    """,
    'zsh': """
        function _pip_completion {{
          local words cword
          read -Ac words
          read -cn cword
          reply=( $( COMP_WORDS="$words[*]" \\
                     COMP_CWORD=$(( cword-1 )) \\
                     PIP_AUTO_COMPLETE=1 $words[1] 2>/dev/null ))
        }}
        compctl -K _pip_completion {prog}
    """,
    'fish': """
        function __fish_complete_pip
            set -lx COMP_WORDS (commandline -o) ""
            set -lx COMP_CWORD ( \\
                math (contains -i -- (commandline -t) $COMP_WORDS)-1 \\
            )
            set -lx PIP_AUTO_COMPLETE 1
            string split \\  -- (eval $COMP_WORDS[1])
        end
        complete -fa "(__fish_complete_pip)" -c {prog}
    """,
}


class CompletionCommand(Command):
    """A helper command to be used for command completion."""

    ignore_require_venv = True

    def add_options(self):
        # type: () -> None
        self.cmd_opts.add_option(
            '--bash', '-b',
            action='store_const',
            const='bash',
            dest='shell',
            help='Emit completion code for bash')
        self.cmd_opts.add_option(
            '--zsh', '-z',
            action='store_const',
            const='zsh',
            dest='shell',
            help='Emit completion code for zsh')
        self.cmd_opts.add_option(
            '--fish', '-f',
            action='store_const',
            const='fish',
            dest='shell',
            help='Emit completion code for fish')

        self.parser.insert_option_group(0, self.cmd_opts)

    def run(self, options, args):
        #  type: (Values, List[str]) -> int
        """Prints the completion code of the given shell"""
        shells = COMPLETION_SCRIPTS.keys()
        shell_options = ['--' + shell for shell in sorted(shells)]
        if options.shell in shells:
            script = textwrap.dedent(
                COMPLETION_SCRIPTS.get(options.shell, '').format(
                    prog=get_prog())
            )
            print(BASE_COMPLETION.format(script=script, shell=options.shell))
            return SUCCESS
        else:
            sys.stderr.write(
                'ERROR: You must pass {}\n' .format(' or '.join(shell_options))
            )
            return SUCCESS
