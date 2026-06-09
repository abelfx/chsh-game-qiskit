# CHSH Game: Classical vs. Quantum Strategies

This repository contains a Python implementation of the CHSH (Clauser-Horne-Shimony-Holt) nonlocal game. The code uses IBM's Qiskit to simulate both classical and quantum strategies, mathematically demonstrating the violation of Bell's Inequality through quantum entanglement.

## Overview

The CHSH game involves two isolated players, Alice and Bob, who receive random binary questions ($x$ and $y$) from a referee. They must reply with binary answers ($a$ and $b$) without communicating. 

The winning condition is: 
$$a \oplus b = x \land y$$

* **Classical Limit:** Using purely classical physics (even with shared pre-planned strategies or randomness), the maximum possible win rate is capped at **75%**.
* **Quantum Strategy:** By sharing an entangled qubit pair (a Bell state $|\Phi^+\rangle$) and measuring at specific rotated bases ($\pi/8$ and $-\pi/8$), Alice and Bob can exploit quantum correlations to reach Tsirelson's bound, winning approximately **85.4%** of the time.

## Prerequisites

Ensure you have Python 3.12+ installed. Install the required dependencies using the provided requirements file:

```
```bash
pip install -r requirements.txt
```

## run
```
```
python3 quantum.py
```
```
