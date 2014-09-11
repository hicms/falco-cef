# To generate a zip file: python setup.py bdist_esky
# To generate patche files: python setup.py bdist_esky_patch

import distutils.command
import sys
import os
from distutils.sysconfig import get_python_lib
# from esky.bdist_esky import Executable
# from setuptools import setup, Command
# from setuptools import setup
from cx_Freeze import setup, Executable
import py2exe
"""
A custom setuptools command to invoke sphinx-apidoc script
"""

# I just did a "pip freeze" to collect these
requirements = [
    "Twisted<14.0.0",
    "esky==0.9.8",
    "ipython==2.2.0",
    "pyreadline==2.0",
    "zope.interface==4.1.1",
]

if sys.platform in ["win32"]:

    setup(
        name = "Falco",
        executables = [Executable("wxpython.py", base="Win32GUI")],
        # optimize = 1,
        # compressed = 0,
        # bundle_files = 3,
        # "zipfile": None, # The zipfile will by packaged into the exe instead.
        # "packages": ["werkzeug", "email"],
        # packages = ["wx"],
        # "includes": ["sip"],
        includes = ["json", "wx"],        
        )
    setup(
        name = "Falco",
        windows = ["wxpython.py"],
        optimize = 1,
        compressed = 0,
        bundle_files = 3,
        # "zipfile": None, # The zipfile will by packaged into the exe instead.
        # "packages": ["werkzeug", "email"],
        # packages = ["wx"],
        # "includes": ["sip"],
        includes = ["json", "wx"],
    )
    exit(0)
    setup(
        name = "falco-cef",
        version = "0.0.1",
        author = "Team Smash at FiveStars",
        author_email = "smash@fivestars.com",
        license = "Restrictive",
        description = "The CEF FiveStars POS client",
        setup_requires=[
        ] + requirements,
        install_requires=requirements,
        # packages =  ["starfox"], # For flake8, not used in bdist_esky
        scripts = [
            Executable(
                "wxpython.py",
                name = "Falco",
                gui_only = True,
            ),
        ],
        # data_files = [(".", ("dll/gdiplus.dll",))],
        data_files = [
            (".", [os.path.join(get_python_lib(), 'cefpython3', name) for name in (
                "Microsoft.VC90.CRT.manifest",
                "msvcm90.dll",
                "msvcp90.dll",
                "msvcr90.dll"
            )]),
        ],
        options = {
            "nosetests": {
                "match": "(?:^|[b_.-])(([Tt]est)|([Ss]hould))"
            },
            "build_sphinx": {
                "source_dir": "doc/apidoc.auto",
                "build_dir": "doc",
                "config_dir": "doc",
            },
            "bdist_esky": {

                # Move the esky dist dir beneath build
                "dist_dir": "build/bdist_esky",

                # Necessary for subsequent patching
                "enable_appdata_dir": True,

                # Force esky to freeze the app using py2exe
                "freezer_module": "py2exe",

                # py2exe options
                "freezer_options": {
                    "optimize": 0,
                    "compressed": 1,
                    # "bundle_files": 3,
                    # "zipfile": None, # The zipfile will by packaged into the exe instead.
                    # "packages": ["werkzeug", "email"],
                    "packages": ["wx"],
                    # "includes": ["sip"],
                    "includes": ["json", "wx"],
                    "excludes": [
                        # "IPython", "IPython.Shell", "IPython.frontend.terminal.embed",
                        # "Tkconstants", "Tkinter",
                        # "cherrypy",
                        # "jinja2.debug",
                        # "pydoc",
                        # "test.test_support",
                        # "twisted.test",
                        # "unittest",
                        # "wx", "wxPython", "wxversion"
                    ],
                    "dll_excludes": [
                        # "OLEAUT32.dll", "USER32.dll", "MPR.dll", "SHELL32.dll", "KERNEL32.dll", "COMDLG32.dll",
                        # "WSOCK32.dll", "COMCTL32.dll", "ADVAPI32.dll", "NETAPI32.dll", "WS2_32.dll", "MSVCP71.dll",
                        # "VERSION.dll", "ole32.dll", "MSWSOCK.dll", "GDI32.dll"
                    ],
                    "ignores": [
                        # "DLFCN",
                        # "PySide.QtCore",
                        # "__pypy__",
                        # "blinker",
                        # "dl",
                        # "cmemcache", "cmemcached",
                        # "django.utils",
                        # "email.Charset", "email.Encoders", "email.Errors", "email.Generator", "email.Header", "email.Iterators", "email.MIMEAudio", "email.MIMEBase", "email.MIMEImage", "email.MIMEMessage", "email.MIMEMultipart", "email.MIMEText", "email.Message", "email.Parser", "email.Utils", "email.base64MIME", "email.quopriMIME",
                        # "genshi.template", "genshi.template.loader",
                        # "google.appengine.api",
                        # "greenlet",
                        # "io",
                        # "jinja2._markupsafe._speedups",
                        # "json",
                        # "logging._checkLevel",
                        # "lxml", "lxml.html",
                        # "memcache",
                        # "pkg_resources",
                        # "pyinotify",
                        # "pylibmc",
                        # "redis",
                        # "resource",
                        # "twisted.internet._sigchld",
                        # "tcl",
                        # "unittest.case", "unittest.runner",
                        # "werkzeug.Client", "werkzeug.EnvironBuilder", "werkzeug.Headers", "werkzeug.ImmutableDict", "werkzeug.LocalProxy", "werkzeug.LocalStack", "werkzeug.Request", "werkzeug.Response", "werkzeug.abort", "werkzeug.cached_property", "werkzeug.create_environ", "werkzeug.import_string", "werkzeug.redirect", "werkzeug.run_simple", "werkzeug.wrap_file"
                    ],
                },
            },
        },
    )
