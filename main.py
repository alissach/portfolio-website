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

########## Alissa Chan ##########
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AllHandlers(webapp2.RequestHandler):
    def get(self):
        try: #try block necessary to keep code running and to set homepage as the default if url fails (see except block)
            template = JINJA_ENVIRONMENT.get_template('/templates' + self.request.path + ".html") #using string concatenation to retrieve urls using this one handler; to avoid showing .html in address bar I can use just the simple filepath, but must concatenate ".html" to make all the links work properly
            self.response.write(template.render({})) #nothing to render in base.html, so I just left dictionary blank.
            logging.info("Using self.request.path for AllHandlers; here's the current path: " + self.request.path) #logging info to check what the path is of the current page; this is how I figured out you have to append .html in line 30.
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/home.html') #use default homepage if above fails
            self.response.write(template.render({'title': 'Home'}))
            logging.info("Failed to use current path: " + self.request.path +" Redirecting to home.html")

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'Login'})) #Set title of login page
        logging.info("Form login page using GET") 

    def post(self):
        (username, pw) = (self.request.get('username'), self.request.get('pw')) #tuple assignment: setting variable username and pw to retrieve data associated with name "username" and "pw" from the form, respectively

        template = JINJA_ENVIRONMENT.get_template('templates/postlogin.html') #retrieve postlogin.html as template
        self.response.write(template.render({'username': username, 'pw': pw}))
        if username != "Colleen" and pw != "pass":
            logging.info("Invalid credentials used; Username: " + username + " password: " + pw) #print in log the username and password only when invalid credentials were used.
app = webapp2.WSGIApplication([
    ('/home', AllHandlers),
    ('/aboutme', AllHandlers),
    ('/blog', AllHandlers),
    ('/login', LoginHandler),
    ('/.*', AllHandlers)
], debug=True)
