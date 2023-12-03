import pytest
import unittest

from main.stringcase import to_camel_case

class TestStringMethods(unittest.TestCase):

    def test_camelcase(self):
        expected_result = "BeeruIAmHere"
        result = to_camel_case("Beeru i am here ")
        self.assertEqual( expected_result , result)
