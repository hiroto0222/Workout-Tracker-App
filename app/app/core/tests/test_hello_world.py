from django.test import TestCase


class HelloWorldTestCase(TestCase):
    def test_hello_world(self):
        msg = "Hello World!"
        self.assertEqual(msg, "Hello World!")
