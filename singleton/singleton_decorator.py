#---------coding:utf8---------------

"""
file name: singleton_decorator
author: Zhao Ying
email: zhaoying612@gmail.com
create time: 9/17/17 17:09

使用装饰器实现单例
reference: https://wiki.python.org/moin/PythonDecoratorLibrary#Singleton
"""

import functools

def singleton(cls):
    ''' Use class as singleton. '''

    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kw):
        it =  cls.__dict__.get('__it__')
        if it is not None:
            return it

        cls.__it__ = it = cls.__new_original__(cls, *args, **kw)
        it.__init_original__(*args, **kw)
        return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__

    return cls

#
# Sample use:
#

@singleton
class Foo(object):
    def __new__(cls):
        cls.x = 10
        return object.__new__(cls)

    def __init__(self):
        assert self.x == 10
        self.x = 15


#TODO: 从官网copy的,但是运行时会报错,待排查
if __name__ == '__main__':
    assert Foo().x == 15
    Foo().x = 20
    assert Foo().x == 20