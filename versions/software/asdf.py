from versions.software.utils import get_response, get_text_between


def name():
    """Return the precise name for the software."""
    return 'asdf'


def installed_version():
    """Return the installed version of asdf."""
    # I don't have a command-line version to run to get this from
    return '3.3.1'


def latest_version():
    """Return the latest version of asdf available for download."""
    url = 'https://common-lisp.net/project/asdf/archives/asdf.lisp'
    source_code = get_response(url).text
    return get_text_between(source_code, 'This is ASDF ', ':')
