# Adding REST API to Python App 

Just some example code using timeouts in BaseHTTPServer to add a REST API to a
Python app.

Currently, the app will exit once a POST request is sent to the web server on
port 1024. There is no additional processing being done, but whatever it is, 
should be done fairly quickly to allow the app to check for any pending HTTP
requests.

No authentication enabled, no SSL. Not Production ready!

![](https://github.com/sduff/adding_rest_api_to_python_app/workflows/Test with Python 2.x/badge.svg)

![](https://github.com/sduff/adding_rest_api_to_python_app/workflows/Test with Python 3.x/badge.svg)
