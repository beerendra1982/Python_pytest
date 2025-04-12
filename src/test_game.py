import unittest
import gamequiz

class test_game1(unittest.TestCase):
    def test_quiz(self):
        expected_Retuls="3 can be divided by 3"
        actual_Result= gamequiz.validateion(3)
        print(actual_Result)
        assert expected_Retuls==actual_Result

    def test_quiz2(self):
        expected_Retuls="15 can be divided by 3 and 5"
        actual_Result= gamequiz.validateion(15)
        print(actual_Result)
        assert expected_Retuls==actual_Result

    def test_quiz3(self):
        expected_Retuls="5 can be divided by 5"
        actual_Result= gamequiz.validateion(5)
        print(actual_Result)
        assert expected_Retuls==actual_Result

    def test_quiz4(self):
        expected_Retuls="4 can't be divided by 3 or 5"
        actual_Result= gamequiz.validateion(4)
        print(actual_Result)
        assert expected_Retuls==actual_Result



