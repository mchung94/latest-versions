import re

from versions.software.utils import get_command_stderr, get_soup, \
    get_text_between


def name():
    """Return the precise name for the software."""
    return 'Zulu OpenJDK'


def installed_version():
    """Return the installed version of the jdk, or None if not installed."""
    try:
        version_string = get_command_stderr(('java', '-version'))
        return get_text_between(version_string, '"', '"')
    except FileNotFoundError:
        pass


def downloadable_version(url):
    """Strip the version out of the Zulu OpenJDK manual download link."""
    # example: http://cdn.azul.com/.../zulu8.23.0.3-jdk8.0.144-win_x64.zip
    filename = url[url.rfind('/') + 1:]
    jdk_version = get_text_between(filename, '-jdk', '-')
    version, update = jdk_version.rsplit('.', 1)
    return f'1.{version}_{update}'


def latest_version():
    """Return the latest version of Zulu OpenJDK available for download."""
    soup = get_soup('http://www.azul.com/downloads/zulu/zulu-windows/')
    if soup:
        div = soup.find('div', class_='latest_area')
        if div:
            zip_filename = re.compile('\.zip$')
            tag = div.find('a', class_='r-download', href=zip_filename)
            if tag:
                return downloadable_version(tag.attrs['href'])
    return 'Unknown'
