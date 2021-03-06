#!/usr/bin/env python
# Copyright (c) 2002-2008 ActiveState Software
# Author: Trent Mick (trentm@gmail.com)

import os
import sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
try:
    import go
finally:
    del sys.path[0]

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python :: 2
Topic :: Software Development :: Libraries :: Python Modules
"""

_top_dir = os.path.dirname(os.path.abspath(__file__))
README = open(os.path.join(_top_dir, 'README.rst')).read()
NEWS = open(os.path.join(_top_dir, 'NEWS.rst')).read()

setup(
    name="go",
    version=go.__version__,
    description='Quick directory changing (super-cd)',
    long_description=README + '\n\n' + NEWS,
    maintainer="Trent Mick",
    maintainer_email="trentm@gmail.com",
    url="http://code.google.com/p/go-tool/",
    license="http://www.opensource.org/licenses/mit-license.php",
    py_modules=["go"],
    package_dir={"": "lib"},
    entry_points={
        'console_scripts': [
            'go-setup=go:setup',
        ]
    },
    classifiers=filter(None, classifiers.split("\n")),
)

