---
aliases: 
tags:
  - discrete
"References:":
  - "[[20240510 - 101543 - Exercises - Modular arithmetic|Exercises - Modular arithmetic]]"
cssclasses:
---
Modular arithmetic is based on the simple concept of a division of integer numbers. This division follows the following property: 
$$
q = a \text{ div } b 
$$
$$
a = b \cdot q + r
$$
**Where**: 
+ r is the remainder of dividing a by b
+ q is the integer part of the solution 

**Remark:** 
We can establish some bounds for this relation: 
$$
0 \leq r \leq |b| -1
$$
Given this definition we can define **congruent relations** 
# Congruent relation: 
![[20240429 - 121006 - Congruent relation|Congruent relation]]

# Operating with modular arithmetic.
The congruent relation makes it so the operations we are used to for regular mathematics change. 

**Given**: 
$$
\begin{gather}
a_1 \equiv  b_1 \mod m\\
a_2 \equiv  b_2 \mod m\\
\end{gather}
$$
Then the following properties can be proved: 

## Addition and subtraction: 

$$
a_1 \pm a_2 \equiv b_1 \pm b_2 \mod m
$$
## Product properties: 
$$
a_1 \cdot a_2 \equiv b_1 \cdot b_2 \mod m
$$
## Power operations:
**IF:**
$$
a \equiv b \mod m
$$
**THEN:**
$$
a^k \equiv b^k \mod m
$$
+ For k a positive integer.

## Theorems: 

Let m be a positive integer and let a, b, c be integers. 

**IF:**
+ $a \cdot c \equiv b \cdot c \mod m$
and
+ gcd(c,m) = 1
**THEN:**
$a\equiv b mod m$

# Linear congruence equations: 
![[20240520 - 163951 - Linear congruence equations|Linear congruence equations]]
# Arithmetic with $\mathbb{Z}_m$
$\mathbb{Z}_m$ is composed by the elements of the quotient set described by the congruence relation modulo m on Z.

During this section we’ll use the following notation: 
$$
x\in Z_m \Rightarrow_{Def} \space x \in [x]_m
$$
## Sum and multiplication: 
Sum and multiplication are defined as: 
$$
x + y = [x]_m + [y]_m = [x+y]_m
$$
$$
x \cdot y = [x]_m \cdot [y]_m = [x\cdot y]_m
$$
Satisfying the following properties: 
+ **Closure**
+ **Associativity**
+ **Commutativity**
+ **Distributivity**
+ **Identity element (sum)**
+ **Identity element (product)**
+ **Inverse element (sum)**

**Remark:**
+ These properties are the same ones as those characterizing a field. However there is **no multiplicative inverse**


### Multiplicative inverse of x:
![[20240520 - 171554 - Definition - Modular arithmetics - Multiplicative inverse of x|Modular arithmetics - Multiplicative inverse of x]]




