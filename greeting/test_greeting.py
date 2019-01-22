from unittest import TestCase
from greeting.services import greet

class TestGreet(TestCase):

    def setUp(self):
        super(TestGreet, self).setUp()

    def test_hello(self):
        assert greet("Maksud") == "Hello, Maksud."

    def test_null(self):
        assert greet(None) == "Hello, my friend."

    def test_shouting_when_name_uppercase(self):
        assert greet("MAKSUD") == "HELLO MAKSUD!"

    def test_concat_array_of_names(self):
        assert greet(["Maksud", "Zimi"]) == "Hello, Maksud and Zimi."

    def test_concat_array_of_arbitrary_names(self):
        assert greet(["Maksud", "Zimi", "Robert", "Tanvir", "Musa"]) == "Hello, Maksud, Zimi, Robert, Tanvir, and Musa."


    def tearDown(self):
        super(TestGreet, self).tearDown()

