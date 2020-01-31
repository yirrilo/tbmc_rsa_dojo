from typing import Tuple, List


class Rsa:
    p: int
    q: int
    e: int
    n: int
    d: int
    phi: int

    @property
    def public_key(self):
        return self.e, self.n

    @property
    def private_key(self):
        return self.d, self.n

    def __egcd(self, a: int, b: int) -> Tuple[int, int, int]:
        """
        Compute the extended euclidean algorithm
        :param a:
        :param b:
        :return: gcd, u, v
        """
        if a == 0:
            return b, 0, 1
        gcd, u, v = self.__egcd(b % a, a)
        return gcd, v - (b // a) * u, u

    def __modinv(self, a: int, b: int) -> int:
        gcd, u, v = self.__egcd(a, b)
        if gcd != 1:
            raise ValueError("Module inverse doesn't exist")
        return u % b

    def generate_keys(self, p: int, q: int, e: int) -> None:
        self.p = p
        self.q = q
        self.e = e
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.d = self.__modinv(e, self.phi)
        if self.phi % e == 0:
            raise ValueError("Invalid values for p and q")

    def encrypt(self, plaintext: str) -> List[int]:
        e, n = self.public_key
        cipher = [
            pow(ord(char), e, n)
            for char in plaintext
        ]
        return cipher

    def decrypt(self, ciphered_text: List[int]) -> str:
        d, n = self.private_key
        plain = [
            chr(pow(char, d, n))
            for char in ciphered_text
        ]
        return ''.join(plain)
