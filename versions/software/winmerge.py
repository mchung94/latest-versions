import re

from versions.software.utils import get_soup


def name():
    """Return the precise name for the software."""
    return 'WinMerge'


def installed_version():
    """Return the installed version of WinMerge."""
    # I don't know yet how to get the version programmatically
    # there isn't a command line option to print the version
    return '2.16.2'


def latest_version():
    """Return the latest version of WinMerge available for download."""
    soup = get_soup('http://winmerge.org/?lang=en')
    if soup:
        ends_with_latest_stable_version = re.compile('latest stable version$')
        tag = soup.find('h3', string=ends_with_latest_stable_version)
        if tag:
            return tag.text.split()[1]
    return 'Unknown'
