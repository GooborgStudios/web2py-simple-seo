# web2py Module: plugin_simple_seo
# Original version (c) cccaballero (https://github.com/daxslab/web2py-simple-seo)
# Version 2.0 (c) Vinyl Da.i'gyu-Kazotetsu (Gooborg Studios), 2018-2026.

__author__ = ['queengooborg', 'cccaballero']

from collections import OrderedDict

from gluon import URL, current

# -=- Basic Set Functions -=-

def set_seo_tag(name, value):
	if value is None:
		return

	f_name = name.replace(":", "_")

	if isinstance(value, dict):
		for k, v in value.items():
			if k == "main":
				set_seo_tag(name, v)
			else: set_seo_tag(f"{name}:{k}", v)
	if isinstance(value, list):
		for i in range(len(value)):
			d = OrderedDict()
			d['property'] = name
			d['name'] = name
			d['content'] = value[len(value)]
			current.response.meta[f"{f_name}_{i}"] = d
	else:
		d = OrderedDict()
		d['property'] = name
		d['name'] = name
		d['content'] = value
		current.response.meta[f_name] = d

# web2py Meta
def set_meta(name, value):
	set_seo_tag(name, value)
	current.response[name] = value

# Open Graph
def set_og(name, value):
	set_seo_tag(f"og:{name}", value)

# Twitter Card
def set_tc(name, value):
	set_seo_tag(f"tc:{name}", value)

def set_all_seo(name, value):
	set_meta(name, value)
	set_og(name, value)
	set_tc(name, value)

# -=- Initializers -=-

def init_seo(type="website", card="summary", title=None, author=None, keywords=None, generator="Web2py Web Framework", image=None, description=None, determiner="auto", site_name=None, locale=current.T.accepted_language or 'en', locale_alternate=(), twitter_username=None, label1=None, data1=None, label2=None, data2=None):
	init_meta(title, description, keywords, author, generator)
	init_og(type, title, image, description, determiner, site_name, locale, locale_alternate)
	init_tc(card, title, twitter_username, label1, data1, label2, data2, image, description)

def init_meta(title=None, description=None, keywords=None, author=None, generator="Web2py Web Framework"):
	set_meta("title", title)
	set_meta("description", description)
	set_meta("keywords", keywords)
	set_meta("author", author)
	set_meta("generator", generator)

def init_og(type="website", title=None, image=None, description=None, determiner="auto", site_name=None, locale=None, locale_alternate=()):	
	set_og("url", URL(args=current.request.args, host=True))

	set_og("type", type)
	set_og("title", title)
	set_og("image", image)
	set_og("description", description)
	set_og("determiner", determiner)
	set_og("site_name", site_name)
	set_og("locale", locale)
	set_og("locale:alternate", locale_alternate)

def init_tc(card="summary", title=None, username=None, label1=None, data1=None, label2=None, data2=None, image=None, description=None):
	set_tc("card", card)
	set_tc("title", title)
	set_tc("label1", label1)
	set_tc("data1", data1)
	set_tc("label2", label2)
	set_tc("data2", data2)
	set_tc("image", image)
	set_tc("description", description)

	if username:
		set_tc("name", username)
		set_tc("creator", username)

# -=- Specific Types -=-

# XXX Add the following types:
	# book: http://ogp.me/ns/book#
	# books: http://ogp.me/ns/books#
	# business: http://ogp.me/ns/business#
	# fitness: http://ogp.me/ns/fitness#
	# game: http://ogp.me/ns/game#
	# music: http://ogp.me/ns/music#
	# place: http://ogp.me/ns/place#
	# product: http://ogp.me/ns/product#
	# restaurant: http://ogp.me/ns/restaurant#
	# video: http://ogp.me/ns/video#

# https://developers.facebook.com/docs/reference/opengraph/#object-type

# Article
def set_article(author=None, content_tier="free", expiration_time=None, modified_time=None, published_time=None, publisher=None, section=None, tags=()):
	set_og("type", "article")
	set_og("article:author", author)
	set_og("article:expiration_time", expiration_time)
	set_og("article:modified_time", modified_time)
	set_og("article:published_time", published_time)
	set_og("article:publisher", publisher)
	set_og("article:section", section)
	set_og("article:tags", tags)
	if content_tier in ['free', 'locked', 'metered']: 
		set_og("article:content_tier", content_tier)

def article(author=None, content_tier="free", expiration_time=None, modified_time=None, published_time=None, publisher=None, section=None, tags=()):
	def wrapper(function):
		def f(*args, **kwargs):
			set_article(author, content_tier, expiration_time, modified_time, published_time, publisher, section, tags)

			return function(*args, **kwargs)
		return f
	return wrapper

# Profile
def set_profile(first_name=None, last_name=None, username=None, gender=None):
	set_og("type", "profile")
	set_og("profile:first_name", first_name)
	set_og("profile:last_name", last_name)
	set_og("profile:username", username)
	if gender in ['male', 'female']:
		set_all_seo("profile:gender", gender)

def profile(first_name=None, last_name=None, username=None, gender=None):
	def wrapper(function):
		def f(*args, **kwargs):
			set_profile(first_name, last_name, username, gender)

			return function(*args, **kwargs)
		return f
	return wrapper

# -=- Specific Properties -=-

# Title
def set_title(new_title):
	set_all_seo("title", new_title)

def title(new_title):
	def wrapper(function):
		def f(*args, **kwargs):
			set_title(new_title)

			return function(*args, **kwargs)
		return f
	return wrapper

# Description
def set_description(new_description):
	set_all_seo("description", new_description)

def description(new_description):
	def wrapper(function):
		def f(*args, **kwargs):
			set_description(new_description)

			return function(*args, **kwargs)
		return f
	return wrapper

# Image
def set_image(new_image):
	set_og("image", new_image)
	set_tc("image", new_image)

def image(new_image):
	def wrapper(function):
		def f(*args, **kwargs):
			set_image(new_image)

			return function(*args, **kwargs)
		return f
	return wrapper
