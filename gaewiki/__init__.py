# encoding=utf-8

import os
import sys
import wsgiref.handlers

import webapp2
import handlers

application = webapp2.WSGIApplication(
    handlers.handlers,
    debug=True)
