---
aliases:
  - Bézout's Identity
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-05-21
sr-interval: 1
sr-ease: 190
---


> [!NOTE] Theorem:
> IF a and b are: 
> + Two integers
> + Not simultaneously zero
> **THEN:**
> Exists integers u and w such that: 
> $$ 
> gcd(a,b)= a \cdot u + b\cdot w
> $$

**Remarks:**
+ The proof of this theorem is given by “unrolling” the steps of [[20240519 - 233523 - Algorithm - Euclid's algorithm|Euclid's algorithm]]. 
![[Screenshot 2024-05-19 at 23.53.57.png]]

+ The Bézout’s identity does **not imply that the integers u and v are unique**

From this identity we obtain the following theorems: 

> [!NOTE] Theorem: 
> Let a and b be two integers not simultaneously zero with gcd(a,b) = d. 
> **THEN:**
> An integer c can be written in the form: $$a\cdot x + b\cdot y $$
> + For some integers x,y
> + IF and only if: c is multiple of d.

**Remarks:**
+ In particular, d is the smallest positive integer of the form $a \cdot x + b \cdot y$ with $x,y \in Z$

+ Going back to [[20240519 - 232552 - Definition - Relatively prime numbers|Relatively prime numbers]]. Two integers are relatively prime if exists integers x, y such that: $a \cdot x + b \cdot y = 1$

+ **IF:** gcd(a,b) = d **THEN:** 
	+ $gcd(m \cdot a , m \cdot b)$ = m * d: For all m in N
	+ $\gcd (\frac{a}{d}, \frac{b}{d})$= 1

+ **IF:** a and b relatively-prime **THEN:** 
1. If a| c and b | c, then $(a\cdot b)$ | c
2. If a | $(b \cdot c)$ then a|c

