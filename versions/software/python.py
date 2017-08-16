import sys

import versions.software.utils


def name():
    """Return the precise name for the software."""
    return 'Python'


def installed_version():
    """Return the currently installed version of Python, assuming it's what we're running now."""
    # We want the text rather than sys.version_info so we can compare with the web page
    return sys.version.split()[0]


def latest_version():
    """Return the latest version of Python available for download."""
    soup = versions.software.utils.get_soup('https://www.python.org/')
    if soup:
        text = soup.find(string='Latest: ')
        if text:
            return text.next_sibling.text.split()[-1]
    return 'Unknown'
