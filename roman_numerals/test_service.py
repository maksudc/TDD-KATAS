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

    def tearDown(self):
        super(TestRomanToDecimal, self).tearDown()

