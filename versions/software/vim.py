import subprocess

import bs4
import requests


def name():
    """Return the precise name for the software."""
    return 'vim'


def installed_version():
    """Return the currently installed version of vim."""
    try:
        version_string = subprocess.check_output(('vim', '--version')).decode('utf-8').strip()
        if version_string.startswith('VIM - Vi IMproved'):
            return version_string.split()[4]
    except FileNotFoundError:
        pass


def download_html():
    """Return the HTML of the vim download web page."""
    response = requests.get('http://www.vim.org/download.php')
    response.raise_for_status()
    return response.text


def downloadable_version(text):
    """Strip the version out of the vim version description text."""
    pos1 = text.find(' ') + 1
    pos2 = text.find(' ', pos1)
    return text[pos1:pos2]


def latest_version():
    """Return the latest version of vim available for download."""
    response_html = download_html()
    if response_html:
        download = bs4.BeautifulSoup(response_html, 'html.parser')
        version = download.find('h1', string='Version')
        if version:
            return downloadable_version(version.next_sibling)
