from algorithms.QuantumAlgorithms.qft import QFT
from algorithms.ClassicalAlgorithms.order_finding_brute_force import OrderFindingClassical
from algorithms.QuantumAlgorithms.factoring_shor import FactorShor




if __name__ == '__main__':
    algorithm = FactorShor('Shor', 537)
    algorithm.run()
    algorithm.plot()

