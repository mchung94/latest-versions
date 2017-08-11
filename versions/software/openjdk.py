import re
import subprocess

import requests
import bs4


def name():
    """Return the precise name for the software."""
    return 'Zulu OpenJDK'


def installed_version():
    """Return the currently installed version of the jdk."""
    try:
        version_string = subprocess.check_output(('java', '-version'), stderr=subprocess.STDOUT).decode('utf-8')
        if version_string.startswith('openjdk version'):
            pos = version_string.find('"') + 1
            return version_string[pos:version_string.find('"', pos)]
    except FileNotFoundError:
        pass


def windows_download_html():
    """Return the HTML of the Zulu OpenJDK download web page."""
    response = requests.get('http://www.azul.com/downloads/zulu/zulu-windows/')
    response.raise_for_status()
    return response.text


def downloadable_version(href):
    """Strip the version out of the Zulu OpenJDK manual download link."""
    filename = href[href.rfind('/') + 1:]
    # find the part of the filename in between the first and last hyphen
    jdk_name = filename[filename.find('-') + 1:filename.rfind('-')]
    jdk_version = jdk_name.replace('jdk', '1.')
    last_period = jdk_version.rfind('.')
    return jdk_version[:last_period] + '_' + jdk_version[last_period + 1:]


def latest_version():
    """Return the latest version of Zulu OpenJDK available for download."""
    response_html = windows_download_html()
    if response_html:
        download = bs4.BeautifulSoup(response_html, 'html.parser')
        tag = download.find('div', class_='latest_area').find('a', class_='r-download', href=re.compile('\.zip$'))
        if tag:
            return downloadable_version(tag.attrs['href'])
