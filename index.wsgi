import sae
from mxonline import wsgi

application = sae.create_wsgi_app(wsgi.application)