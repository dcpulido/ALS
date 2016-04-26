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
from google.appengine.api import users

import os
import webapp2
import jinja2
from mainMenu import MainMenuHandler
from game import gameHandler
from addGame import gameAddHandler
from player import playerHandler
from addPlayer import playerAddHandler
from addTeam import teamAddHandler

from equipo import Equipo
from jugador import Jugador

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_name = "Please login"
        user = users.get_current_user()
        if  user !=None:
            if  user.email() == "dcpulido@gmail.com" :
                self.redirect("/main") 
        access_link = users.create_login_url("/main")

        template_values = {
            "user_name": user_name,
            "access_link": access_link,
        }
    
        template = JINJA_ENVIRONMENT.get_template( "index.html" )
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/main", MainMenuHandler),
    ("/game",gameHandler),
    ("/addGame",gameAddHandler),
    ("/player",playerHandler),
    ("/addPlayer",playerAddHandler),
    ("/addTeam",teamAddHandler)
], debug=True)



