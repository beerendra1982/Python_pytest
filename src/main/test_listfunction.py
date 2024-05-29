import unittest

class test_listfunction(unittest.TestCase):
    def test_minNumber(self):
        from listfunction import minNumber
        result=minNumber([1,5,3,0])
        expectedResult=0
        assert(result, expectedResult)

    def test_maxNumber(self):
        from listfunction import maxNumber
        result=maxNumber([1,5,3,0])
        expectedResult=5
        assert(result, expectedResult)

    def test_evenNumberList(self):
        from listfunction import evenNumberList
        result =evenNumberList([1,2,3,4,5,6])
        expectedResult=[2,4,6]
        assert(result, expectedResult)