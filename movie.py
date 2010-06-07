#!/usr/bin/env python
# encoding: utf-8
"""
movie.py

Provides functions to interact with the movie/series features of the IMDb iPhone API.
"""

from base import *


class imdb_movie(imdb):

	Name = 'imdb_movie'

	"""Set title ID constant and run the parent's init method.

	Keyword arguments:
	url -- An IMdb URL

	"""
	def __init__(self, url):
		self._title_id = self.get_title_id_from_url(url)
		super(imdb_movie, self).__init__()


	"""Get title's IMDb ID from the URL provided

	Keyword arguments:
	url -- An IMDb URL to search for the ID

	"""
	def get_title_id_from_url(self, url):
		matches = re.search('/(tt[0-9]{7})/', url).group(1)
		if matches is not None:
			return matches
		else:
			raise Exception, 'get_title_id_from_url(): Invalid title ID.'

	"""Return the title ID"""
	def get_title_id(self):
		return self._title_id

	"""Get the main details for the current movie/series"""
	def get_main_details(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/maindetails', arg)

	"""Get photo URLs for the current movie/series"""
	def get_photos(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/photos', arg)

	"""Get the plot summary for the current movie/series"""
	def get_plot_summary(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/plot', arg)

	"""Get the synopsis for the current movie/series"""
	def get_synopsis(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/synopsis', arg)

	"""Get the complete cast and crew list for the current movie/series"""
	def get_all_cast(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/fullcredits', arg)

	"""Get external review URLs for the current movie/series"""
	def get_external_reviews(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/external_reviews', arg)

	"""Get the user review URL list for the current movie/series"""
	def get_user_reviews(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/usercomments', arg)

	"""Get the parental guide for the current movie/series"""
	def get_parental_guide(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/parentalguide', arg)

	"""Get the trivia for the current movie/series"""
	def get_trivia(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/trivia', arg)

	"""Get the quotes for the current movie/series"""
	def get_quotes(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/quotes', arg)

	"""Get the goofs for the current movie/series"""
	def get_goofs(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/goofs', arg)

	"""Get an episode list sorted by season for the current series"""
	def get_episodes_by_season(self):
		arg = {
			"tconst": self.get_title_id()
		}
		return self.make_request('/title/episodes', arg)