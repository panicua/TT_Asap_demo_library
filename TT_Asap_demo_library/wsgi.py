import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "TT_Asap_demo_library.settings"
)

application = get_wsgi_application()
