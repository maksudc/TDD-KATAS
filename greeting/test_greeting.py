from unittest import TestCase

class TestGreet(TestCase):

    def setUp(self):
        super(TestGreet, self).setUp()

    def test_hello(self):
        greet("Maksud")

    def tearDown(self):
        super(TestGreet, self).tearDown()

