#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Stephan Helas <stephan.helas@pp-nt.com>
#
# Distributed under terms of the MIT license.

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 12345

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            # Send the html message
            self.wfile.write("ok")

            # do something with uri
            print self.path

            return
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
