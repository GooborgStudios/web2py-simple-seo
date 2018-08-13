# web2py Module: plugin_simple_seo
# Original version (c) cccaballero (https://github.com/daxslab/web2py-simple-seo), version 2.0 (c) Gooborg Studios, 2018.

__author__ = ['cccaballero', 'vinyldarkscratch']

from gluon import *
from collections import OrderedDict

# -=- Basic Set Functions -=-

def set_seo_tag(mame, value):
	if value is None:
		return
	if isinstance(value, dict):
		for k, v in value.iteritems():
			if k == "main": set_seo_tag(name, v)
			else: set_seo_tag("%s:%s" %(name, k), v)
	if isinstance(value, list):
		for i in range(len(value)):
			d = OrderedDict()
			d['property'] = "%s" %name
			d['content'] = value[count]
			current.response.meta['%s_%d' %(name.replace(":", "_"), i)] = d
	else:
		d = OrderedDict()
		d['property'] = "%s" %name
		d['content'] = value
		current.response.meta['%s' %name.replace(":", "_")] = d

# web2py Meta
def set_meta(name, value):
	set_seo_tag(name, value)

# Open Graph
def set_og(name, value):
	set_seo_tag("og:%s" %name, value)

# Twitter Card
def set_tc(name, value):
	set_seo_tag("tc:%s" %name, value)

def set_all_seo(name, value):
	set_meta(name, value)
	set_og(name, value)
	set_tc(name, value)

# -=- Initializers -=-

def init_seo(type="website", card="summary", title=None, author=None, keywords=None, generator="Web2py Web Framework", image=None, description=None, site_name=None, locale=current.T.accepted_language or 'en', locale_alternate=[], twitter_username=None, label1=None, data1=None, label2=None, data2=None):
	init_meta(title, description, keywords, author, generator)
	init_og(type, title, image, description, determiner, site_name, locale, locale_alternate)
	init_tc(card, title, twitter_username, label1, data1, label2, data2, image, description)

def init_meta(title=None, description=None, keywords=None, author=None, generator="Web2py Web Framework"):
	data = locals()
	for name in ['title', 'description', 'keywords', 'author', 'generator']:
		if data[name]: set_meta(name, data[name])

def init_og(type="website", title=None, image=None, description=None, determiner="auto", site_name=None, locale=None, locale_alternate=[]):
	url = URL(args=current.request.args, host=True)
	data = locals()
	for name in ['type', 'title', 'image', 'url', 'description', 'determiner', 'site_name', 'locale']:
		if data[name]: set_og(name, data[name])

def init_tc(card="summary", title=None, username=None, label1=None, data1=None, label2=None, data2=None, image=None, description=None):
	data = locals()
	for name in ['card', 'title', 'label1', 'data1', 'label2', 'data2', 'image', 'description']:
		if data[name]: set_tc(name, data[name])
	if username:
		for name in ['site', 'creator']: set_tc(name, username)

# -=- Set Specific Types -=-

# XXX Add the following types:
	# article: http://ogp.me/ns/article#
	# book: http://ogp.me/ns/book#
	# books: http://ogp.me/ns/books#
	# business: http://ogp.me/ns/business#
	# fitness: http://ogp.me/ns/fitness#
	# game: http://ogp.me/ns/game#
	# music: http://ogp.me/ns/music#
	# place: http://ogp.me/ns/place#
	# product: http://ogp.me/ns/product#
	# profile: http://ogp.me/ns/profile#
	# restaurant: http://ogp.me/ns/restaurant#
	# video: http://ogp.me/ns/video#

# -=- Specific Properties -=-

# Title
def set_title(title):
	set_all_seo("title", title)

def title(new_title):
	def wrapper(function):
		def f(*args, **kwargs):
			set_title(new_title)
			
			return function(*args, **kwargs)
		return f
	return wrapper

# Description
def set_description(description):
	set_all_seo("description", description)

def description(new_description):
	def wrapper(function):
		def f(*args, **kwargs):
			set_description(new_description)
			
			return function(*args, **kwargs)
		return f
	return wrapper

# Image
def set_image(image):
	set_og("image", image)
	set_tc("image", image)

def image(new_image):
	def wrapper(function):
		def f(*args, **kwargs):
			set_image(new_image)
			
			return function(*args, **kwargs)
		return f
	return wrapper
