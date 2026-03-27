"""
ASGI config for petstore project.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petstore.settings')
application = get_asgi_application()
