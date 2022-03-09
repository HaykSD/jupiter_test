from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'test'
LONG_DESCRIPTION = 'test'

# Setting up
setup(
    name="test_jupiter",
    version=VERSION,
    author="Hayk Sardaryan",
    author_email="<hayktest@gmail.com>",
    description=DESCRIPTION,
    url='https://github.com/HaykSD/jupiter_test/',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'requests'],
    keywords=['python', 'jupyter', 'test'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
