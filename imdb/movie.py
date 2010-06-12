#!/usr/bin/env python
# encoding: utf-8
#FIXME: This file has not been refactored yet
"""
Provides functions to interact with the movie/series features of the IMDb iPhone API.
"""

from .base import Imdb


class ImdbMovie(Imdb):
    def __init__(self, url):
        """Set title ID constant and run the parent's init method.

        Keyword arguments:
        url -- An IMdb URL

        """
        self._title_id = self.get_title_id_from_url(url)
        super(imdb_movie, self).__init__()


    def get_title_id_from_url(self, url):
        """Get title's IMDb ID from the URL provided

        Keyword arguments:
        url -- An IMDb URL to search for the ID

        """
        matches = re.search('/(tt[0-9]{7})/', url).group(1)
        if matches is not None:
            return matches
        else:
            raise Exception, 'get_title_id_from_url(): Invalid title ID.'

    def get_title_id(self):
        """Return the title ID"""
        return self._title_id

    def get_main_details(self):
        """Get the main details for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/maindetails', arg)

    def get_photos(self):
        """Get photo URLs for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/photos', arg)

    def get_plot_summary(self):
        """Get the plot summary for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/plot', arg)

    def get_synopsis(self):
        """Get the synopsis for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/synopsis', arg)

    def get_all_cast(self):
        """Get the complete cast and crew list for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/fullcredits', arg)

    def get_external_reviews(self):
        """Get external review URLs for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/external_reviews', arg)

    def get_user_reviews(self):
        """Get the user review URL list for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/usercomments', arg)

    def get_parental_guide(self):
        """Get the parental guide for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/parentalguide', arg)

    def get_trivia(self):
        """Get the trivia for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/trivia', arg)

    def get_quotes(self):
        """Get the quotes for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/quotes', arg)

    def get_goofs(self):
        """Get the goofs for the current movie/series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/goofs', arg)

    def get_episodes_by_season(self):
        """Get an episode list sorted by season for the current series"""
        arg = {
            "tconst": self.get_title_id()
        }
        return self.make_request('/title/episodes', arg)
