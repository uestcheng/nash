# -*- coding:utf-8 -*-


class Logger(object):
    """Logger class"""
    def __init__(self):
        self.FORMAT = "%(asctime)-15s %(levelno)s %(user)-8s %(message)s'"

    @staticmethod
    def log_info(message):
        """:param: message is the string which is output in console"""
        print(message)

    @staticmethod
    def log_error(message):
        raise Exception(message)