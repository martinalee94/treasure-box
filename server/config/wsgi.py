import os
from pathlib import Path

import environ
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.config.settings.prod")
environ.Env.read_env(
    env_file=os.path.join(Path(__file__).resolve().parent.parent, ".env.heroku")
)
application = get_wsgi_application()
