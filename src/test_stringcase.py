import unittest

class test_stringcase(unittest.TestCase):
    def test_camelcase(self):
        from stringcase import to_camel_case
        expected_result = "BeeruIAmHere"
        result = to_camel_case("Beeru i am here")
        assert( expected_result , result)

    def test_camelcaseNegative(self):
        from stringcase import to_camel_case
        expected_result = ""
        result = to_camel_case("")
        assert( expected_result , result)


    def test_isBlanlTrue(self):
        from stringcase import isBlank
        result = isBlank("")
        assert(result,True)


    def test_isBlanlFalse(self):
        from stringcase import isBlank
        result = isBlank("Beeru")
        assert(result,True)

    def test_c(self):
        from stringcase import upper
        result = upper("Beeru")
        expected_result = "BEERU"
        assert( expected_result , result)

    def test_stringslice(self):
        from stringcase import stringslice
        result = stringslice("Beeru",1)
        expected_result = "BEERU"
        print( result)
        # assert( expected_result , result)



