'''
Install script for this module.
'''

import setuptools

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

with open('LICENSE', 'r') as f:
    LICENCE_TEXT = f.read()

import example_python.__about__ as about

setuptools.setup(
    name=about.__title__,
    version=about.__version__,
    author=about.__author__,
    author_email=about.__author_email__,
    description=about.__description__,
    url=about.__url__,

    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license=LICENCE_TEXT,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT :: ',
        'Operating System :: Tested on MacOS only',
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9',

    entry_points={
        'console_scripts': ['example_python=example_python.console:main'],
    }
)
