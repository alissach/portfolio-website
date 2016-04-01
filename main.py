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
        try:
            template = JINJA_ENVIRONMENT.get_template('/templates' + self.request.path + ".html") #using string concatenation to retrieve urls using this one handler; to avoid showing .html in address bar I can use just the simple filepath, but must concatenate ".html" to make all the links work properly
            self.response.write(template.render({}))
            logging.info("Using self.request.path for AllHandlers; here's the current path: " + self.request.path)
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html') #Redirect to error page
            self.response.write(template.render({'title': 'Home'}))
            logging.info("Failed to use current path: " + self.request.path +" Redirecting to index.html")

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title': 'Contact'})) #Set title of login page
        logging.info("Contact form page using GET") 

    def post(self):
        (name, email, msg) = (self.request.get('name'), self.request.get('email'), self.request.get('msg')) #tuple assignment
        template = JINJA_ENVIRONMENT.get_template('templates/postcontact.html') #retrieve postlogin.html as template
        self.response.write(template.render({'name': name, 'email': email, 'msg': msg}))
        
app = webapp2.WSGIApplication([
    ('/', AllHandlers),
    ('/index', AllHandlers),
    ('/aboutme', AllHandlers),
    ('/blog', AllHandlers),
    ('/resume', AllHandlers),
    ('/contact', ContactHandler),
    ('/.*', AllHandlers)
], debug=True)
