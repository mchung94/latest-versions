import json
import os
from os.path import expandvars, normpath

from versions.software.utils import get_command_stderr, get_response, \
    get_text_between


def name():
    """Return the precise name for the software."""
    return 'AdoptOpenJDK'


def installed_version():
    """Return the installed version of the JDK, or None if not installed."""
    try:
        java_path = 'java'
        if 'JAVA_HOME' in os.environ:
            java_path = normpath(expandvars('$JAVA_HOME/bin/java'))
        version_string = get_command_stderr((java_path, '-version'))
        return get_text_between(version_string, '(build ', ')')
    except FileNotFoundError:
        return None


def latest_release(major_version_number):
    """Return the release_name of the latest release of the given JDK."""
    base_url = 'https://api.adoptopenjdk.net/v2/info/releases'
    version = f'openjdk{major_version_number}'
    params = 'openjdk_impl=hotspot'
    url = f'{base_url}/{version}?{params}'
    return json.loads(get_response(url).text)[-1]['release_name']


def adjust_release_version(release_name):
    """
    Adjust release_name to match the build version from the executable.

    executable: 1.8.0_212-b04          release_name: jdk8u212-b04
    executable: 11.0.3+7               release_name: jdk-11.0.3+7
    executable: 12.0.1+12              release_name: jdk-12.0.1+12
    """
    if release_name.startswith('jdk8u'):
        return release_name.replace('jdk8u', '1.8.0_')
    else:
        return release_name[4:]


def latest_version():
    """Return the latest version of AdoptOpenJDK available for download."""
    build_version = installed_version()
    if build_version:
        parts = build_version.split('.')
        major_version_number = int(parts[1] if parts[0] == '1' else parts[0])
        return adjust_release_version(latest_release(major_version_number))
    return 'Unknown'
