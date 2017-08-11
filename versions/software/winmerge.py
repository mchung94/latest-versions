import re

import bs4
import requests


def name():
    """Return the precise name for the software."""
    return 'WinMerge'


def installed_version():
    """Return the currently installed version of WinMerge."""
    # I don't know yet how to get the version programmatically
    return '2.14.0'


def download_html():
    """Return the HTML of the WinMerge download web page."""
    response = requests.get('http://winmerge.org/?lang=en')
    response.raise_for_status()
    return response.text


def downloadable_version(text):
    """Strip the version out of the WinMerge download version text."""
    return text.split()[1]


def latest_version():
    """Return the latest version of WinMerge available for download."""
    response_html = download_html()
    if response_html:
        download = bs4.BeautifulSoup(response_html, 'html.parser')
        tag = download.find('h3', string=re.compile('latest stable version$'))
        if tag:
            return downloadable_version(tag.text)
