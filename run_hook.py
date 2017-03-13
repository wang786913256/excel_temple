from wsgiref.simple_server import make_server
import os
import json
from cgi import parse_qs, escape

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    if request_body:
        print type(request_body)
        print [request_body]
        request_body = json.loads(request_body)
        ref = request_body.get("ref")
        print ref
        # d = parse_qs(request_body)
        # print d
        #os.system('git add .')
        #os.system('git commit -m "merge"')
        #os.system('git pull origin master')
        os.system('git pull')
        print "success"
    return ['My own hello webhook']

if __name__ == "__main__":
    httpd = make_server("localhost", 5500, application)
    # httpd.serve_forever()
    httpd.handle_request()
