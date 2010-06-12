#!/usr/bin/env python
# encoding: utf-8
#FIXME: This file has not been refactored yet
"""
Provides all functions to interact with the more special features of the IMDb iPhone API.
"""

from .base import Imdb
from datetime import datetime


class ImdbFeatures(Imdb):
    def get_show_times(self, location, date = None):
        """Gets show times for provided location on provided date.

        Keyword arguments:
        location -- A location in the format of XX,YYYYY. For example, 'US,33333'
        date (optional) -- The date to get show dates for, in SQL format YYYY-mm-dd. Defaults to the current date

        """
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

    def get_coming_soon(self):
        """Gets a list of movies coming soon"""
        return self.make_request('/feature/comingsoon')

    def get_box_office_results(self, region = None):
        """Get current box office results for specified region

        Keyword arguments:
        region (optional) -- The box office region formatted in two character country code. Defaults to 'US'

        """
        if self.check_box_office_region(region) is False:
            region = 'US'
        arg {
            "boxoffice_region": region
        }
        return self.make_request('/boxoffice', arg)

    def get_movie_meter(self):
        """Get the MOVIEmeter list"""
        return self.make_request('/chart/moviemeter')

    def get_star_meter(self):
        """Get the latest STARmeter list"""
        return self.make_request('/chart/starmeter')

    def get_top_250(self):
        """Get the current top 250 movies"""
        return self.make_request('/chart/top')

    def get_bottom_100(self):
        """Get the current bottom 100 movies"""
        return self.make_request('/chart/bottom')

    def get_genres(self):
        """Get a list of all genres"""
        arg = {
            "type": "genre"
        }
        return self.make_request('/keys', arg)

    def get_popular_movies_by_genre(self, genre):
        """Get popular movies by genre

        Keyword arguments:
        genre -- Genre to search movies by
        """
        arg = {
            "genre": genre
        }
        return self.make_request('/moviegenre', arg)

    def get_dvd_bluray_new_releases(self, marketplace = 'US'):
        """Get the latest DVD and Blu-Ray releases

        Keyword arguments:
        marketplace -- Marketplace to get releases for. Defaults to 'US'
        """
        date = datetime.now()
        date = date.strftime('%Y-%m-%d')
        arg = {
            "date": date,
            "marketplace": marketplace
        }
        return self.make_request('/products/new_releases', arg)

    def get_dvd_bestsellers(self, marketplace = 'US'):
        """Get latest DVD best sellers

        Keyword arguments:
        marketplace -- Marketplace to get best sellers for. Defaults to 'US'
        """
        arg = {
            "marketplace": marketplace,
            "media": "dvd"
        }
        self.make_request('/products/bestsellers', arg)

    def get_bluray_bestsellers(self, marketplace = 'US'):
        """Get latest Blu-Ray best sellers

        Keyword arguments:
        marketplace -- Marketplace to get best sellers for. Defaults to 'US'
        """
        arg = {
            "marketplace": marketplace,
            "media": "blu_ray"
        }
        return self.make_request('/products/bestsellers', arg)

    def get_best_picture_winners(self):
        """Get all 'Best Picture' winners"""
        return self.make_request('/feature/best_picture')

    def get_us_tv_tonight(self, date = None):
        """Get TV program for a given night

        Keyword arguments:
        date (optional) -- Date to get TV program for, in SQL format YYYY-mm-dd. Defaults to the current date
        """
        if self.check_date(date) is False:
            date = datetime.now()
            date = date.strftime('%Y-%m-%d')
        arg = {
            "date": date
        }
        return self.make_request('/tv/tonight', arg)

    def get_us_tv_recaps(self, date = None):
        """Get TV recaps for a given night

        Keyword arguments:
        date (optional) -- Date to get TV recaps for, in SQL format YYYY-mm-dd. Defaults to the current date
        """
        if self.check_date(date) is False:
            date = datetime.now()
            date = date.strftime('%Y-%m-%d')
        arg = {
            "date": date
        }
        return self.make_request('/tv/recap', arg)

    def get_popular_tv(self, date = None):
        """Get popular TV shows"""
        return self.make_request('/chart/tv')

    def get_born_today(self, date = None):
        """Get a list of people born the provided date

        Keyword arguments:
        date (optional) -- Date to get birthdays for, in SQL format YYYY-mm-dd. Defaults to the current date
        """
        if self.check_date(date) is False:
            date = datetime.now()
            date = date.strftime('%Y-%m-%d')
        arg = {
            "date": date
        }
        return self.make_request('/feature/borntoday', arg)

    def get_news(self):
        """Get the latest news"""
        return self.make_request('/news')


    def check_location(self, location):
        """Checks if provided location is in a valid format

        Keyword arguments:
        location -- Location to check. Should be in the format 'US,33333'
        """
        match = re.match('^([A-Z]{2}),([0-9]{5})$', location)
        if match is not None:
            return True
        else:
            raise Exception, 'check_location(): Format should be XX,YYYYY. For example US,33333.'

    def check_date(self, date):
        """Checks if the provided date is in a valid format

        Keyword arguments:
        date -- Date to check. Should be in the SQL format YYYY-mm-dd, e.g. '2009-12-24'
        """
        match = re.match('^([1-3][0-9]{3,3})-(0?[1-9]|1[0-2])-(0?[1-9]|[1-2][1-9]|3[0-1])$', date)
        if match is not None:
            return True
        else:
            return False

    def check_box_office_region(self, region):
        """Checks if provided box office location is in a valid format

        Keyword arguments:
        region -- Region to check. Should be a two character country code like 'US'
        """
        match = re.match('^([A-Z]{2})?$', region)
        if match is not None:
            return True
        else:
            return False
