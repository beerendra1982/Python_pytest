import unittest
import quize

class test_quize(unittest.TestCase):
    def test_fize(self):
        expected_Retuls="fizz"
        actual_Result=quize.validation(3)
        print(actual_Result)
        assert expected_Retuls==actual_Result

