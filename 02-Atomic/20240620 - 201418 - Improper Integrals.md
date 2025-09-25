---
aliases:
  - Improper Integrals
Date: 2024-03-12
tags:
  - diffcalc
  - calc
"References:": 
sr-due: 2024-10-14
sr-interval: 34
sr-ease: 210
---
# Improper Integrals

Improper integrals of first kind are those integrals defined on an **infinite interval** and **integrable on each bounded subinterval**:

There are different improper integrals of **first kind:**

> [!NOTE] Definition: 
> 
>$$
\begin{align}
&1. \int_a ^\infty f(x) dx = \lim_{N \rightarrow \infty} \int_a^N f(x)dx\\\\
&2. \int_\infty ^b f(x) dx = \lim_{N \rightarrow \infty} \int_{-N}^b f(x)dx\\\\
&3. \int^\infty_{-\infty} f(x) dx = \int_{-infty}^a f(x) dx + \int^\infty _a f(x)dx : a \in \mathbb R
\end{align}
>$$
>Based on the solution of this limits we can say that there is (or not) a solution to the integral: 
>+ The limit **converges** => There is a solution
>+ The limit **diverges** => There is no solution
 