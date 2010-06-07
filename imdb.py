#!/usr/bin/env python
# encoding: utf-8
"""
imdb.py

A test case for the Python hacked IMDb iPhone API.
"""

from search import *
from movie import *


def main():
	search = imdb_search()
	print search.get_search_results('ghost busters')


if __name__ == '__main__':
	main()

