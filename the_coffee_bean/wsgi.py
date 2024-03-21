"""
WSGI config for boutique_ado project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static'))