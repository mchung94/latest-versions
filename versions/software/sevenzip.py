import re

from versions.software.utils import get_command_stdout, get_soup, \
    get_text_between


def name():
    """Return the precise name for the software."""
    return '7-Zip'


def installed_version():
    """Return the installed version of 7-Zip, or None if not installed."""
    try:
        version_string = get_command_stdout('7z')
        version = get_text_between(version_string, '] ', ' : ')
        if version.startswith('<archive_name>'):
            version = get_text_between(version_string, '7-Zip ', ' ')
        return version
    except FileNotFoundError:
        pass


def latest_version():
    """Return the latest version of 7-Zip available for download."""
    soup = get_soup('http://www.7-zip.org/')
    if soup:
        tag = soup.find('b', string=re.compile('^Download'))
        if tag:
            return tag.text.split()[2]
    return 'Unknown'
