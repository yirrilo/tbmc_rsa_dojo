from typing import Tuple, List


class Rsa:
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
        raise NotImplementedError()

    def generate_keys(self, p: int, q: int, e: int) -> None:
        self.e = e
        raise NotImplementedError()

    def encrypt(self, plaintext: str) -> List[int]:
        raise NotImplementedError()

    def decrypt(self, ciphered_text: List[int]) -> str:
        raise NotImplementedError()
