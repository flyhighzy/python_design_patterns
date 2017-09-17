#---------coding:utf8---------------

"""
file name: singleton_new
author: Zhao Ying
email: zhaoying612@gmail.com
create time: 9/17/17 16:22

使用 __new__实现单例
"""


import threading


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        lock = threading.Lock()
        if cls.__instance is None:
            with lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton, cls).__new__(cls, args, kwargs)
        return cls.__instance

    def __init__(self):
        self.name = "Zhaoying"

    def do_something(self):
        pass


def worker():
    e = Singleton()
    print id(e)
    e.do_something()


if __name__ == '__main__':
    e1 = Singleton()
    e2 = Singleton()
    print e1
    print e2
    e1.name = "test"
    print e1.name
    print e2.name


    task = []
    for one in range(30):
        t = threading.Thread(target=worker)
        task.append(t)

    for one in task:
        one.start()

    for one in task:
        one.join()




