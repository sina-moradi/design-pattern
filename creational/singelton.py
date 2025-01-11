from typing import Any


class Singleton(type):
    _instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._instance is None:
            self._instance = super().__call__(*args, **kwds)

        return self._instance


class SingletonClass(object):
    def __new__(cls, *name, **table):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class Db(metaclass=SingletonClass):
    def __init__(self, name, table) -> None:
        self.name = name
        self.table = table
