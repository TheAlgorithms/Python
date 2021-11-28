import logging
import os
import shlex
import subprocess
from typing import Any, Callable, Iterable, List, Mapping, Optional, Union

from pip._internal.cli.spinners import SpinnerInterface, open_spinner
from pip._internal.exceptions import InstallationSubprocessError
from pip._internal.utils.logging import subprocess_logger
from pip._internal.utils.misc import HiddenText

CommandArgs = List[Union[str, HiddenText]]


LOG_DIVIDER = "----------------------------------------"


def make_command(*args):
    # type: (Union[str, HiddenText, CommandArgs]) -> CommandArgs
    """
    Create a CommandArgs object.
    """
    command_args = []  # type: CommandArgs
    for arg in args:
        # Check for list instead of CommandArgs since CommandArgs is
        # only known during type-checking.
        if isinstance(arg, list):
            command_args.extend(arg)
        else:
            # Otherwise, arg is str or HiddenText.
            command_args.append(arg)

    return command_args


def format_command_args(args):
    # type: (Union[List[str], CommandArgs]) -> str
    """
    Format command arguments for display.
    """
    # For HiddenText arguments, display the redacted form by calling str().
    # Also, we don't apply str() to arguments that aren't HiddenText since
    # this can trigger a UnicodeDecodeError in Python 2 if the argument
    # has type unicode and includes a non-ascii character.  (The type
    # checker doesn't ensure the annotations are correct in all cases.)
    return " ".join(
        shlex.quote(str(arg)) if isinstance(arg, HiddenText) else shlex.quote(arg)
        for arg in args
    )


def reveal_command_args(args):
    # type: (Union[List[str], CommandArgs]) -> List[str]
    """
    Return the arguments in their raw, unredacted form.
    """
    return [arg.secret if isinstance(arg, HiddenText) else arg for arg in args]


def make_subprocess_output_error(
    cmd_args,  # type: Union[List[str], CommandArgs]
    cwd,  # type: Optional[str]
    lines,  # type: List[str]
    exit_status,  # type: int
):
    # type: (...) -> str
    """
    Create and return the error message to use to log a subprocess error
    with command output.

    :param lines: A list of lines, each ending with a newline.
    """
    command = format_command_args(cmd_args)

    # We know the joined output value ends in a newline.
    output = "".join(lines)
    msg = (
        # Use a unicode string to avoid "UnicodeEncodeError: 'ascii'
        # codec can't encode character ..." in Python 2 when a format
        # argument (e.g. `output`) has a non-ascii character.
        "Command errored out with exit status {exit_status}:\n"
        " command: {command_display}\n"
        "     cwd: {cwd_display}\n"
        "Complete output ({line_count} lines):\n{output}{divider}"
    ).format(
        exit_status=exit_status,
        command_display=command,
        cwd_display=cwd,
        line_count=len(lines),
        output=output,
        divider=LOG_DIVIDER,
    )
    return msg


def call_subprocess(
    cmd,  # type: Union[List[str], CommandArgs]
    show_stdout=False,  # type: bool
    cwd=None,  # type: Optional[str]
    on_returncode="raise",  # type: str
    extra_ok_returncodes=None,  # type: Optional[Iterable[int]]
    command_desc=None,  # type: Optional[str]
    extra_environ=None,  # type: Optional[Mapping[str, Any]]
    unset_environ=None,  # type: Optional[Iterable[str]]
    spinner=None,  # type: Optional[SpinnerInterface]
    log_failed_cmd=True,  # type: Optional[bool]
    stdout_only=False,  # type: Optional[bool]
):
    # type: (...) -> str
    """
    Args:
      show_stdout: if true, use INFO to log the subprocess's stderr and
        stdout streams.  Otherwise, use DEBUG.  Defaults to False.
      extra_ok_returncodes: an iterable of integer return codes that are
        acceptable, in addition to 0. Defaults to None, which means [].
      unset_environ: an iterable of environment variable names to unset
        prior to calling subprocess.Popen().
      log_failed_cmd: if false, failed commands are not logged, only raised.
      stdout_only: if true, return only stdout, else return both. When true,
        logging of both stdout and stderr occurs when the subprocess has
        terminated, else logging occurs as subprocess output is produced.
    """
    if extra_ok_returncodes is None:
        extra_ok_returncodes = []
    if unset_environ is None:
        unset_environ = []
    # Most places in pip use show_stdout=False. What this means is--
    #
    # - We connect the child's output (combined stderr and stdout) to a
    #   single pipe, which we read.
    # - We log this output to stderr at DEBUG level as it is received.
    # - If DEBUG logging isn't enabled (e.g. if --verbose logging wasn't
    #   requested), then we show a spinner so the user can still see the
    #   subprocess is in progress.
    # - If the subprocess exits with an error, we log the output to stderr
    #   at ERROR level if it hasn't already been displayed to the console
    #   (e.g. if --verbose logging wasn't enabled).  This way we don't log
    #   the output to the console twice.
    #
    # If show_stdout=True, then the above is still done, but with DEBUG
    # replaced by INFO.
    if show_stdout:
        # Then log the subprocess output at INFO level.
        log_subprocess = subprocess_logger.info
        used_level = logging.INFO
    else:
        # Then log the subprocess output using DEBUG.  This also ensures
        # it will be logged to the log file (aka user_log), if enabled.
        log_subprocess = subprocess_logger.debug
        used_level = logging.DEBUG

    # Whether the subprocess will be visible in the console.
    showing_subprocess = subprocess_logger.getEffectiveLevel() <= used_level

    # Only use the spinner if we're not showing the subprocess output
    # and we have a spinner.
    use_spinner = not showing_subprocess and spinner is not None

    if command_desc is None:
        command_desc = format_command_args(cmd)

    log_subprocess("Running command %s", command_desc)
    env = os.environ.copy()
    if extra_environ:
        env.update(extra_environ)
    for name in unset_environ:
        env.pop(name, None)
    try:
        proc = subprocess.Popen(
            # Convert HiddenText objects to the underlying str.
            reveal_command_args(cmd),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT if not stdout_only else subprocess.PIPE,
            cwd=cwd,
            env=env,
            errors="backslashreplace",
        )
    except Exception as exc:
        if log_failed_cmd:
            subprocess_logger.critical(
                "Error %s while executing command %s",
                exc,
                command_desc,
            )
        raise
    all_output = []
    if not stdout_only:
        assert proc.stdout
        assert proc.stdin
        proc.stdin.close()
        # In this mode, stdout and stderr are in the same pipe.
        while True:
            line = proc.stdout.readline()  # type: str
            if not line:
                break
            line = line.rstrip()
            all_output.append(line + "\n")

            # Show the line immediately.
            log_subprocess(line)
            # Update the spinner.
            if use_spinner:
                assert spinner
                spinner.spin()
        try:
            proc.wait()
        finally:
            if proc.stdout:
                proc.stdout.close()
        output = "".join(all_output)
    else:
        # In this mode, stdout and stderr are in different pipes.
        # We must use communicate() which is the only safe way to read both.
        out, err = proc.communicate()
        # log line by line to preserve pip log indenting
        for out_line in out.splitlines():
            log_subprocess(out_line)
        all_output.append(out)
        for err_line in err.splitlines():
            log_subprocess(err_line)
        all_output.append(err)
        output = out

    proc_had_error = proc.returncode and proc.returncode not in extra_ok_returncodes
    if use_spinner:
        assert spinner
        if proc_had_error:
            spinner.finish("error")
        else:
            spinner.finish("done")
    if proc_had_error:
        if on_returncode == "raise":
            if not showing_subprocess and log_failed_cmd:
                # Then the subprocess streams haven't been logged to the
                # console yet.
                msg = make_subprocess_output_error(
                    cmd_args=cmd,
                    cwd=cwd,
                    lines=all_output,
                    exit_status=proc.returncode,
                )
                subprocess_logger.error(msg)
            raise InstallationSubprocessError(proc.returncode, command_desc)
        elif on_returncode == "warn":
            subprocess_logger.warning(
                'Command "%s" had error code %s in %s',
                command_desc,
                proc.returncode,
                cwd,
            )
        elif on_returncode == "ignore":
            pass
        else:
            raise ValueError(f"Invalid value: on_returncode={on_returncode!r}")
    return output


def runner_with_spinner_message(message):
    # type: (str) -> Callable[..., None]
    """Provide a subprocess_runner that shows a spinner message.

    Intended for use with for pep517's Pep517HookCaller. Thus, the runner has
    an API that matches what's expected by Pep517HookCaller.subprocess_runner.
    """

    def runner(
        cmd,  # type: List[str]
        cwd=None,  # type: Optional[str]
        extra_environ=None,  # type: Optional[Mapping[str, Any]]
    ):
        # type: (...) -> None
        with open_spinner(message) as spinner:
            call_subprocess(
                cmd,
                cwd=cwd,
                extra_environ=extra_environ,
                spinner=spinner,
            )

    return runner
