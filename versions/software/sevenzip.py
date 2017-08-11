import re
import subprocess

import bs4
import requests


def name():
    """Return the precise name for the software."""
    return '7-Zip'


def installed_version():
    """Return the currently installed version of 7-Zip."""
    try:
        version_string = subprocess.check_output('7z').decode('utf-8').strip()
        if version_string.startswith('7-Zip'):
            return version_string[version_string.find(']') + 1:version_string.find(':')].strip()
    except FileNotFoundError:
        pass


def download_html():
    """Return the HTML of the 7-Zip download web page."""
    response = requests.get('http://www.7-zip.org/')
    response.raise_for_status()
    return response.text


def downloadable_version(text):
    """Strip the version out of the 7-Zip download version text."""
    return text.split()[2]


def latest_version():
    """Return the latest version of 7-Zip available for download."""
    response_html = download_html()
    if response_html:
        download = bs4.BeautifulSoup(response_html, 'html.parser')
        tag = download.find('b', string=re.compile('^Download'))
        if tag:
            return downloadable_version(tag.text)
