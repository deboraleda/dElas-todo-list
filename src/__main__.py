
from urllib.parse import urlparse
import logging

from flask import Flask
from flask import request
from flask import jsonify

from . rest import app

logging = logging.getLogger(__name__)
bind_url = 'http://0.0.0.0:8000'
url = urlparse(bind_url)
host, port = url.hostname, url.port
logging.info(f"Iniciando servidor em: {url.geturl()}")
app.run(host=host, port=port, debug=True)