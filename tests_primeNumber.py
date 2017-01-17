import unittest

from primeNumber import primeNumber_generator

class test_primeNumber_generator(unittest.TestCase):
    def setUp(self):
        pass

    #passing tests
    def test_primein_0_t0_positiveInt(self):
        self.assertEqual(primeNumber_generator(10), [2, 3, 5,7])

    def test_primein_0_to_largePosInt(self):
        self.assertEqual(primeNumber_generator(1000),([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149
, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311
, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487
, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673
, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877
, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]))

    def test_primein_0_to_negativeInt(self):
        with self.assertRaises(TypeError):
            primeNumber_generator(-20)

    def test_NonInteger_input(self):
        with self.assertRaises(TypeError):
            primeNumber_generator([])

    def test_inclusiveRange_0_to_prime(self):
        self.assertEqual(primeNumber_generator(13) ,[2, 3, 5, 7, 11, 13])

    def test_nonInclusiveRange_0_to_nonPrime(self):
        self.assertTrue(primeNumber_generator(20) == [2, 3, 5, 7, 11, 13, 17, 19])

    def test_EdgeCase_Zero(self):
        self.assertEqual(primeNumber_generator(0), [])

    #Evaluate to false
    def test_wrongAnswer1_0_to_10(self):
        self.assertFalse(primeNumber_generator(10) == [1, 2, 4])

    def test_wrongAnswer2_0_to_neg20(self):
        self.assertFalse(primeNumber_generator(25) == [0, 0, 0, 5])

    def test_wrongAnswer3_NonInt_Input(self):
        self.assertFalse(primeNumber_generator(0) == [1, 3, 7])

if __name__ == '__main__':
    unittest.main()
