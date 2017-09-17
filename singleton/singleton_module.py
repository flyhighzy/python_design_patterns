#---------coding:utf8---------------

"""
file name: singleton_module.py
author: Zhao Ying
email: zhaoying612@gmail.com
create time: 2017-09-17 16:16
"""


# 使用模块实现单例的例子.模块是天然的单例, 但不推荐使用

class My_Singleton(object):
    def foo(self):
        pass


my_instance = My_Singleton()

