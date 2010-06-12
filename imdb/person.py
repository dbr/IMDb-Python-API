#!/usr/bin/env python
# encoding: utf-8
#FIXME: This file has not been refactored yet
"""
Provides functions to interact with the person feature of the IMDb iPhone API.
"""

from .base import Imdb


class ImdbPerson(Imdb):
    def __init__(self, url):
        """Set person ID constant and run the parent's init method.

        Keyword arguments:
        url -- An IMdb URL

        """
        self._person_id = self.get_person_id_from_url(url)
        super(imdb_person, self).__init__()


    def get_person_id_from_url(self, url):
        """Get person's IMDb ID from the URL provided

        Keyword arguments:
        url -- An IMDb URL to search for the ID

        """
        matches = re.search('/(nm[0-9]{7})/', url).group(1)
        if matches is not None:
            return matches
        else:
            raise Exception, 'get_person_id_from_url(): Invalid person ID.'

    def get_person_id(self):
        """Return the person ID"""
        return self._person_id

    def get_main_details(self):
        """Get a person's main details"""
        arg = {
            "nconst": self.get_person_id()
        }
        return self.make_request('/name/maindetails', arg)

    def get_photos(self):
        """Get a person's photo URLs"""
        arg = {
            "nconst": self.get_person_id()
        }
        return self.make_request('/name/photos', arg)

    def get_filmography(self):
        """Get a person's filmography"""
        arg = {
            "nconst": self.get_person_id()
        }
        return self.make_request('/name/filmography', arg)

    def get_trivia(self):
        """Get a person's trivia"""
        arg = {
            "nconst": self.get_person_id()
        }
        return self.make_request('/name/trivia', arg)

    def get_quotes(self):
        """Get a person's quotes"""
        arg = {
            "nconst": self.get_person_id()
        }
        return self.make_request('/name/quotes', arg)
