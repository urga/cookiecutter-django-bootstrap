#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call

call(["mv", "dotgitignore", ".gitignore"])
print("******* Installling node modules:")
call(["npm", "install"])
print("******* Node modules installed.")
print("******* Installing python dependancies:")
call(["pip", "install", "-r", "requirements/local.txt"])
print("******* Python depedancies installed.")
call(["./manage.py", "bower", "install"])
