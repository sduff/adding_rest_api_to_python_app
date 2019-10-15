#!/usr/local/bin/python

import BaseHTTPServer

addy = ('',1024)

# A global data structure for access between HTTP server and main code
class Config(object):
    httpd_running = False
config = Config()

# define the http handler
class httpd_handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print("In GET Handler for ",self)
        self.wfile.write(self.__dict__)
        self.wfile.write(config.__dict__)
        return

    def do_POST(self):
        print("In POST Handler for ",self)
        self.wfile.write(self.__dict__)
        self.wfile.write(config.__dict__)
        config.httpd_running = False
        return

# create http daemon
httpd = BaseHTTPServer.HTTPServer(addy,httpd_handler)
httpd.timeout = 0.1

print "Starting HTTP Server"
config.httpd_running = True
while config.httpd_running:
    # Check for any pending HTTP events
    httpd.handle_request()
    # Run the rest of the program
print "Stopped HTTP Server"
