import os
from setuptools import setup

try:
    from landb import __version__ as landb_version
except ImportError:
    landb_version = "UNKOWN"


def read(fname):
    """Open a filename and return the contents as a string.

    :param fname: Filename (relative to this file) to read
    :type fname: str

    :returns: str -- file contents

    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='LANDB',
    version=landb_version,
    url='https://github.com/cernops/landb',
    license='GPLv3',
    author='Joe Harrison',
    author_email='joe.harrison@cern.ch',
    description='A Python library designed to interface with CERN\'s LANDB '
    'network information system',
    long_description=read('README.md'),
    packages=['landb'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Database :: Front-Ends'
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
