#!/usr/bin/env python
# encoding: utf-8
"""
search.py

Provides functions to interact with the search feature of the IMDb iPhone API.
"""

from base import *
import urllib


class imdb_search(imdb):
	Name = 'imdb_search'

	"""Run the parent's init method"""
	def __init__(self):
		super(imdb_search, self).__init__()


	"""Return search results for the provided query

	Keyword arguments:
	search_term -- The term to query IMDb for.

	"""
	def get_search_results(self, search_term):
		arg = {
			"q": urllib.quote_plus(search_term)
		}
		return self.make_request('/find', arg)