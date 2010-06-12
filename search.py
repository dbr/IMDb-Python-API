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

    def __init__(self):
        """Run the parent's init method"""
        super(imdb_search, self).__init__()


    def get_search_results(self, search_term):
        """Return search results for the provided query

        Keyword arguments:
        search_term -- The term to query IMDb for.
        """
        arg = {
            "q": urllib.quote_plus(search_term)
        }
        return self.make_request('/find', arg)