---
aliases:
  - Chromatic poly of a wheel graph
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-06-11
sr-interval: 23
sr-ease: 188
---
**Remark:** Before defining the polynomial, it is important to notice that the wheel graphs are defined as following: 

A wheel graph $W_n$ **has n + 1 vertices** with n vertices joined adjacently in a loop an the other one in the center joined to every vertex but itself. See image. 
![Pasted image 20240423132014](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240423132014.png)

Then, based on this definition, the chromatic poly of the graph is computed in the following way: 

1. Obtain the recurrence by contraction-deletion theorem: The deleted edge lets us use the product principle to compute the polynomial. 
$$
P_{W_n} = q(q-1)(q-2)^{n-1} + P_{W_{n-1}}
$$
2. Solve the recurrence: 

Non-Homogeneous recurrence: 
+ Homogeneous part => Two roots: q = 0, q = -1 
+ Non-Homogeneous part (particular) => Guess: $(q-2)^{n-1}[A+Bq+Cq^2]$ 
	After computations, we obtain: A = 0, C = 1, B = -2. This results in: 
$$
	(q-2)^{n-1}[-2q+q^2] = (q-2)^{n-1}[q(-2+q)] = q(q-2)^n
$$
3. Solution of the recurrence without computing B: 
$$
P_{W_n} (q) = B(-1)^n + q(q-2)^n
$$
Using $W_3 = K_3$ we have: 
$$
q(q-1)(q-2) = B(-1)^n + q(q-2)^n
$$
Then B = q(q-2)

4. **FINAL SOLUTION:** ^FinalSol
$$
P_{W_n} (q) =q(q-2)(-1)^n + q(q-2)^n
$$
^FinalSol