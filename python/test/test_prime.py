import unittest
import rsa.prime as prime


class TestSimplePrimeTest(unittest.TestCase):
    def test_not_prime(self):
        result = prime.simple_prime_test(323)
        self.assertFalse(result)

    def test_prime_19(self):
        result = prime.simple_prime_test(19)
        self.assertTrue(result)

    def test_prime_23(self):
        result = prime.simple_prime_test(23)
        self.assertTrue(result)


class TestFermiPrimeTest(unittest.TestCase):
    def test_prime_17(self):
        result = prime.fermi_prime_test(17)
        self.assertTrue(result)

    def test_not_prime_21(self):
        result = prime.fermi_prime_test(21)
        self.assertFalse(result)

    def test_prime_1223(self):
        result = prime.fermi_prime_test(1223)
        self.assertTrue(result)

    def test_prime_1225(self):
        result = prime.fermi_prime_test(1225)
        self.assertFalse(result)

    def test_prime(self):
        data = [
            (17, True),
            (19, True),
            (23, True),
            (25, False),
            (97, True),
            (1181, True),
            (1201, True),
            (1217, True),
            (1219, False),
        ]
        for i, expected in data:
            result = prime.fermi_prime_test(i)
            self.assertEqual(expected, result, f"{i}, expected: {expected}, result: {result}")


class TestGeneratePrimeNumber(unittest.TestCase):
    def test_generate_prime_number(self):
        for _ in range(3):
            result = prime.generate_prime_number(16)
            self.assertTrue(prime.is_prime(result))
