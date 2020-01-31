import unittest
from python.rsa import rsa as rsa


class TestRsaEncryptDecrypt(unittest.TestCase):
    p = 11
    q = 13
    e = 7
    rsa: rsa.Rsa

    def setUp(self) -> None:
        self.rsa = rsa.Rsa()
        self.rsa.generate_keys(self.p, self.q, self.e)

    def test_egcd_120_23(self):
        a = 120
        b = 23
        gcd, u, v = self.rsa._Rsa__egcd(a, b)
        self.assertEqual(gcd, a * u + b * v)
        self.assertEqual(gcd, 1)
        self.assertEqual(u, -9)
        self.assertEqual(v, 47)

    def test_egcd_240_46(self):
        result = self.rsa._Rsa__egcd(240, 46)
        self.assertEqual(result, (2, -9, 47))

    def test_modinv_120_23(self):
        result = self.rsa._Rsa__modinv(120, 23)
        self.assertEqual(14, result)

    def test_modinv_240_46(self):
        a = 240
        b = 46
        self.assertRaises(ValueError, lambda: self.rsa._Rsa__modinv(a, b))

    def test_generate_keys(self):
        self.assertEqual(self.rsa.private_key, (103, 143))
        self.assertEqual(self.rsa.public_key, (7, 143))

    def test_encrypt(self):
        text = "my text"
        ciphered = self.rsa.encrypt(text)
        self.assertEqual([21, 121, 98, 129, 62, 120, 129], ciphered)

    def test_decrypt(self):
        ciphered = [21, 121, 98, 129, 62, 120, 129]
        plaintext = self.rsa.decrypt(ciphered)
        self.assertEqual("my text", plaintext)

    def test_encrypt_decrypt(self):
        text = "my_text"
        ciphered = self.rsa.encrypt(text)
        plaintext = self.rsa.decrypt(ciphered)
        self.assertEqual(text, plaintext)
