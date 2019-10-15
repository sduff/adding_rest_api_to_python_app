#!/usr/local/bin/python

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except:
    from http.server import BaseHTTPRequestHandler, HTTPServer

# listen on port 1024 of the localhost
addy = ('',1024)

# A global data structure for access between HTTP server and main code
class Config(object):
    httpd_running = False
config = Config()

# define the http handler
class httpd_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(("In GET Handler for ",self))
        self.wfile.write(str(self.__dict__).encode())
        self.wfile.write(str(config.__dict__).encode())
        return

    def do_POST(self):
        print(("In POST Handler for ",self))
        self.wfile.write(str(self.__dict__).encode())
        self.wfile.write(str(config.__dict__).encode())
        config.httpd_running = False
        return

# create http daemon
httpd = HTTPServer(addy,httpd_handler)
httpd.timeout = 0.1

print("Starting HTTP Server")
config.httpd_running = True
while config.httpd_running:
    # Check for any pending HTTP events
    httpd.handle_request()
    # Run the rest of the program
print("Stopped HTTP Server")
