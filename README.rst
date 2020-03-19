=============
Two Qubit Interactions
=============

This exercise contains three small programs which illustrate two qubit
interactions in QUBO models. Understanding these small problems is vital for
writing QUBOs for much larger problems.

Exercise 1 
----------

Run ``two_same.py``.  Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain a sampler/solver
- Define the Q matrix
- Run the problem, using the sampler/solver
- Print the results

In this exercise, we want to penalize the two qubit solutions in which the 
qubits have different values; we want to favor the two qubit solutions in 
which the qubits have the same values.

In the results, you should notice that the solutions (0 0) and (1 1) have 
lower energy than the solutions (0 1) and (1 0).

Exercise 2 
----------

Run ``two_different.py``.

In this exercise, we want to penalize the two qubit solutions in which the 
qubits have the same values; we want to favor the two qubit solutions in 
which the qubits have different values.

In the results, you should notice that the solutions (0 1) and (1 0) have 
lower energy than the solutions (0 0) and (1 1).

Exercise 3 
----------

Run ``two_implies.py``.

The implies function in logic has the following truth table:

=== === ===
F   F   T
F   T   T
T   F   F
T   T   T

In QUBO variables, we can write the problem as

=== === ===
0   0   0
0   1   0
1   0   1
1   1   0

and thus we want to penalize the (1 0) solution, relative to the others.
Your results should agree with this.
