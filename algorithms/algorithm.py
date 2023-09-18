from abc import ABC, abstractmethod


class Algorithm(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self):
        pass

    def __repr__(self):
        return self.name


    @abstractmethod
    def plot(self):
        pass
