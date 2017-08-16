# latest-versions
latest-versions checks if there's an upgrade available for installed software.

This is just a simple tool I made to check if I need to update some software on
my computer.  For each program I want to check, first it runs some code to
figure out which version I have installed, then it goes to the software's web
page and scrapes the latest version available for download.
  
Then it prints its results out onto the console.

# Usage
I used Python 3.6.2 on Windows 10 while writing this program.
1. Clone this project and go into the directory where it resides.
2. Create and activate a virtualenv if you want, and run
   `python -m pip install -r requirements.txt`
   - It just wants to install requests (HTTP library) and beautifulsoup4
     (HTML parsing).
3. Run `python -m versions.latest`

An example of the results:
```
Software: asdf
    Installed Version : 3.2.1
    Latest Version    : 3.2.1
Software: git
    Installed Version : 2.14.0.windows.1
    Latest Version    : 2.14.1.windows.1
    An upgrade is available.
Software: Zulu OpenJDK
    Installed Version : 1.8.0_144
    Latest Version    : 1.8.0_144
Software: Python
    Installed Version : 3.6.2
    Latest Version    : 3.6.2
Software: 7-Zip
    Installed Version : 16.04
    Latest Version    : 16.04
Software: vim
    Installed Version : 8.0
    Latest Version    : 8.0
Software: WinMerge
    Installed Version : 2.14.0
    Latest Version    : 2.14.0
```

# Programming Guide
The [versions.software](versions/software) package contains one module for
each program you're interested in, plus a
[utils.py](versions/software/utils.py) for common utility functions.

Each module implements three functions that all return strings:
1. `name()`
   - Return the name of the software.
   - This is only used when printing out the version report.
2. `installed_version()`
   - Figure out what version you have installed locally and return it.
   - Usually, I use the `subprocess` module to run the program and then strip
     out the version string from whatever it prints out.
   - Sometimes there's no easy way to programmatically determine the version
     so I just hardcode the version I know I have.  It doesn't really matter
     since the important piece is finding out what the latest version is.
3. `latest_version()`
   - Figure out what the latest version of the software is and return it.
   - Usually I use the Requests library to grab the info from the web page,
     then use the Beautiful Soup library to scrape the version out of the
     HTML.

[versions/latest.py](versions/latest.py) uses the `pkgutil` module to load
each module in the [versions.software](versions/software) package and then
determine which modules implement all three functions above.  For those
modules, it then runs each of the three functions and prints out a report.

If you want to add support for another software package, create a new python
file inside the [versions.software](versions/software) package and implement
the three functions. It should automatically get picked up next time you run
[versions/latest.py](versions/latest.py).
