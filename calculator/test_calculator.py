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

    def tearDown(self):
        super(TestCalculator, self).tearDown()