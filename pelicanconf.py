#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "/home/mat/Projects/Flex"

AUTHOR = u'Matt Kieblesz'
SITENAME = u'OpenDevBlog'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Matt Kieblesz'
SITESUBTITLE = 'Software Engineer'
SITEDESCRIPTION = 'Matt\'s thoughts on writing effective software'
BROWSER_COLOR = '#333'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('linkedin', 'https://uk.linkedin.com/in/matt-kieblesz-4a4a75124'),
          ('github', 'https://github.com/mattkieblesz'),)

DEFAULT_PAGINATION = 5

# FAVICON = SITEURL + '/images/favicon.ico'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2016
# CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

ADD_THIS_ID = 'ra-57863b21a2797cb3'
DISQUS_SITENAME = "opendevblog"
GOOGLE_ANALYTICS = "UA-80715356-1"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
