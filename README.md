# Adding REST API to Python App 

Just some example code using timeouts in BaseHTTPServer to add a REST API to a
Python app.

Currently, the app will exit once a POST request is sent to the web server on
port 1024. There is no additional processing being done, but whatever it is, 
should be done fairly quickly to allow the app to check for any pending HTTP
requests.

No authentication enabled, no SSL. Not Production ready!

Python 2.x, should be easily convertable to Python 3
