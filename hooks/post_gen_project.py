#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
call(["mv", "dotgitignore", ".gitignore"])
call(["pip", "install", "-r", "requirements/local.txt"])
call(["fab", "create_db"])
call(["./manage.py", "syncdb", "--noinput"])
call(["npm", "install"])
call(["bower", "install"])
call(["grunt"])
call(["git", "init"])
call(["git", "add", "-A"])
call(["git", "commit", "-m", "'Initial commit'"])