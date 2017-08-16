import versions.software.utils


def name():
    """Return the precise name for the software."""
    return 'asdf'


def installed_version():
    """Return the currently installed version of asdf."""
    # I don't have a command-line version to run to get this from
    return '3.2.1'


def latest_version():
    """Return the latest version of asdf available for download."""
    url = 'https://common-lisp.net/project/asdf/archives/asdf.lisp'
    source_code = versions.software.utils.get_response(url).text
    return versions.software.utils.get_text_between(source_code, 'This is ASDF ', ':')
