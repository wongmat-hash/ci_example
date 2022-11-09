import unittest
from task import my_func


class TestCase(unittest.TestCase):

	def test1(self):
        expected = "Hello World"
        self.assertEqual(my_func(), expected)

    def test2(self):
        expected = "Goodbye World"
        self.assertNotEqual(my_func(), expected)


if __name__ == '__main__':
    unittest.main()
