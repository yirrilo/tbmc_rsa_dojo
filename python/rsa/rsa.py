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

    def __modinv(self, a: int, b: int) -> int:
        a = a % b
        for i in range(1, b):
            if (a * i) % b == 1:
                return i
        return 1

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
