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
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
	def __init__(self,request=None,response=None):
		self.initialize(request,response)
	def get(self):
		access_link="ERROR"
		logged="logged In"
		userid="None"
		user= users.get_current_user()

		if user != None:
			access_link = users.create_logout_url("/")
			User_id=user.nickname()
		else:
			access_link = users.create_login_url("/")
			logged="Not logged In"

		self.response.write( "<a href='"+ access_link+"'>login/logout</a>\
							<br>"+logged\
							+ "<br>" +userid)
	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
