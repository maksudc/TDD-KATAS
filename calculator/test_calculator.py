from unittest import TestCase
from .services import Calculator

class TestCalculator(TestCase):

    def setUp(self):
        super(TestCalculator, self).setUp()

    def test_add_empty(self):

        calculator = Calculator()
        assert calculator.add("") == 0

    def test_add_single_number(self):

        calculator = Calculator()
        assert calculator.add("2") == 2

    def test_add_multiple_number(self):

        calculator = Calculator()
        assert calculator.add("2,3,4,5,6") == 20

    def test_add_newline_separated_number(self):

        calculator = Calculator()
        assert calculator.add("1\n2,3") == 6

    def test_invalid_newline_separated_number(self):
        calculator = Calculator()

        with self.assertRaises(Exception):
            calculator.add("1,\n2,3")

    def test_default_delimeter_beginning(self):
        calculator = Calculator()
        assert calculator.add("//;\n1;2") == 3

    def test_raises_exception_on_negative_number(self):

        calculator = Calculator()
        with self.assertRaises(Exception):
            calculator.add("-1,1,-3,4")

    def test_numbers_bigger_than_1000(self):

        calculator = Calculator()
        assert calculator.add("2,1001, 3") == 5

    def test_multiple_length_delimeter(self):

        calculator = Calculator()
        assert calculator.add("//***\n1***2***3") == 6

    def tearDown(self):
        super(TestCalculator, self).tearDown()