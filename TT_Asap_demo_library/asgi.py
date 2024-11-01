import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "TT_Asap_demo_library.settings"
)

application = get_asgi_application()
