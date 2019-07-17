import pkgutil

import versions.software


def all_modules(package_path):
    """"Return a generator of all modules in the given package path."""

    def load_module(module_info):
        """Load and return the module referred to by the given ModuleInfo."""
        name = module_info.name
        return module_info.module_finder.find_module(name).load_module(name)

    modules = pkgutil.iter_modules(package_path)
    return (load_module(m_info) for m_info in modules if not m_info.ispkg)


def is_software_module(m):
    """Return True if module m is a software version checking module."""

    def has_callable(name):
        """Return True if the module m has a callable by the given name."""
        try:
            attr = getattr(m, name)
            return callable(attr)
        except AttributeError:
            return False

    def has_callables(*args):
        """Return True if all args are names of functions in module m."""
        return all([has_callable(attr) for attr in args])

    return has_callables('name', 'installed_version', 'latest_version')


def print_version_results(software_module):
    """Print a report on the software's name/current/latest version."""
    name = software_module.name()
    # noinspection PyBroadException
    try:
        installed_version = software_module.installed_version()
    except Exception:
        installed_version = 'Unknown'
    # noinspection PyBroadException
    try:
        latest_version = software_module.latest_version()
    except Exception:
        latest_version = 'Unknown'
    print('Software: %s' % name)
    print('    Installed Version : %s' % installed_version)
    print('    Latest Version    : %s' % latest_version)
    if installed_version is not None:
        if installed_version == 'Unknown' or latest_version == 'Unknown':
            print('    Check manually if an upgrade is available or needed.')
        elif installed_version != latest_version:
            print('    An upgrade is available.')


def main(*args):
    """
    Print a report of each software module's installed and latest versions.

    args can be optional strings naming modules that should be checked,
    for example 'asdf' or 'vim'. These are the names of the modules in
    the versions.software package.
    """
    for m in all_modules(versions.software.__path__):
        if is_software_module(m):
            if not args or m.__name__ in args:
                print_version_results(m)


if __name__ == '__main__':
    # Example of checking a subset: main('openjdk', 'vim')
    main()
