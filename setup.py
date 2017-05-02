import os

from setuptools import setup

setup(
    name='covns',
    description='Reproducer for https://bitbucket.org/ned/coveragepy/issues/572',
    version='0.1',
    author='Christian Heimes',
    package_dir={'': 'src'},
    namespace_packages=[
        'covns',
    ],
    packages=[
        'covns.sub',
    ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
