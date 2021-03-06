#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def buil_page(text_content):
	rot_label = "<label>Rotate by:</label>"
	rot_input = "<input type='number' name='rot'/>"
	header = "<h2>Welcome to Web Caesar</h2>"
	message_label= "<label>Type a message:</label>"
	textarea = "<textarea name='message'>" + text_content + "</textarea>"
	submit = "<input type= 'submit'/>"
	form = "<form method='post'>" + rot_label + rot_input + "<br>" + message_label + textarea + "<br>" + submit + "</form>"

	return header + form

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(buil_page(""))

	def post(self):
		message = self.request.get('message')
		rot = int(self.request.get('rot'))
		encrypted_message = caesar.encrypt(message, rot)
		escaped_message = cgi.escape(encrypted_message)		
		self.response.write(buil_page(escaped_message))

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
