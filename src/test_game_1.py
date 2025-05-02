import pytest
import gamequiz


def test_quiz2():
    expected_Retuls="15 can be divided by 3 and 5"
    actual_Result= gamequiz.validateion(15)
    # print(actual_Result)
    assert expected_Retuls==actual_Result


def test_quiz():
    expected_Retuls="3 can be divided by 3"
    actual_Result= gamequiz.validateion(3)
    assert expected_Retuls==actual_Result

