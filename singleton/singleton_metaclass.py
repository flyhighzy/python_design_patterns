#---------coding:utf8---------------

"""
file name: singleton_metaclass
author: Zhao Ying
email: zhaoying612@gmail.com
create time: 9/17/17 18:48

use metaclass to implement Singleton
preferred!
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
class MyClass(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.x = 10

#Python3
#class MyClass(object, metaclass=Singleton):
#    pass

if __name__ == '__main__':
    e1 = MyClass()
    e2 = MyClass()
    print e1, e2
    e1.x = 20
    print e1.x, e2.x

