import os
def application(environ, start_response):
 start_response('200 OK', [('Content-Type','text/html')])
 #os.system('git add .')
 #os.system('git commit -m "merge"')
 #os.system('git pull origin master')
 print "success"
 return ['My own hello webhook']
