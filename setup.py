# Copyright (c) 2010 Guilherme Gondim and contributors
#
# This file is part of Django Admin Help.
#
# Django Admin Help is free software under terms of the GNU Lesser
# General Public License version 3 (LGPLv3) as published by the Free
# Software Foundation. See the file README for copying conditions.

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from adminhelp import get_version

setup(
    name = 'django-adminhelp',
    version = get_version(),
    description = 'A help application for Django administration.',
    long_description = ('Django Admin Help is a pluggable help system for '
                        'Django Web Framework to be used with administration '
                        'application.\n\n'
                        'Admin Help was inspired by help system of Django '
                        'Grappelli.'),
    keywords = 'django apps admin help',
    author = 'Guilherme Gondim',
    author_email = 'semente@taurinus.org',
    url = 'http://github.com/semente/django-adminhelp',
    download_url = 'http://github.com/semente/django-adminhelp/downloads',
    license = 'GNU Lesser General Public License (LGPL), Version 3',
    classifiers = [
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
