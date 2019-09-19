#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

SUPPORTED_ENVS = ('test', 'sample')

SETTINGS_MODULES = {
    'sample': 'tests.sample_proj.settings'
}

ENV = os.environ.get('ENV', 'sample')
ENV = ENV.lower()

if ENV not in SUPPORTED_ENVS:
    raise Exception('Unsupported environment: %s' % ENV)


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULES[ENV])
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
