import math
import random


def simple_prime_test(n: int) -> bool:
    for i in [2, 3, 5, 7, 11, 13, 17, 19]:
        if n != i and n % i == 0:
            return False
    return True


def fermi_prime_test(n: int, k: int = 10) -> bool:
    for i in range(k):
        a = random.randrange(2, n - 2)
        if a ** (n - 1) % n != 1:
            return False
    return True


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 2, 2):
        if num % i == 0:
            return False
    return True


def __generate_prime_number_candidate(length: int) -> int:
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length: int) -> int:
    p = 12
    while not fermi_prime_test(p) or not simple_prime_test(p):
        p = __generate_prime_number_candidate(length)
    return p
