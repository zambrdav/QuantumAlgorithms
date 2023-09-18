import qiskit
import numpy as np
from algorithms.algorithm import Algorithm
from qiskit.circuit.library import PhaseGate
import matplotlib.pyplot as plt
from functools import lru_cache, cached_property


@lru_cache()
def _build_circuit(qubits: int):
    circuit = qiskit.QuantumCircuit(qubits)
    for i in range(qubits):
        circuit.h(i)
        for k, j in zip(range(2, qubits + 1 - i), range(i + 1, qubits)):
            R_k = _R_k(k).control()
            # Apply  the gate to the i qubit with j as controll
            circuit.append(R_k, [j, i])
    # swap the qubits
    for i in range(qubits // 2):
        circuit.swap(i, qubits - i - 1)
    return circuit


def _R_k(k: int):
    return PhaseGate(2 * np.pi / 2 ** k)


class QFT(Algorithm):

    def __init__(self, name: str, qubits: int):
        super().__init__(name)
        self.qubits = qubits
        self.result = None


    @cached_property
    def circuit(self):
        return _build_circuit(self.qubits)


    @cached_property
    def inverse_circuit(self):
        return self.circuit.inverse()



    def run(self):
        # define the simulator
        simulator = qiskit.Aer.get_backend('qasm_simulator')
        job = qiskit.execute(self.circuit, simulator, shots=1024)
        self.result = job.result()



    def plot(self):
        # plot the circuit
        print(self.circuit)
        self.circuit.draw(output='mpl')
        plt.show()


