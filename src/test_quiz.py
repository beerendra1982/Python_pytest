import unittest
import quiz

class test_quize(unittest.TestCase):
    def test_fize(self):
        expected_Retuls="fizz"
        actual_Result= quiz.validation(3)
        print(actual_Result)
        assert expected_Retuls==actual_Result

