import re

import versions.software.utils


def name():
    """Return the precise name for the software."""
    return 'WinMerge'


def installed_version():
    """Return the currently installed version of WinMerge."""
    # I don't know yet how to get the version programmatically
    return '2.14.0'


def latest_version():
    """Return the latest version of WinMerge available for download."""
    soup = versions.software.utils.get_soup('http://winmerge.org/?lang=en')
    if soup:
        tag = soup.find('h3', string=re.compile('latest stable version$'))
        if tag:
            return tag.text.split()[1]
    return 'Unknown'
