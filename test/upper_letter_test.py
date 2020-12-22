import unittest

from src.cal_math import cal_sin


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_upper(self):
        self.assertEqual('cc'.upper(), 'CC')

    def test_isupper(self):
        self.assertTrue('CC'.isupper())
        self.assertFalse('Cc'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_math(self):
        y = cal_sin(1.57079632729)
        self.assertAlmostEqual(y, 1)


if __name__ == '__main__':
    unittest.main()
