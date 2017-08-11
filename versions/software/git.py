import subprocess

import bs4
import requests


def name():
    """Return the precise name for the software."""
    return 'git'


def installed_version():
    """Return the currently installed version of git."""
    try:
        # run 'git --version' and strip out the version number from stdout
        version_string = subprocess.check_output(('git', '--version')).decode('utf-8')
        if version_string.startswith('git version '):
            return version_string[len('git version '):].strip()
    except FileNotFoundError:
        pass


def windows_download_html():
    """Return the HTML of the git download web page."""
    response = requests.get('https://git-scm.com/download/win')
    response.raise_for_status()
    return response.text


def downloadable_version(filename):
    """Strip the version out of the git manual download link."""
    return filename.split('/')[-2][1:]


def latest_version():
    """Return the latest version of Windows git available for download."""
    response_html = windows_download_html()
    if response_html:
        download = bs4.BeautifulSoup(response_html, 'html.parser')
        tag = download.find('a', string='click here to download manually')
        if tag:
            return downloadable_version(tag.attrs['href'])
