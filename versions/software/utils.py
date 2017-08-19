import subprocess

import bs4
import requests


class VersionParsingError(Exception):
    """Raise when unable to strip the version number from some text."""


def get_text_between(text, before_text, after_text):
    """Return the substring of text between before_text and after_text."""
    pos1 = text.find(before_text)
    if pos1 != -1:
        pos1 += len(before_text)
        pos2 = text.find(after_text, pos1)
        if pos2 != -1:
            return text[pos1:pos2].strip()
        else:
            error_message = f"Can't find '{after_text}' within a longer text."
            raise VersionParsingError(error_message)
    else:
        error_message = f"Can't find '{before_text}' within a longer text."
        raise VersionParsingError(error_message)


def get_response(url):
    """Return the response from the URL, raising exception on error status."""
    response = requests.get(url)
    response.raise_for_status()
    return response


def get_soup(url):
    """Return a BeautifulSoup object for the given URL."""
    return bs4.BeautifulSoup(get_response(url).text, 'html.parser')


def _run_command(args):
    """Run a command, capturing stdout and stderr."""
    return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def get_command_stdout(command_args, encoding='utf-8'):
    """Run a command and return its stdout as a string."""
    return _run_command(command_args).stdout.decode(encoding)


def get_command_stderr(command_args, encoding='utf-8'):
    """Run a command return its stderr as a string."""
    return _run_command(command_args).stderr.decode(encoding)
