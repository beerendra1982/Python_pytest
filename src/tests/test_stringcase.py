import pytest



# class TestStringMethods(unittest.TestCase):

def test_camelcase():
    from main.stringcase import to_camel_case
    expected_result = "BeeruIAmHere"
    result = to_camel_case("Beeru i am here")
    assert( expected_result , result)

def test_camelcaseNegative():
    from main.stringcase import to_camel_case
    expected_result = ""
    result = to_camel_case("")
    assert( expected_result , result)


def test_isBlanlTrue():
    from main.stringcase import isBlank
    result = isBlank("")
    assert(result,True)


def test_isBlanlFalse():
    from main.stringcase import isBlank
    result = isBlank("Beeru")
    assert(result,True)

def test_c():
    from main.stringcase import upper
    result = upper("Beeru")
    expected_result = "BEERU"
    assert( expected_result , result)


