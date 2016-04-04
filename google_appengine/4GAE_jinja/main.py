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
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
 loader=jinja2.FileSystemLoader(os.path.dirname( __file__ )),
 extensions=["jinja2.ext.autoescape"],
 autoescape=True)


class MainHandler(webapp2.RequestHandler):
	def __init__(self,request=None,response=None):
		self.initialize(request,response)
		self.name=self.request.get("edName","anonymous")
	def get(self):
		pass
	def post(self):
		label_values={
			"user_name": self.name,
			"user_list": [1,2,3,4,5,6,7,8,9]
		}
		template = JINJA_ENVIRONMENT.get_template( "answer.html" )
		self.response.write(template.render(label_values))

class MainHandler2(webapp2.RequestHandler):
	def __init__(self,request=None,response=None):
		self.initialize(request,response)
	def get(self):
		pass
	def post(self):
		self.redirect("index2.html")

app = webapp2.WSGIApplication([
    ('/doit', MainHandler),('/doit2', MainHandler2)
], debug=True)
