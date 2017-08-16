import re

import versions.software.utils


def name():
    """Return the precise name for the software."""
    return '7-Zip'


def installed_version():
    """Return the currently installed version of 7-Zip, or None if it isn't installed."""
    try:
        version_string = versions.software.utils.get_command_stdout('7z')
        return versions.software.utils.get_text_between(version_string, '] ', ' : ')
    except FileNotFoundError:
        pass


def latest_version():
    """Return the latest version of 7-Zip available for download."""
    soup = versions.software.utils.get_soup('http://www.7-zip.org/')
    if soup:
        tag = soup.find('b', string=re.compile('^Download'))
        if tag:
            return tag.text.split()[2]
    return 'Unknown'
