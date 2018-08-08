# web2py Module: plugin_simple_seo
# Original version (c) cccaballero (https://github.com/daxslab/web2py-simple-seo), version 2.0 (c) Vinyl Darkscratch, 2018.

__author__ = ['cccaballero', 'vinyldarkscratch']

from gluon import *
from collections import OrderedDict

def set_seo_meta(type="website", card="summary", title=None, author=None, keywords=None, generator="Web2py Web Framework", image=None, description=None, site_name=None, locale=None, locale_alternate={}, twitter_username=None, label1=None, data1=None, label2=None, data2=None):
	set_meta(title, description, keywords, author, generator)
	set_open_graph(type, title, image, description, site_name, locale, locale_alternate)
	set_twitter_card(card, title, twitter_username, label1, data1, label2, data2, image, description)

def set_meta(title=None, description=None, keywords=None, author=None, generator="Web2py Web Framework"):
	data = locals()
	for name in ['title', 'description', 'keywords', 'author', 'generator']:
		if data[name]: current.response.meta[name] = data[name]

def set_open_graph(type="website", title=None, image=None, description=None, site_name=None, locale=None, locale_alternate={}):
	url = URL(args=current.request.args, host=True)
	data = locals()
	for name in ['type', 'title', 'url', 'description', 'site_name', 'locale']:
		d = OrderedDict()
		if data[name]:
			d['property'] = "og:"+name
			d['content'] = data[name]
			current.response.meta['og_'+name] = d
	if image: set_og_image(image)

def set_twitter_card(card="summary", title=None, username=None, label1=None, data1=None, label2=None, data2=None, image=None, description=None):
	data = locals()
	for name in ['card', 'title', 'description', 'label1', 'data1', 'label2', 'data2']:
		d = OrderedDict()
		if data[name]:
			d['property'] = "twitter:"+name
			d['content'] = data[name]
			current.response.meta['tc_'+name] = d
	if username:
		for name in ['site', 'creator']:
			d = OrderedDict()
			d['property'] = "twitter:"+name
			d['content'] = username
			current.response.meta['tc_'+name] = d
	if image: set_tc_image(image)

# Open Graph meta
def set_og_image(image):
	if isinstance(image, list):
		for count in range(len(image)):
			d = OrderedDict()
			d['property'] = "og:image"
			d['content'] = image[count]
			current.response.meta['og_image_'+str(count)] = d
	else:
		d = OrderedDict()
		d['property'] = "og:image"
		d['content'] = image
		current.response.meta.og_image = d

# Twitter Card meta
def set_tc_image(image):
	if isinstance(image, list): image = image[0]
	d = OrderedDict()
	d['name'] = "twitter:image"
	d['content'] = image
	current.response.meta.tc_image = d
