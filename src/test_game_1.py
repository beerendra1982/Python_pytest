import pytest
import gamequiz


def test_quiz2():
    expected_Retuls="15 can be divided by 3 and 5"
    actual_Result= gamequiz.validateion(151)
    # print(actual_Result)
    assert expected_Retuls==actual_Result

