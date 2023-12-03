import pytest
import unittest


class TestStringMethods(unittest.TestCase):

    def test_camelcase(self):
        from main.stringcase import to_camel_case
        expected_result = "BeeruIAmHere"
        result = to_camel_case("Beeru i am here")
        self.assertEqual( expected_result , result)

    def test_camelcaseNegative(self):
        from main.stringcase import to_camel_case
        expected_result = ""
        result = to_camel_case("")
        self.assertEqual( expected_result , result)


    def test_isBlanlTrue(self):
        from main.stringcase import isBlank
        result = isBlank("")
        self.assertTrue(result)


    def test_isBlanlFalse(self):
        from main.stringcase import isBlank
        result = isBlank("Beeru")
        self.assertFalse(result)
