# web2py Module: plugin_simple_seo
# Original version (c) cccaballero (https://github.com/daxslab/web2py-simple-seo), version 2.0 (c) Vinyl Darkscratch, 2018.

__author__ = ['cccaballero', 'vinyldarkscratch']

from gluon import *
from collections import OrderedDict

# -=- Basic Set Functions -=-

# web2py Meta
def set_meta(name, value):
	current.response[name] = value

# Open Graph
def set_og(name, value):
	if isinstance(value, list):
		for count in range(len(value)):
			d = OrderedDict()
			d['property'] = "og:%s" %name
			d['content'] = value[count]
			current.response.meta['og_%s_%d' %(name, count)] = d
	else:
		d = OrderedDict()
		d['property'] = "og:%s" %name
		d['content'] = value
		current.response.meta['og_%s' %name] = d

# Twitter Card
def set_tc(name, value):
	if isinstance(value, list):
		for count in range(len(value)):
			d = OrderedDict()
			d['name'] = "twitter:%s" %name
			d['content'] = value[count]
			current.response.meta['tc_%s_%d' %(name, count)] = d
	else:
		d = OrderedDict()
		d['name'] = "twitter:%s" %name
		d['content'] = value
		current.response.meta['tc_%s' %name] = d

# -=- Initializers -=-

def init_seo(type="website", card="summary", title=None, author=None, keywords=None, generator="Web2py Web Framework", image=None, description=None, site_name=None, locale=T.accepted_language or 'en', locale_alternate=[], twitter_username=None, label1=None, data1=None, label2=None, data2=None):
	init_meta(title, description, keywords, author, generator)
	init_og(type, title, image, description, site_name, locale, locale_alternate)
	init_tc(card, title, twitter_username, label1, data1, label2, data2, image, description)

def init_meta(title=None, description=None, keywords=None, author=None, generator="Web2py Web Framework"):
	data = locals()
	for name in ['title', 'description', 'keywords', 'author', 'generator']:
		if data[name]: set_meta(name, data[name])

def init_og(type="website", title=None, image=None, description=None, site_name=None, locale=None, locale_alternate=[]):
	url = URL(args=current.request.args, host=True)
	data = locals()
	for name in ['type', 'title', 'image', 'url', 'description', 'site_name', 'locale']:
		if data[name]: set_og(name, data[name])

def init_tc(card="summary", title=None, username=None, label1=None, data1=None, label2=None, data2=None, image=None, description=None):
	data = locals()
	for name in ['card', 'title', 'label1', 'data1', 'label2', 'data2', 'image', 'description']:
		if data[name]: set_tc(name, data[name])
	if username:
		for name in ['site', 'creator']: set_tc(name, username)

# -=- Title -=-

def set_title(title):
	set_meta("title", title)
	set_og("title", title)
	set_tc("title", title)

def title(new_title):
	def wrapper(function):
		def f(*args, **kwargs):
			set_title(new_title)
			
			return function(*args, **kwargs)
		return f
	return wrapper

# -=- Description -=-

def set_description(description):
	set_meta("description", description)
	set_og("description", description)
	set_tc("description", description)

def description(new_description):
	def wrapper(function):
		def f(*args, **kwargs):
			set_description(new_description)
			
			return function(*args, **kwargs)
		return f
	return wrapper

# -=- Image -=-

def set_image(image):
	set_og("image", image)
	set_tc("image", image)
