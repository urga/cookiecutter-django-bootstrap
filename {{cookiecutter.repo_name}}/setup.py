#!/usr/bin/env python
import subprocess
import version
from setuptools import setup, find_packages
from setuptools.command.install import install as _install


class install(_install):
    """
    This executes the original install method but adds install requirements that are defined in requirements.txt
    """
    def run(self):
        _install.run(self)
        subprocess.call(['pip', 'install', '-r', 'requirements.txt'])


setup(
    name='littleball',
    url="{{ cookiecutter.url }}",
    version=version.getVersion(),
    description="{{ cookiecutter.description }}",
    cmdclass={'install': install},
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts = ['manage.py'],
)