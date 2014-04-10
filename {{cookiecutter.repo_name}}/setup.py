#!/usr/bin/env python
import subprocess
import versioneer
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

versioneer.versionfile_source = '{{ cookiecutter.repo_name }}/_version.py'
versioneer.versionfile_build = '{{ cookiecutter.repo_name }}/_version.py'
versioneer.tag_prefix = 'v' # tags are like 1.2.0
versioneer.parentdir_prefix = '{{ cookiecutter.repo_name }}-' # dirname like 'myproject-1.2.0'


class install(_install):
    """
    This executes the original install method but adds install requirements that are defined in requirements.txt
    """
    def run(self):
        _install.run(self)
        subprocess.call(['pip', 'install', '-r', 'requirements.txt'])


cmdclass = versioneer.get_cmdclass()
cmdclass.update({'install': install})


setup(
    name='littleball',
    url="{{ cookiecutter.url }}",
    version=versioneer.get_version(),
    description="{{ cookiecutter.description }}",
    cmdclass=cmdclass,
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts = ['manage.py'],
)