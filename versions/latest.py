import pkgutil

import versions.software


def all_modules(package_path):
    """"Return a list of all modules in the given package path."""

    def load_module(module_info):
        """Load and return the module referred to by the given ModuleInfo."""
        return module_info.module_finder.find_module(module_info.name).load_module(module_info.name)

    return [load_module(m_info) for m_info in pkgutil.iter_modules(package_path) if not m_info.ispkg]


def is_software_module(m):
    """Return True if the given module m has name(), installed_version(), and latest_version() defined."""

    def has_callable(name):
        """Return True if the module m has a callable by the given name."""
        try:
            attr = getattr(m, name)
            return callable(attr)
        except AttributeError:
            return False

    def has_callables(*args):
        """Return True if all the args are names of functions defined in module m."""
        return all([has_callable(attr) for attr in args])

    return has_callables('name', 'installed_version', 'latest_version')


def print_version_results(software_module):
    """Print a human-readable report on the software's name/current/latest version."""
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
    if (installed_version is not None) and (installed_version != latest_version):
        if installed_version == 'Unknown' or latest_version == 'Unknown':
            print('    Check manually if an upgrade is available.')
        else:
            print('    An upgrade is available.')


def main():
    for m in all_modules(versions.software.__path__):
        if is_software_module(m):
            print_version_results(m)


if __name__ == '__main__':
    main()
