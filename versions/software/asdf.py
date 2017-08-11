import requests

TEXT_BEFORE_VERSION_NUMBER = 'This is ASDF '


def name():
    """Return the precise name for the software."""
    return 'asdf'


def installed_version():
    """Return the currently installed version of asdf."""
    # I don't have a command-line version to run to get this from
    return '3.2.1'


def download_asdf_release():
    """Return the contents of the latest release source for asdf.lisp."""
    response = requests.get('https://common-lisp.net/project/asdf/archives/asdf.lisp')
    response.raise_for_status()
    return response.text


def latest_version():
    """Return the latest version of asdf available for download."""
    source_code = download_asdf_release()
    if source_code:
        pos = source_code.find(TEXT_BEFORE_VERSION_NUMBER)
        if pos != -1:
            return source_code[pos + len(TEXT_BEFORE_VERSION_NUMBER):source_code.find(':', pos)]
