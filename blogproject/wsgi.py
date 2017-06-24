#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
WSGI config for blogproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogproject.settings")
sys.path.append('/usr/lib/python2.7/site-packages')
sys.path.append('/usr/lib64/python2.7/site-packages')

application = get_wsgi_application()
