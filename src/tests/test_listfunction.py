import pytest
import unittest


class MyTestCase(unittest.TestCase):
    def test_minNumber(self):
        from main.listfunction import minNumber
        result=minNumber([1,5,3,0])
        expectedResult=0
        self.assertEqual(result, expectedResult)

    def test_maxNumber(self):
        from main.listfunction import maxNumber
        result=maxNumber([1,5,3,0])
        expectedResult=5
        self.assertEqual(result, expectedResult)

    def test_evenNumberList(self):
        from main.listfunction import evenNumberList
        result =evenNumberList([1,2,3,4,5,6])
        expectedResult=[2,4,6]
        self.assertEqual(result, expectedResult)