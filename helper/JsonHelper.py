<<<<<<< HEAD
#-*- coding:utf-8 -*-


class Stack(object):
    """Stack implementation"""
=======
#-*- coding:utf -*-


class Stack(object):
    """Stack implementation 
       store different pack    
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

>>>>>>> 9a9f63ba265cb76be8d77c17601f3ec4f8fe725d
    def __init__(self):
        self.stack = []

    def append(self, item):
        self.stack.append(item)

    def __repr__(self):
<<<<<<< HEAD
        _str = ""
        for i in self.stack:
            _str += str(i) 
        return _str
    

class Item(object):
    """stack item implementation"""
    def __init__(self, reason, expected, actual):
        self.reason = reason

    def __repr__(self):
        _str = 
        for s in self.reason:
            _str += s

        return 'Reason:{}\n'.format(
            _str,
        )

def _is_dict_same(expected, actual, ignore_value_of_keys, ignore_missing_keys):
    if ignore_missing_keys:
        if len(expected.keys()) > len(actual.keys()):
            return False, Stack().append(Item(
                    "Keys Mismatch: {0} keys are mismatch".format(
                    list(set(expected.keys()) ^ set(actual.keys()))
                    )
                ))
    else:
        if len(expected.keys()) != len(actual.keys()):
            return False, Stack().append(Item(
                    "Keys Mismatch: {0} keys are mismatch".format(
                        list(set(expected.keys()) ^ set(actual.keys()))
                    )
                ))
    is_same_flag, stack = _is_same(expected, actual, ignore_value_of_keys, ignore_missing_keys)
    return is_same_flag, stack()
    
def _is_same(expected, actual, ignore_value_of_keys=True, ignore_missing_keys=False):
    if expected is None or type(expected) in (int, bool, str, float):
        return expected == actual, Stack()

    if type(exected) != type(actual):
        return False, Stack().append(Item(
            'Type Mismatch: Expected Type: {0}, Actual Type: {1}'
                                .format(type(expected), type(actual)),
            ))
    if isinstance(expected, dict):
        _is_dict_same(expected, actual, ignore_value_of_keys, ignore_missing_keys):
    
    if isinstance(expected, list):
        pass



   

    
        
=======
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
>>>>>>> 9a9f63ba265cb76be8d77c17601f3ec4f8fe725d
