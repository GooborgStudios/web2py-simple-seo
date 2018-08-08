# -*- coding: utf-8 -*-

# web2py Model: plugin_simple_seo
# Original version (c) cccaballero (https://github.com/daxslab/web2py-simple-seo), version 2.0 (c) Vinyl Darkscratch, 2018.

from plugin_simple_seo.seo import set_seo_meta, set_og_image, set_tc_image
from gluon.contrib.ordereddict import OrderedDict

# -=- Title -=-

def set_title(title):
	response.title = title

	d = OrderedDict()
	d['property'] = "og:title"
	d['content'] = title
	response.meta['og_title'] = d

	d = OrderedDict()
	d['property'] = "tc:title"
	d['content'] = title
	response.meta['tc_title'] = d

def title(new_title):
	def wrapper(function):
		def f(*args, **kwargs):
			set_title(new_title)
			
			return function(*args, **kwargs)
		return f
	return wrapper

# -=- Description -=-

def set_description(description):
	response.description = description

	d = OrderedDict()
	d['property'] = "og:description"
	d['content'] = description
	response.meta['og_description'] = d

	d = OrderedDict()
	d['property'] = "tc:description"
	d['content'] = description
	response.meta['tc_description'] = d

def description(new_description):
	def wrapper(function):
		def f(*args, **kwargs):
			set_description(new_description)
			
			return function(*args, **kwargs)
		return f
	return wrapper

# -=- Image -=-

def set_image(image):
	set_og_image(image)
	set_tc_image(image)
