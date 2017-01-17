import unittest

from primeNumber import primeNumber_generator

class test_primeNumber_generator(unittest.TestCase):
    #passing tests
    def test_primein_0_t0_positiveInt(self):
        pass

    def test_primein_0_to_largePosInt(self):
        pass

    def test_primein_0_to_negativeInt(self):
        pass

    def test_NonInteger_input(self):
        pass

    def test_inclusiveRange_0_to_prime(self):
        pass

    def test_nonInclusiveRange_0_to_nonPrime(self):
        pass

    def test_EdgeCase_Zero(self):
        pass

    #Failing tests
    def test_wrongAnswer1_0_to_10(self):
        pass
    def test_wrongAnswer2_0_to_neg20(self):
        pass
    def test_wrongAnswer3_NonInt_Input(self):
        pass

if __name__ == '__main__':
    unittest.main()
