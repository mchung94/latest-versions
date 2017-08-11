import sys

import bs4
import requests


def name():
    """Return the precise name for the software."""
    return 'Python'


def installed_version():
    """Return the currently installed version of Python, assuming it's what we're running now."""
    # We want the text rather than sys.version_info so we can compare with the web page
    return sys.version.split()[0]


def download_html():
    """Return the HTML of the Python web page."""
    response = requests.get('https://www.python.org/')
    response.raise_for_status()
    return response.text


def latest_version():
    """Return the latest version of Python available for download."""
    response_html = download_html()
    if response_html:
        download = bs4.BeautifulSoup(response_html, 'html.parser')
        text = download.find(string='Latest: ')
        if text:
            return text.next_sibling.text.split()[-1]
