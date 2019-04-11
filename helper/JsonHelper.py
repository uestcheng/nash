#-*- coding:utf -*-


class Stack(object):
    """Stack implementation 
       store different pack    
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.stack = []

    def append(self, item):
        self.stack.append(item)

    def __repr__(self):
        __str = ''
        for i in stack:
            __str += i
        return __str


class StackItem(object):
    """stack item implementation"""

    def __init__(self, reason, expected, actual):
        self.reason = reason
        self.expected = expected
        self.actual = actual
