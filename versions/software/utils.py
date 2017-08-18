import subprocess

import bs4
import requests


class VersionParsingError(Exception):
    """Raise when unable to strip out a version number from some longer text."""


def get_text_between(text, before_text, after_text):
    """Return the string from text that is in between before_text and after_text, without whitespace."""
    pos1 = text.find(before_text)
    if pos1 != -1:
        pos1 += len(before_text)
        pos2 = text.find(after_text, pos1)
        if pos2 != -1:
            return text[pos1:pos2].strip()
        else:
            raise VersionParsingError(f"Unable to find '{after_text}' within a longer text.")
    else:
        raise VersionParsingError(f"Unable to find '{before_text}' within a longer text.")


def get_response(url):
    """Return the response from the given URL, raising an exception if there's an error."""
    response = requests.get(url)
    response.raise_for_status()
    return response


def get_soup(url):
    """Return a BeautifulSoup object for the given URL."""
    return bs4.BeautifulSoup(get_response(url).text, 'html.parser')


def get_command_stdout(command_args, encoding='utf-8'):
    """Run the command described by command_args (as in subprocess.run() args) and return its stdout as a string."""
    return subprocess.run(command_args, stdout=subprocess.PIPE).stdout.decode(encoding)


def get_command_stderr(command_args, encoding='utf-8'):
    """Run the command described by command_args (as in subprocess.run() args) and return its stderr as a string."""
    return subprocess.run(command_args, stderr=subprocess.PIPE).stderr.decode(encoding)

