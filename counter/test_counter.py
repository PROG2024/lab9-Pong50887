"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest

from counter import Counter


class testCounter(unittest.TestCase):

    def test_share_count(self):
        counter = Counter()
        self.assertEquals(counter.count, 0)
        counter.increment()
        counter.increment()
        counter1 = Counter()
        self.assertEquals(counter1.count, 1)
        