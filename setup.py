from setuptools import setup
from pyautomate import __version__


setup(
    name='pyautomate',
    version=__version__,
    description='PyAuto Core',
    author='Adam Jaso',
    packages=['pyauto'],
    package_dir={'pyautomate': 'pyautomate'},
    install_requires=['PyYAML', 'six'],
    url='https://github.com/adamjaso/pyautomate,
)
