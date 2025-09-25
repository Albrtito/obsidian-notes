---
aliases:
  - Computation of the gcd and lcm
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-06-14
sr-interval: 42
sr-ease: 292
---
The greatest common divisor (gcd) and lowest common multiple (lcm) can be computed based on the [Fundamental theorem of Arithmetic](20240429%20-%20112402%20-%20Theorem%20-%20Fundamental%20theorem%20of%20Arithmetic.md). It can be said that for two composite numbers a and b bigger than 1. 
$$
a  = p_1^{n_1} * p_2^{n_2} * p_3^{n_3} ... * p_k^{n_k}
$$
$$
b = p_1^{m_1} * p_2^{m_2} * p_3^{m_3} ... * p_k^{m_k}
$$
**Then:** 
$\boxed{\text{gcd(a,b) }= p_1^{\min(n_1,m_1)}*p_2^{\min(n_2,m_2)}…p_k^{\min(n_k,m_k)}}$
$\boxed{\text{lcm(a,b) }=p_1^{\max(n_1,m_1)}*p_2^{\max(n_2,m_2)}…p_k^{\max(n_k,m_k)}}$

**Remarks:**
+ The lowest common multiple can be found once known the greatest common divisor: 
$$
lcm(a,b) = {a * b \over gcd(a,b)}
$$
+ Based on the proposed formula we obtain: 
$$
gcd(a,b) = {a * b \over lcm(a,b)}
$$
