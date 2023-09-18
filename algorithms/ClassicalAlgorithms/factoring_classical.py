from sympy import factorint
from algorithms.algorithm import Algorithm
from typing import Optional


class FactoringClassical(Algorithm):

    def __init__(self, name: str, N: int):
        super().__init__(name)
        self.N: int = N
        self.factors: Optional[list[int]] = None

    def run(self):
        self.factors = factorint(self.N).keys()

    def plot(self):
        if self.factors is None:
            raise ValueError('Please run the algorithm first!')
        print(f'The factors of {self.N} are {self.factors}')