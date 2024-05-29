import unittest

class test_function(unittest.TestCase):
    def test_average(self):
        from function import average
        result = average(10,20)
        expectedResult=15
        assert(expectedResult,result)

    def test_addition(self):
        from function import addition
        result = addition(10,20)
        expectedResult=30
        assert (expectedResult,result)

    def test_sumOfNumber(self):
        from function import sumOfNumber
        result = sumOfNumber(1,2,3,4,5)
        expectedResult = 15
        assert(expectedResult,result)

