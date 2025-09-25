---
aliases:
  - Deduction Theorem
tags:
  - logic
"References:": 
cssclasses: 
sr-due: 2025-01-07
sr-interval: 257
sr-ease: 330
---
The deduction theorem is used in logic (however the structure it has can be applied to any logic-based structures, such as all mathematics)

> [!NOTE] Theorem: Deduction theorem
> **Condition:**
> If $p_1,p2,…,p_n \Rightarrow q_1,q_2,…,q_m$ is a correct deduction. 
> **Consequences:**
> Then $p_1,p_2,…,p_{n-1} \Rightarrow p_n \rightarrow q_m$ is also a correct deduction. 

**Remark:**
The opposite is also true: Given a deduction
$$
	p_1,p_2,p_3 \Rightarrow (A\rightarrow (B \rightarrow C)
$$
We can obtain: 
$$
p_1, p_2, p_3, A, B \Rightarrow C
$$
**This is how it’s mostly used.**

**Restriction:**
Free variables in $p_n$ cannot be used to obtain $q_m$ by means of universal generalisation rules. 

**Careful:**
Not every correct deduction has a related valid formula, there cannot be a part of the deduction empty:

f.e (prepositional calculus example):
	$$
	\begin{gathered}
	\mathrm{B}(\mathrm{y}) \Rightarrow \forall \mathrm{xB}(\mathrm{x}) \text { Valid } \\
	\Rightarrow \mathrm{B}(\mathrm{y}) \rightarrow \forall \mathrm{xB}(\mathrm{x}) \text { Not valid }
	\end{gathered}
	$$
