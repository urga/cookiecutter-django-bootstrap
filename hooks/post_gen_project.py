#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
call(["pip", "install", "-r", "requirements/local.txt"])
# call(["createuser", "{{ cookiecutter.repo_name }}"])
call (["git", "init"])
# call(["manage.py", "syncdb"])