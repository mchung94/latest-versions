import re

from versions.software.utils import get_command_stderr, get_soup, \
    get_text_between


def name():
    """Return the precise name for the software."""
    return 'Zulu OpenJDK'


def installed_version():
    """Return the installed version of the JDK, or None if not installed."""
    try:
        version_string = get_command_stderr(('java', '-version'))
        # Examples: 1.6.0-107, 1.7.0_181, 1.8.0_172, 9.0.7.1, 10, 10.0.1
        return get_text_between(version_string, '"', '"')
    except FileNotFoundError:
        pass


def jdk_version():
    """Return the installed JDK main version string: 1.6, 1.7, 1.8, 9, 10..."""
    installed = installed_version()
    if installed is None:
        return None
    elif re.search('^1\.[678]', installed):
        return installed[:3]
    return installed.split('.')[0]


def url_version(url):
    """Given a Zulu download URL, return the JDK version."""
    jdk = get_text_between(url, 'jdk', '-')
    if jdk[0] == '6':
        version, update = jdk.rsplit('.', 1)
        return f'1.{version}-{update}'
    elif jdk[0] in ('7', '8'):
        version, update = jdk.rsplit('.', 1)
        return f'1.{version}_{update}'
    elif jdk[0] == '9':
        return get_text_between(url, 'bin/zulu', '-')
    else:
        return jdk


def latest_version():
    """Return the latest version of Zulu OpenJDK available for download."""
    soup = get_soup('http://www.azul.com/downloads/zulu/zulu-windows/')
    if soup:
        file_re = re.compile('x64\.zip$')
        matches = soup.find_all('a', class_='r-download', href=file_re)
        files = [tag.attrs['href'] for tag in matches]
        if files:
            version_names = [url_version(url) for url in files]
            version = jdk_version()
            if version is None:
                return version_names[0]
            else:
                for v in version_names:
                    if v.startswith(version):
                        return v
    return 'Unknown'
