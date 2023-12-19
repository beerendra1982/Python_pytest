import pytest
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from main.listfunction import minNumber
        result=minNumber([1,5,3,0])
        expectedResult=0
        self.assertEqual(result, expectedResult)

