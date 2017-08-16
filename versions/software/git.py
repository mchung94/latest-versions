import versions.software.utils


def name():
    """Return the precise name for the software."""
    return 'git'


def installed_version():
    """Return the currently installed version of git, or None if it isn't installed."""
    try:
        return versions.software.utils.get_command_stdout(['git', '--version']).split()[-1]
    except FileNotFoundError:
        pass


def downloadable_version(url):
    """Strip the version out of the git manual download url."""
    # example: https://github.com/git-for-windows/git/releases/download/v2.14.1.windows.1/Git-2.14.1-64-bit.exe
    return url.split('/')[-2][1:]


def latest_version():
    """Return the latest version of Windows git available for download."""
    soup = versions.software.utils.get_soup('https://git-scm.com/download/win')
    if soup:
        tag = soup.find('a', string='click here to download manually')
        if tag:
            return downloadable_version(tag.attrs['href'])
    return 'Unknown'
