#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import datetime


default = "No Value Present"


print "Content-Type: text/html"
print

body = """<html>
<head>
<title>Lab 1 - CGI experiments</title>
</head>
<body>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
The server address is %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
You are coming from  %s:%s.<br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>

</body>
</html>""" % (
        os.environ.get('SERVER_NAME', default), # Server Hostname
        os.environ.get('REMOTE_ADDR', default),# server IP
        os.environ.get('SERVER_PORT', default),# server port
        'REMOTE_HOST', # client hostname
        'REMOTE_ADDR', # client IP
        'eeee', # client port
        'ffff', # this script name
        datetime.'gggg', # time
        )

print body,
