import unittest
import pytest

class TestFunction(unittest.TestCase):
    def test_average(self):
        from main.function import average
        result = average(10,20)
        expectedResult=15
        self.assertEqual(expectedResult,result)
