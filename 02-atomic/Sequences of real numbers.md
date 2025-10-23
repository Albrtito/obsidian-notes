---
Date: 2024-03-19
tags:
  - calc
"References:": 
sr-due: 2024-06-22
sr-interval: 26
sr-ease: 250
---
# Intro and definition: 
A sequence is an application that assign to each natural number n a unique real number $a_n$ . 
+ No two natural numbers can have the same real number

Move from the  space of natural numbers to the space of real numbers. 
$$
s: \mathbb{N} \rightarrow \mathbb{R}
$$
## Definition: 
In order to define sequences we usually define the general term of the sequence $a_n$ . This term gives a description of every term in the sequence based on n
A sequence can be defined for an specific number of elements inside N. 
This means that even though usually n would take all possible values in N, it's domain can also be defined as N $\cup \{0\}$ or $n \in N , n > 3$ 

f.e: 
$$
s_1 = ({1\over n}_{n\in N}) = \{1, 1/2, 1/3, 1/4...\}
$$

During the calculus 1 course three main properties of sequences will be seen **convergence** (wether or not a sequence, when approaching infinity, tends to one specific value), **boundedness** (wether or not the sequence has upper or lower bounds, see [Boundedness](Boundedness.md)) and **monotonicity** (wether or not the sequence is getting bigger or smaller all the time)

# Properties: 
+ [Convergence of sequences](Convergence%20of%20sequences.md)
+ [Boundedness of sequences](Boundedness%20of%20sequences.md)
+ [Monotonicity of sequences](Monotonicity%20of%20sequences.md)
## Theorems: 
Really careful with how we use this two theorems. They really help to determine if a sequence is bounded, if it decreases or increases. However it is really easy to misread and obtain a conclusion based on some relation that is not stated in this two theorems. 

![Theorem 2 Convergent, then bounded. Not bounded, divergent](Theorem%202%20Convergent,%20then%20bounded.%20Not%20bounded,%20divergent.md)
![Theorem 3  Monotonicity + Boundedness = Convergence?](Theorem%203%20%20Monotonicity%20+%20Boundedness%20=%20Convergence?.md)
# Computation methods for sequences. 
## Limits of sequences:
 ![Limits of sequences](Limits%20of%20sequences.md)