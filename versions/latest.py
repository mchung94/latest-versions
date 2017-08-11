import collections
import pkgutil

import versions.software


VersionInfo = collections.namedtuple('VersionInfo', ['name', 'installed_version', 'latest_version'])


def get_version_info(module_info):
    module_finder, name, _ = module_info
    m = module_finder.find_module(name).load_module(name)
    return VersionInfo(m.name(), m.installed_version(), m.latest_version())


def all_versions():
    return [get_version_info(m) for m in pkgutil.iter_modules(versions.software.__path__) if not m.ispkg]


def main():
    for version_info in all_versions():
        print(version_info)


if __name__ == '__main__':
    main()
