from algorithms.algorithm import Algorithm
from typing import Literal, Protocol, Callable
import random
from math import gcd
from sympy import isprime
from algorithms.ClassicalAlgorithms.order_finding_brute_force import OrderFindingClassical
from algorithms.QuantumAlgorithms.order_finding_quantum import OrderFindingQuantum
from functools import lru_cache


order_finding = {
    'classical': OrderFindingClassical.find_order,
    "quantum": OrderFindingQuantum.find_order
}

OrderFindingType = Literal['classical', 'quantum']


@lru_cache()
def find_factors(k: int, order_finding_type: OrderFindingType = 'classical', verbose: bool = False,) -> list[int]:
    if order_finding_type not in order_finding.keys():
        raise ValueError('Invalid order finding type! Specify either classical or quantum')

    find_order: Callable[[int, int], int] = order_finding[order_finding_type]
    factors: list[int] = []
    while k != 1:
        if isprime(k):
            factors.append(k)
            break
        x = random.randint(2, k - 1)
        if gcd(x, k) > 1:
            factors.append(gcd(x, k))
            k = k // gcd(x, k)
            continue
        else:
            r = find_order(x, k)
            if r % 2 == 1 or x ** (r // 2) % k == -1:
                continue
        f_plus = gcd(int(x ** (r // 2) + 1), k)
        f_minus = gcd(int(x ** (r // 2) - 1), k)

        if f_plus != 1 and f_plus != k:
            factors.append(f_plus)
            k = k // f_plus
            continue

        elif f_minus != 1 and f_minus != k:
            factors.append(f_minus)
            k = k // f_minus
            continue
        if verbose:
            print(k)
    return factors




class FactorShor(Algorithm):
    """
    This class implements Shor's algorithm for factoring integers.
    """

    def __init__(self, name: str, N: int, order_finding_type: OrderFindingType = 'classical'):
        super().__init__(name)
        self.N: int = N
        self.factors: list = []
        self.type: OrderFindingType = order_finding_type


    def run(self):
        factors = find_factors(self.N)
        all_primes = False
        while not all_primes:
            all_primes = True
            f = []
            for factor in factors:
                if not isprime(factor):
                    all_primes = False
                    # add factors of factors[i] to factors
                    f.extend(find_factors(factor))
                else:
                    f.append(factor)
            factors = f
        self.factors = factors




    def plot(self):
        print(f'The factors of {self.N} are {self.factors}')













