#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
call(["manage.py", "syncdb"])