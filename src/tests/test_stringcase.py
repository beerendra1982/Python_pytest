import pytest

from main.stringcase import to_camel_case


def test_camelcase():
    expected_result = "BeeruIAmHere"
    result = to_camel_case("Beeru i am here ")
    assert expected_result == result
