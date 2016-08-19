#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import deaw

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(
    name='deaw',
    version=deaw.__version__,
    packages=find_packages(),
    author="Pawy (Patrick Borowy)",
    author_email="issues@pawy.pro",
    description="aioHTTP wrapped for easy and effective web programming",
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
    url='http://github.com/pawyp/deaw',

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications",
    ],
    install_requires=[
        "cryptography",
        "aiohttp",
        "aiohttp_debugtoolbar",
        "aiohttp_jinja2",
        "aiohttp_session[secure]",
        "cchardet",
        "cffi",
        "envparse",
        "ipython",
        "ipdb",
        "jinja2",
        "motor",
        "fernet",
    ],

    entry_points = {
        'console_scripts': [
            'deaw-admin.py = deaw.core:deawadmin',
        ],
    },

    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="WTFPL",

    # Il y a encore une chiée de paramètres possibles, mais avec ça vous
    # couvrez 90% des besoins

)


