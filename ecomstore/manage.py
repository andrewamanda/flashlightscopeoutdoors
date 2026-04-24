#!/usr/bin/env python

if __name__ == "__main__":
    #execute_manager(settings)

    import os
    import sys
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomstore.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
