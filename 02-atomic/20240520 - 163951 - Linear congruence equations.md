---
aliases:
  - Linear congruence equations
tags:
  - discrete
"References:": 
cssclasses:
---
# Linear congruence equations
Linear congruence equations are a way of proposing the [Linear Diophantine equations](20240429%20-%20113931%20-%20Linear%20Diophantine%20equations.md). 

For this type of equations we ask whether there is a number x such as if multiplied by a the following relation would comply.  
$$
a \cdot x \equiv b \mod m 
$$
This can be rewritten as the Diophantine equation:
$$
b = a\cdot x + m y
$$
Where for a solution to be found the gcd of a and b (denoted as d) must divide b. 
$$
gcd(a,m)| b
$$
## Formal definition:

> [!NOTE] Definition: Congruence equation
> A congruence modulo m of the form: 
> $$
> a \cdot x \equiv b \mod m
> $$
> **Where**:
> + m is a positive integer
> + a,b are integers 
> + x is a variable 
> 
> **Then:** This is called a **congruence equation**

**Remarks:**
+ Obtaining the **multiplicative inverse** of $a \mod m$ is **equal to** $a\cdot x \equiv 1 \mod{m}$ **IF:** There is an **unique solution** for that relation. 
+ **If** x is a solution of a linear congruence equation **and**:  $x'\equiv x \mod{m}$. 
	**Then:** x’ is **also a solution of that equation.**
+ The solution of a linear congruence equation are the equivalent classes classes of congruence modulo m. Elements of $\mathbb{Z}_m$

## Solving linear congruence equations:

> [!NOTE] Theorem: Solving linear congruence equations 
> 
> **IF:**
> + d = gcd(a,m)
> **THEN:**
> The linear congruence equation:
> $$
> a \cdot x \equiv b \mod m
> $$
> 
> Has a solution **if and only if** d | b.
> 
> After obtaining one single solution of the congruence equation $x_0$. The general solution is given by: 
> $$
> x_k = x_0 + \frac{m\cdot k}{d}, k\in Z
> $$
> 
> Because for every congruence equation we’ll have d equivalent classes, one for each possible solution of the congruence equation. The set of solutions is:
> $$
> \left\{x_0, x_0+\frac{m}{d}, x_0+\frac{2 m}{d}, \ldots, x_0+\frac{m(d-1)}{d}\right\}
> $$
> 

**Remarks:**
+ **IF** gcd(a, m) = 1 with m > 1:
	+ **Then:** The solutions of the linear congruence equation: $a\cdot x \equiv b \mod m$ form **one unique congruence class modulo m**
+ **IF:** gcd(a, m) = 1 with m >1. Then there e**xists an unique multiplicative inverse of a modulo m**

There exists a multiplicative inversee of a modulo m. This multiplicative inverse is unique modulo m