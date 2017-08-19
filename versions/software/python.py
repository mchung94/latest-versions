import sys

from versions.software.utils import get_soup


def name():
    """Return the precise name for the software."""
    return 'Python'


def installed_version():
    """Return the installed version of Python we're running now."""
    # Use the text rather than sys.version_info to compare with the web page
    return sys.version.split()[0]


def latest_version():
    """Return the latest version of Python available for download."""
    soup = get_soup('https://www.python.org/')
    if soup:
        text = soup.find(string='Latest: ')
        if text:
            return text.next_sibling.text.split()[-1]
    return 'Unknown'
