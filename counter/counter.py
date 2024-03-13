"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    """
    >>> counter = Counter()
    >>> counter.count
    0
    >>> counter.count
    0
    >>> counter.increment()
    >>> counter.count
    1
    >>> counter2 = Counter()
    >>> counter2 is counter
    True
    >>> counter2.count
    1
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return
        self._initialized = True
        self.__count = 0

    def __str__(self):
        return f"{self.__count}"

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1
