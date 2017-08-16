import versions.software.utils


def name():
    """Return the precise name for the software."""
    return 'vim'


def installed_version():
    """Return the currently installed version of vim, or None if it isn't installed."""
    try:
        version_string = versions.software.utils.get_command_stdout(('vim', '--version'))
        return version_string.split()[4]
    except FileNotFoundError:
        pass


def latest_version():
    """Return the latest version of vim available for download."""
    soup = versions.software.utils.get_soup('http://www.vim.org/download.php')
    if soup:
        tag = soup.find('h1', string='Version')
        if tag:
            return versions.software.utils.get_text_between(tag.next_sibling, ' ', ' ')
    return 'Unknown'
