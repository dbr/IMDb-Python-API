#!/usr/bin/env python
# encoding: utf-8
"""
features.py

Provides all functions to interact with the more special features of the IMDb iPhone API.
"""

from base import *
from datetime import datetime


class imdb_features(imdb):

	Name = 'imdb_features'

	"""Run the parent's init method."""
	def __init__(self):
		super(imdb_features, self).__init__()


	"""Gets show times for provided location on provided date.

	Keyword arguments:
	location -- A location in the format of XX,YYYYY. For example, 'US,33333'
	date (optional) -- The date to get show dates for, in SQL format YYYY-mm-dd. Defaults to the current date

	"""
	def get_show_times(self, location, date = None):
		if self.check_date(date) is False:
			date = datetime.now()
			date = date.strftime('%Y-%m-%d')
		if self.check_location(location) is False:
			raise Exception, 'get_show_times(): A proper location is required'
		arg = {
			"date": date,
			"location": location
		}
		return self.make_request('/showtimes/location', arg)

	"""Gets a list of movies coming soon"""
	def get_coming_soon(self):
		return self.make_request('/feature/comingsoon')

	"""Get current box office results for specified region

	Keyword arguments:
	region (optional) -- The box office region formatted in two character country code. Defaults to 'US'

	"""
	def get_box_office_results(self, region = None):
		if self.check_box_office_region(region) is False:
			region = 'US'
		arg {
			"boxoffice_region": region
		}
		return self.make_request('/boxoffice', arg)

	"""Get the MOVIEmeter list"""
	def get_movie_meter(self):
		return self.make_request('/chart/moviemeter')

	"""Get the latest STARmeter list"""
	def get_star_meter(self):
		return self.make_request('/chart/starmeter')

	"""Get the current top 250 movies"""
	def get_top_250(self):
		return self.make_request('/chart/top')

	"""Get the current bottom 100 movies"""
	def get_bottom_100(self):
		return self.make_request('/chart/bottom')

	"""Get a list of all genres"""
	def get_genres(self):
		arg = {
			"type": "genre"
		}
		return self.make_request('/keys', arg)

	"""Get popular movies by genre

	Keyword arguments:
	genre -- Genre to search movies by

	"""
	def get_popular_movies_by_genre(self, genre):
		arg = {
			"genre": genre
		}
		return self.make_request('/moviegenre', arg)

	"""Get the latest DVD and Blu-Ray releases

	Keyword arguments:
	marketplace -- Marketplace to get releases for. Defaults to 'US'

	"""
	def get_dvd_bluray_new_releases(self, marketplace = 'US'):
		date = datetime.now()
		date = date.strftime('%Y-%m-%d')
		arg = {
			"date": date,
			"marketplace": marketplace
		}
		return self.make_request('/products/new_releases', arg)

	"""Get latest DVD best sellers

	Keyword arguments:
	marketplace -- Marketplace to get best sellers for. Defaults to 'US'

	"""
	def get_dvd_bestsellers(self, marketplace = 'US'):
		arg = {
			"marketplace": marketplace,
			"media": "dvd"
		}
		self.make_request('/products/bestsellers', arg)

	"""Get latest Blu-Ray best sellers

	Keyword arguments:
	marketplace -- Marketplace to get best sellers for. Defaults to 'US'

	"""
	def get_bluray_bestsellers(self, marketplace = 'US'):
		arg = {
			"marketplace": marketplace,
			"media": "blu_ray"
		}
		return self.make_request('/products/bestsellers', arg)

	"""Get all 'Best Picture' winners"""
	def get_best_picture_winners(self):
		return self.make_request('/feature/best_picture')

	"""Get TV program for a given night

	Keyword arguments:
	date (optional) -- Date to get TV program for, in SQL format YYYY-mm-dd. Defaults to the current date
	"""
	def get_us_tv_tonight(self, date = None):
		if self.check_date(date) is False:
			date = datetime.now()
			date = date.strftime('%Y-%m-%d')
		arg = {
			"date": date
		}
		return self.make_request('/tv/tonight', arg)

	"""Get TV recaps for a given night

	Keyword arguments:
	date (optional) -- Date to get TV recaps for, in SQL format YYYY-mm-dd. Defaults to the current date
	"""
	def get_us_tv_recaps(self, date = None):
		if self.check_date(date) is False:
			date = datetime.now()
			date = date.strftime('%Y-%m-%d')
		arg = {
			"date": date
		}
		return self.make_request('/tv/recap', arg)

	"""Get popular TV shows"""
	def get_popular_tv(self, date = None):
		return self.make_request('/chart/tv')

	"""Get a list of people born the provided date

	Keyword arguments:
	date (optional) -- Date to get birthdays for, in SQL format YYYY-mm-dd. Defaults to the current date

	"""
	def get_born_today(self, date = None):
		if self.check_date(date) is False:
			date = datetime.now()
			date = date.strftime('%Y-%m-%d')
		arg = {
			"date": date
		}
		return self.make_request('/feature/borntoday', arg)

	"""Get the latest news"""
	def get_news(self):
		return self.make_request('/news')


	"""Checks if provided location is in a valid format

	Keyword arguments:
	location -- Location to check. Should be in the format 'US,33333'

	"""
	def check_location(self, location):
		match = re.match('^([A-Z]{2}),([0-9]{5})$', location)
		if match is not None:
			return True
		else:
			raise Exception, 'check_location(): Format should be XX,YYYYY. For example US,33333.'

	"""Checks if the provided date is in a valid format

	Keyword arguments:
	date -- Date to check. Should be in the SQL format YYYY-mm-dd, e.g. '2009-12-24'

	"""
	def check_date(self, date):
		match = re.match('^([1-3][0-9]{3,3})-(0?[1-9]|1[0-2])-(0?[1-9]|[1-2][1-9]|3[0-1])$', date)
		if match is not None:
			return True
		else:
			return False

	"""Checks if provided box office location is in a valid format

	Keyword arguments:
	region -- Region to check. Should be a two character country code like 'US'

	"""
	def check_box_office_region(self, region):
		match = re.match('^([A-Z]{2})?$', region)
		if match is not None:
			return True
		else:
			return False