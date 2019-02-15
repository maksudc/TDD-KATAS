from unittest import TestCase
from roman_numerals.services import RomanToDecimalService


class TestRomanToDecimal(TestCase):

    def setUp(self):
        super(TestRomanToDecimal, self).setUp()

    def test_get_one(self):

        service = RomanToDecimalService()
        assert service.convert(1) == 'I'

    def test_get_five(self):

        service = RomanToDecimalService()
        assert service.convert(5) == 'V'

    def test_get_direct_symbols(self):

        service = RomanToDecimalService()
        assert service.convert(10) == 'X'
        assert service.convert(50) == 'L'
        assert service.convert(100) == 'C'
        assert service.convert(500) == 'D'
        assert service.convert(1000) == 'M'

    def test_get_within_five(self):

        service = RomanToDecimalService()

        assert service.convert(2) == "II"
        assert service.convert(3) == "III"
        assert service.convert(4) == "IV"

    def test_get_within_10(self):

        service = RomanToDecimalService()
        assert service.convert(6) == "VI"
        assert service.convert(8) == "VIII"
        assert service.convert(9) == 'IX'
        assert service.convert(10) == "X"

    def test_get_within_50(self):

        service = RomanToDecimalService()
        assert service.convert(30) == "XXX"
        assert service.convert(35) == "XXXV"
        assert service.convert(40) == 'XL'
        assert service.convert(45) == "XLV"
        assert service.convert(50) == "L"

    def test_get_within_100(self):

        service = RomanToDecimalService()
        assert service.convert(55) == "LV"
        assert service.convert(70) == "LXX"
        assert service.convert(79) == 'LXXIX'
        assert service.convert(89) == "LXXXIX"
        assert service.convert(90) == "XC"

    def test_get_within_500(self):

        service = RomanToDecimalService()
        assert service.convert(120) == "CXX"
        assert service.convert(140) == "CXL"
        assert service.convert(150) == "CL"
        assert service.convert(340) == 'CCCXL'
        assert service.convert(400) == 'CD'
        assert service.convert(440) == "CDXL"
        assert service.convert(490) == "CDXC"

    def test_get_within_1000(self):

        service = RomanToDecimalService()
        assert service.convert(678) == "DCLXXVIII"
        assert service.convert(800) == "DCCC"
        assert service.convert(840) == "DCCCXL"
        assert service.convert(900) == "CM"
        assert service.convert(990) == "CMXC"

    def tearDown(self):
        super(TestRomanToDecimal, self).tearDown()

