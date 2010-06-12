#!/usr/bin/env python
# encoding: utf-8
"""
search.py

Provides functions to interact with the search feature of the IMDb iPhone API.
"""

from __future__ import absolute_import
from .base import Imdb
import urllib


def search(term):
    i = Imdb()

    arg = {"q": term}
    return i.make_request('/find', arg)
