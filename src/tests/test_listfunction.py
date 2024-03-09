import pytest

def test_minNumber():
    from main.listfunction import minNumber
    result=minNumber([1,5,3,0])
    expectedResult=0
    assert(result, expectedResult)

def test_maxNumber():
    from main.listfunction import maxNumber
    result=maxNumber([1,5,3,0])
    expectedResult=5
    assert(result, expectedResult)

def test_evenNumberList():
    from main.listfunction import evenNumberList
    result =evenNumberList([1,2,3,4,5,6])
    expectedResult=[2,4,6]
    assert(result, expectedResult)