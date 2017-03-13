from wsgiref.simple_server import make_server
import os

def application(environ, start_response):
 start_response('200 OK', [('Content-Type','text/html')])
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