#!/usr/bin/env python
# encoding: utf-8
"""
Base class to interact with the IMDb iPhone API.
"""

import re
import time
import json
import random
import string
import urllib
import urllib2
from hmac import HMAC
from hashlib import sha1

from .exceptions import ImdbRequestError, ImdbInvalidLocale


class Imdb(object):
    # Hardcoded constants for the IMDb iPhone API - Do not change these!
    # API version
    _api = 'v1'
    # Application identification
    _app_id = 'iphone1_1'
    # API key, needed to sign the request
    _api_key = '2wex6aeu6a8q9e49k7sfvufd6rhh0n'
    # API host
    _host = 'app.imdb.com'
    # API policy
    _api_policy = 'app1_1'

    # Default locale
    _locale = 'en_US'

    def __init__(self):
        """Run a status check on initialization, to make sure everything is working"""
        self.status_check()

    def set_locale(self, locale = None):
        """Sets the locale used in requests

        If no argument is passed, the locale is reset to the default en_US
        Valid locales are: en_US, de_DE, fr_FR, pt_PT, it_IT

        Keyword arguments:
        locale -- The locale of the format xx_XX
        """
        if locale is None:
            self._locale = 'en_US'
        else:
            match = re.match('^[a-z]{2}_[A-Z]{2}$', locale)
            if match is not None:
                self._locale = locale
            else:
                raise ImdbInvalidLocale('Format should be xx_XX. For example en_US.')

    def get_locale(self):
        """Returns the current locale."""
        return self._locale

    def create_parameters(self, arguments = None):
        """Create the parameter dict for requests

        Keyword arguments:
        arguments -- A dict with arguments to append the request
        """
        random.seed(14)
        parameter = {
            'api': self._api,
            'app_id': self._app_id,
            # Create a string of 40 random characters for device name
            'device': ''.join([random.choice(string.letters) for x in xrange(40)]),
            'locale': self._locale,
            'timestamp': time.time(),
            'sig': self._api_policy,
        }
        if isinstance(arguments, dict):
            parameter.update(arguments)
        return parameter

    def create_base_url(self, function, parameter):
        """Create the base URL with parameters

        Keyword arguments:
        function -- The function/address to query on the host
        parameter -- A dict with all parameters to append on the URL
        """
        enc_param = urllib.urlencode(parameter)
        return "http://%s%s?%s" % (self._host, function, enc_param)

    def create_signed_url(self, base_url):
        """Create the signed URL with hmac

        Keyword arguments:
        base_url -- The base URL from create_base_url()
        """
        return "%s-%s" % (base_url, HMAC(self._api_key, base_url, sha1).hexdigest())

    def status_check(self):
        """Checks if everything is working as it should be"""
        arg = {
            "date": "",
            "location": "",
            "app_version": "1.1",
            "count": "1",
            "device_model": "1",
            "system_name": "iPhone OS",
            "system_version": "3.1.2"
        }
        js = self.make_request('/hello', arg)
        # Returned status should be 'ok', or there was an error
        status = js["data"]["status"]
        if status != "ok":
            raise ImdbRequestError(
                "Status check did not return 'ok', was %r" % (status))

    def make_request(self, function, arguments = None):
        """Send the request to the host and return the JSON

        Keyword arguments:
        function -- The function/address to query on the host
        arguments -- A dict with arguments to append the request
        """
        # Build the URL and request it
        parameter = self.create_parameters(arguments)
        base_url = self.create_base_url(function, parameter)
        signed_url = self.create_signed_url(base_url)
        request = urllib2.Request(signed_url)
        # Set the HTTP User-Agent header to Safari's so IMDb won't block the request.
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7')
        opener = urllib2.build_opener()
        json_string = opener.open(request).read()
        # Make sure the JSON string can be decoded
        data = json.loads(json_string, 'utf-8')
        if data is False:
            raise ImdbRequestError('Could not parse the JSON string')
        return data
