---
aliases:
  - Linear Diophantine equations
tags:
  - discrete
"References:": 
cssclasses:
---
A **Diophantine equations** is an equation of one or several variables such that we are only interested in their integer solutions. 

This equations are of the type: 
$$
a *x + b*y = c
$$
This equation has solutions if and only if gcd(a,b) | c. This can be better understood once read and understood the [Bézout's Identity](20240429%20-%20114501%20-%20Theorem%20-Bézout's%20Identity.md) that poofs that for d = gcd(a,b) then there exist some integer values for x and y such as: 
$$
ax + by = d
$$
Then if d | c, the equation has **infinite solutions** $(x_k, y_k)$ with $k\in Z$. This solutions are given by: 
$$
\begin{gather}
x_k = u p + \frac{bk}{d}, \\\\
y_k = wp - \frac{ak}{d}
\end{gather}
$$
**Remarks:** 
Where p, u and w are computed in the following form. 
$$
\begin{gather}
c = dp \\
p = c/d
\end{gather}
$$
And u and w are given by: 
$$
d = u \cdot a + w\cdot b
$$
This can be obtained by applying the solutions for x and y to the initial equation: 
$$
\begin{gather}
 c = ax_k + by_k = a(up + \frac{b}{d}k) + b(wp - \frac{a}{d}k) = \\
 = a(up) + a(\frac{b}{d}k) + b(wp) - b(\frac{a}{d}k)\\
 \Rightarrow \\
 c = a(up)+ b(wp) \Rightarrow \boxed{c /p = ua + wb = d}
\end{gather}
$$
This means that we can obtain u and w from the [[20240429 - 114501 - Theorem -Bézout's Identity|Bézout's Identity]]

