# Two Qubit Interactions

This exercise contains three small programs which illustrate two qubit
interactions in QUBO models. Understanding these small problems is vital for
writing QUBOs for much larger problems.

## Exercise 1

To run the exercise 1 demo, type the command:

```python two_same.py```

Read through the code and take a look at the
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

## Exercise 2 

To run the exercise 2 demo, type the command:

```python two_different.py```

In this exercise, we want to penalize the two qubit solutions in which the 
qubits have the same values; we want to favor the two qubit solutions in 
which the qubits have different values.

In the results, you should notice that the solutions (0 1) and (1 0) have 
lower energy than the solutions (0 0) and (1 1).

## Exercise 3 

To run the exercise 3 demo, type the command:

```python two_implies.py```

Here is a definition of the implies function, from Wikipedia:

The concept of logical implication is associated with an operation on two 
logical values, typically the values of two propositions, that produces a 
value of false just in case the first operand is true and the second operand
is false.

Hence, the implies function in logic has the following truth table:

| X | Y |X -> Y|
|-|-|------|
|F|F|T|
|F|T|T|
|T|F|F|
|T|T|T|

In QUBO variables (0 = False, 1 = True), we can write the problem as

|x_1|x_2|result (energy)|
|---|---|---------------|
|0|0|0|
|0|1|0|
|1|0|1|
|1|1|0|

and and thus we want to penalize the (1 0) solution, relative to the others.
This explains why the energy of (1 0) is 1, whereas the energy of the other 
states is zero.
Your results should agree with this.
