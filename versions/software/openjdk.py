import re

import versions.software.utils


def name():
    """Return the precise name for the software."""
    return 'Zulu OpenJDK'


def installed_version():
    """Return the currently installed version of the jdk, or None if it isn't installed."""
    try:
        version_string = versions.software.utils.get_command_stderr(('java', '-version'))
        return versions.software.utils.get_text_between(version_string, '"', '"')
    except FileNotFoundError:
        pass


def downloadable_version(url):
    """Strip the version out of the Zulu OpenJDK manual download link."""
    # example: http://cdn.azul.com/zulu/bin/zulu8.23.0.3-jdk8.0.144-win_x64.zip
    filename = url[url.rfind('/') + 1:]
    jdk_version = versions.software.utils.get_text_between(filename, '-jdk', '-')
    version, update = jdk_version.rsplit('.', 1)
    return f'1.{version}_{update}'


def latest_version():
    """Return the latest version of Zulu OpenJDK available for download."""
    soup = versions.software.utils.get_soup('http://www.azul.com/downloads/zulu/zulu-windows/')
    if soup:
        tag = soup.find('div', class_='latest_area').find('a', class_='r-download', href=re.compile('\.zip$'))
        if tag:
            return downloadable_version(tag.attrs['href'])
    return 'Unknown'
