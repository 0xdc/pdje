#!/usr/bin/env python
# https://stackoverflow.com/questions/30656162/migrations-in-stand-alone-django-app#answer-32379263
import sys
import django

from django.conf import settings
from django.core.management import call_command

settings.configure(DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'pdje',
    ),
)

django.setup()
call_command('makemigrations', 'pdje')