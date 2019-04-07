#-*-coding:utf-8 -*-

import requests

class APIHelper(object):
    """basic apihelper function"""

    def __init__(self):
        self.s = requests.Session()