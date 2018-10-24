import unittest
from HelloWorld import HelloWorld
class TestCase(unittest.TestCase):
    def test_default_hello(self):
        hello = HelloWorld()
        self.assertEqual(hello.message, 'Hello World')

if __name__ == '__main__':
    unittest.main()
