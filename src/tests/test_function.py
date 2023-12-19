import unittest
import pytest

class TestFunction(unittest.TestCase):
    def test_average(self):
        from main.function import average
        result = average(10,20)
        expectedResult=15
        self.assertEqual(expectedResult,result)

    def test_addition(self):
        from main.function import addition
        result = addition(10,20)
        expectedResult=30
        self.assertEqual(expectedResult,result)

    def test_sumOfNumber(self):
        from main.function import sumOfNumber
        result = sumOfNumber(1,2,3,4,5)
        expectedResult = 15
        self.assertEqual(expectedResult,result)

