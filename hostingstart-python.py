import sys
import os
import platform

var = 3

def application(environ, start_response):

    start_response(b'200 OK', [(b'Content-Type', b'text/html')])
    os.system('python app.py')
    #if(var == 3):
        #with open ("hostingstart-python.html", "r") as hostingstart_file:
        #with open ("app.py", "r") as hostingstart_file:
            #hosting = hostingstart_file.read()
    
        
        #yield hosting.encode('utf8').replace(b'PYTHON_VERSION', platform.python_version().encode('utf8'))


