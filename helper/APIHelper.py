#-*-coding:utf-8 -*-

import os
import yaml
import requests

class APIHelper(object):
    """basic apihelper function"""

    def __init__(self, env='QA'):
        self.s = requests.Session()
        data = os.path.join(os.path.dirname(os.path.abspath(__file__), 'data.yml')
        self.url = data[env]

    def _get(self, uri, *args, **kwargs):
        res = self.s.get("{}/{}".format(self.url, uri), *args, **kwargs)
        return res

    def _post(self, uri, *args, **kwargs):
        res = self.s.post("{}/{}".format(self.url, uri), *args, **kwargs)
        return res

    def _put(self, uri, *args, **kwargs)

        
