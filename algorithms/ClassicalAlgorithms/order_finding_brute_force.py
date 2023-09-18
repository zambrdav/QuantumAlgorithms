import numpy as np
from algorithms.algorithm import Algorithm



def _are_coprime(a: int, b: int) -> bool:
    return np.gcd(a, b) == 1



class OrderFindingClassical(Algorithm):

    def __init__(self, name: str, a: int, N: int):
        super().__init__(name)
        self.a: int = a
        self.N: int = N
        self.type = "classical"
        self.order = None

    def run(self):
        self.order = self.find_order(self.a, self.N)




    @staticmethod
    def find_order(a, N):
        if not _are_coprime(a, N):
            raise ValueError('a and N are not coprime!')
        r: int = 1
        while (a ** r) % N != 1:
            r += 1
        return r




    def plot(self):
        if self.order is None:
            raise ValueError('Please run the algorithm first!')
        print(f'The order of {self.a} mod {self.N} is {self.order}')


