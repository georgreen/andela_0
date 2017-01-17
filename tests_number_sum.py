import unittest

from number_sum import add_sum

class test_number_sum(unittest.TestCase):
    def setUp(self):
        pass

    #passing tests
    def test_sumPositive(self):
        self.assertEqual(add_sum(5), 15)
        self.assertEqual(add_sum(20), 210)
        self.assertEqual(add_sum(1), 1)

    def test_sumNegative(self):
        self.assertEqual(add_sum(-5), (-5 * (-5 + 1)) / 2)
        self.assertEqual(add_sum(-20), (-20 * (-20 + 1)) / 2)
        self.assertEqual(add_sum(-1), (-1 * (-1 + 1)) / 2)

    def test_nonIntegers(self):
        with self.assertRaises(TypeError):
            add_sum("String")

    def test_veryLargeIntergers(self):
        self.assertEqual(add_sum(65536*65536),  (65536*65536 * (65536*65536 + 1))/2)

    def test_verysmallInterger(self):
        self.assertEqual(add_sum(-65536*65536), (-65536*65536 * (-65536*65536 + 1))/2)

    def test_EdgeCase_zero(self):
        self.assertEqual(add_sum(0), 0)

if __name__ == '__main__':
    unittest.main()
