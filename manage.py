#!/usr/bin/env python

from argparse import ArgumentParser as AP

parser = AP(description="Perform django commands in a reusable app")
parser.add_argument("action", help="command (e.g. 'makemigrations', 'shell', 'test')")
args = parser.parse_args()

# https://stackoverflow.com/questions/30656162/migrations-in-stand-alone-django-app#answer-32379263
import sys
import django

from django.conf import settings
from django.core.management import call_command


settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'pdje',
    ),
)
#endsnippet

if args.action == "test":
    # 'test' action requires the default database configured
    # Use in-memory sqlite3
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    }

django.setup()
try:
    call_command(args.action, 'pdje')
except django.core.management.base.CommandError:
    call_command(args.action)
