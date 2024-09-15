import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    # Bind to the port specified by the environment variable
    from django.core.management import execute_from_command_line

    port = os.environ.get("PORT", "8000")  # Default to 8000 if PORT is not set
    execute_from_command_line([sys.argv[0], "runserver", "0.0.0.0:" + port])