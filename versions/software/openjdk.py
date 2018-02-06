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
        # "1.8.0_162" or "9.0.4.1" for example
        return get_text_between(version_string, '"', '"')
    except FileNotFoundError:
        pass


def latest_version():
    """Return the latest version of Zulu OpenJDK available for download."""
    installed = installed_version()
    soup = get_soup('http://www.azul.com/downloads/zulu/zulu-windows/')
    if soup:
        zip_filename = re.compile('\.zip$')
        for tag in soup.find_all('a', class_='r-download', href=zip_filename):
            filename = tag.attrs['href']
            zulu = get_text_between(filename, 'bin/zulu', '-')
            jdk = get_text_between(filename, 'jdk', '-')
            if (installed is None) or (installed[0] == '9' and zulu[0] == '9'):
                return zulu
            elif installed[0] == '1' and jdk[0] == installed[2]:
                version, update = jdk.rsplit('.', 1)
                return f'1.{version}_{update}'
    return 'Unknown'
