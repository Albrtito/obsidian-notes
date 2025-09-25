---
aliases:
  - Chromatic poly of a cycle graph
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-06-10
sr-interval: 24
sr-ease: 228
---
The chromatic polynomial of a cycle graph is defined in the following way: 
$$
P_{C_n}(q) = (q-1)(-1)^n + (q-1)^n
$$
This expression is obtained from the following reasoning: 
1. A cycle graph $C_n$ defined with n vertices. 
2. Use the deletion-contraction theorem: Obtain: 
$$
P_{C_n}(q) = q(q-1)^{n-1}-P_{C_{n-1}}(q)
$$
3. Transform this recursive expression (name it different: $P_C = a_n$
$$
a_n = q(q-1)^{n-1}-a_{n-1}
$$
4. Solve the non-homogeneous recurrence.

+ Homogeneous part: Roots => 0 and -1
$$
a_h = A0^n + B(-1)^n
$$

+ Particular part: Guess => $(p-1)^{n-1}[A+Bq]$ **Remark:** A and B here are not the same ones as in the homogeneous computations. 
	+ Obtain values for A and B: A = -1, B = 1
	+ Final expression: 
$$
a_p = (q-1)^{n-1}[-1+q] = (q-1)^n
$$
+ Final solution for $a_n$ : 
$$
a_n = a_h + a_p = B(-1)^n + (q-1)^n
$$
+ Obtain the value of B: B = (q-1) 
$$
a_n = a_h + a_p = (q-1)(-1)^n + (q-1)^n
$$
**FINAL SOLUTION** ^e29f52

Go back into the expression named with the poly: 

$$
P_{C_n}(q) = (q-1)(-1)^n + (q-1)^n
$$

^7039f1
