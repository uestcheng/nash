#-*-coding:utf-8 -*-

import os
import yaml
import requests

from logger import Logger

class APIHelper(object):
    """basic apihelper function"""

    def __init__(self, env='QA'):
        self.s = requests.Session()
        data = os.path.join(os.path.dirname(os.path.abspath(__file__), 'data.yml')
        self.url = data[env]

    def _get(self, uri, *args, **kwargs):
        """get response.
        :param url: URL for new response
        :param params: (Optional)dictionary, list of parames to send in 
        the query string.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body request. 
        :param headers: (optional) Dictionary of HTTP Headers to send with request
        :param cookies: (optional) Dict or CookieJar object to send with request
        :param verify: (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to ``True``.
        """
        res = self.s.get("{}/{}".format(self.url, uri), *args, **kwargs)
        return res

    def _post(self, uri, *args, **kwargs):
        """POST method"""
        res = self.s.post("{}/{}".format(self.url, uri), *args, **kwargs)
        return res

    def _put(self, uri, *args, **kwargs):
        """put method"""
        res = self.s.put("{}/{}".format(self.url, uri), *args, **kwargs)
        return res

    def _del(self, uri, *args, **kwargs):
        """delete method"""
        res = self.s.delete("{}/{}".format(self.url, uri), *args, **kwargs)
        return res

    def send_request(method, url, *args, **kwargs):
        return getattr(self.s, '_{}'.format(method))(*args, **kwargs)

    @classmethod
    def json_compare(actual, exception):
        """compare two dictionary"""
        pass

    def _simply_dictionary_structure(obj):
        """iterate all the schema of obj, replace all the values to a symbol"""
        if isinstance(obj, dict):
            for k, v in obj.items():
                _simply_dictionary_structure(v)
        if isinstance(obj, list):
            obj = [obj[0]]
            _simply_dictionary_structure(obj[0])
        if isinstance(obj, str):
            obj = "str"
        if isinstance(obj, (int, float)):
            obj = "numeric"
            
