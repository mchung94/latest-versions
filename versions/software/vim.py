from versions.software.utils import get_command_stdout, get_soup, \
    get_text_between


def name():
    """Return the precise name for the software."""
    return 'vim'


def installed_version():
    """Return the installed version of vim, or None if not installed."""
    try:
        version_string = get_command_stdout(('vim', '--version'))
        return version_string.split()[4]
    except FileNotFoundError:
        pass


def latest_version():
    """Return the latest version of vim available for download."""
    soup = get_soup('http://www.vim.org/download.php')
    if soup:
        tag = soup.find('h1', string='Version')
        if tag:
            return get_text_between(tag.next_sibling, ' ', ' ')
    return 'Unknown'
