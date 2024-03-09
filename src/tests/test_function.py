# import unittest
import pytest

def test_average():
    from main.function import average
    result = average(10,20)
    expectedResult=15
    assert(expectedResult,result)

def test_addition():
    from main.function import addition
    result = addition(10,20)
    expectedResult=30
    assert (expectedResult,result)

def test_sumOfNumber():
    from main.function import sumOfNumber
    result = sumOfNumber(1,2,3,4,5)
    expectedResult = 15
    assert(expectedResult,result)

