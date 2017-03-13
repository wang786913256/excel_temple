from wsgiref.simple_server import make_server
from webhook import application
httpd = make_server("localhost", 5500, application)
httpd.serve_forever()