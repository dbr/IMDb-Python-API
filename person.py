#!/usr/bin/env python
# encoding: utf-8
"""
person.py

Provides functions to interact with the person feature of the IMDb iPhone API.
"""

from base import *


class imdb_person(imdb):

	Name = 'imdb_person'

	"""Set person ID constant and run the parent's init method.

	Keyword arguments:
	url -- An IMdb URL

	"""
	def __init__(self, url):
		self._person_id = self.get_person_id_from_url(url)
		super(imdb_person, self).__init__()


	"""Get person's IMDb ID from the URL provided

	Keyword arguments:
	url -- An IMDb URL to search for the ID

	"""
	def get_person_id_from_url(self, url):
		matches = re.search('/(nm[0-9]{7})/', url).group(1)
		if matches is not None:
			return matches
		else:
			raise Exception, 'get_person_id_from_url(): Invalid person ID.'

	"""Return the person ID"""
	def get_person_id(self):
		return self._person_id

	"""Get a person's main details"""
	def get_main_details(self):
		arg = {
			"nconst": self.get_person_id()
		}
		return self.make_request('/name/maindetails', arg)

	"""Get a person's photo URLs"""
	def get_photos(self):
		arg = {
			"nconst": self.get_person_id()
		}
		return self.make_request('/name/photos', arg)

	"""Get a person's filmography"""
	def get_filmography(self):
		arg = {
			"nconst": self.get_person_id()
		}
		return self.make_request('/name/filmography', arg)

	"""Get a person's trivia"""
	def get_trivia(self):
		arg = {
			"nconst": self.get_person_id()
		}
		return self.make_request('/name/trivia', arg)

	"""Get a person's quotes"""
	def get_quotes(self):
		arg = {
			"nconst": self.get_person_id()
		}
		return self.make_request('/name/quotes', arg)