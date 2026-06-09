import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def play_coursework_chsh(num_games=1000):
    """
    Implements the CHSH game using the exact geometric angles 
    specified in the IBM Quantum Learning material.
    """
    simulator = AerSimulator()
    wins = 0

    for _ in range(num_games):
        # Referee uniformly distributes questions
        x = np.random.randint(0, 2)
        y = np.random.randint(0, 2)

        # Initialize 2 qubits (A and B) and 2 classical bits
        qc = QuantumCircuit(2, 2)

        # Set-up: Create the entangled e-bit |Φ+⟩
        qc.h(0)
        qc.cx(0, 1)

        # Alice's actions (Qubit 0)
        # Choosing angle α based on x, applying U_α = Ry(-2α)
        if x == 0:
            alpha = 0
            qc.ry(-2 * alpha, 0)
        else: # x == 1
            alpha = np.pi / 4
            qc.ry(-2 * alpha, 0)

        # Bob's actions (Qubit 1)
        # Choosing angle β based on y, applying U_β = Ry(-2β)
        if y == 0:
            beta = np.pi / 8
            qc.ry(-2 * beta, 1)
        else: # y == 1
            beta = -np.pi / 8
            qc.ry(-2 * beta, 1)

        # Measurement
        qc.measure([0, 1], [0, 1])

        # Execute and extract results
        result = simulator.run(qc, shots=1, memory=True).result()
        measured_bits = result.get_memory()[0]

        # Qiskit orders classical bits as 'b a' (Qubit 1, Qubit 0)
        b = int(measured_bits[0])
        a = int(measured_bits[1])

        # Evaluate win condition: a ⊕ b = x ∧ y
        if (a ^ b) == (x & y):
            wins += 1

    return wins / num_games

def play_coursework_classical(num_games=1000):
    """
    Simulates the optimal classical strategy where Alice and Bob 
    pre-agree to always output 0.
    """
    wins = 0
    for _ in range(num_games):
        x = np.random.randint(0, 2)
        y = np.random.randint(0, 2)
        
        # Alice and Bob always output 0 regardless of x and y
        a = 0
        b = 0
        
        # Evaluate win condition: a ⊕ b = x ∧ y
        if (a ^ b) == (x & y):
            wins += 1
            
    return wins / num_games

if __name__ == "__main__":
    games = 5000
    
    classical_win_rate = play_coursework_classical(games)
    quantum_win_rate = play_coursework_chsh(games)
    
    print(f"Classical Strategy Win Rate ({games} games): {classical_win_rate * 100:.2f}%")
    print(f"Quantum Strategy Win Rate ({games} games):   {quantum_win_rate * 100:.2f}%")
   
