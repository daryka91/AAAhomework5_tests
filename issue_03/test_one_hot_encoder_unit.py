from one_hot_encoder import fit_transform
import unittest

class TestOneHotEncoder(unittest.TestCase):
    def test_equal(self):
        actual = fit_transform('Moscow', 'New York', 'Moscow', 'London')
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [0, 1, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_not_equal(self):
        actual = fit_transform('Moscow', 'New York', 'Moscow', 'London')
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [0, 0, 1]),
        ]
        self.assertNotEqual(actual, expected, "Function doesn't work properly")

    def test_correct_input(self):
        input = 123
        self.assertRaises(TypeError, fit_transform, input)


    def test_empty(self):
        actual = fit_transform('')
        expected = [('', [1])]
        self.assertEqual(actual, expected)


