---
aliases:
  - Exercises - Integer arithmetic
tags:
  - discrete
"References:":
  - "[[20240519 - 212331 - Integer arithmetic|Integer arithmetic]]"
  - "[[Modular arithmetic]]"
  - "[[Discreta_Exercises_All_Solved.pdf]]"
cssclasses:
  - page-manila
---
# Exercises - Integer arithmetics: 

## 12.1
Given a = 92 and b = 84, use Euclid’s algorithm to compute d = gcd(a, b), Find integers x, y ∈ Z such that ax + by = d.

gcd(92,84)  = gcd(84,8) = gcd(8,4) = gcd(4,0) = 4
This is equal to: 
$$
\begin{gather}
92 = 84\cdot1 + 8 \\
84 = 8 \cdot 10 + \boxed{4}\\
8 = 4\cdot 2 + 0
\end{gather}
$$
`
Then gcd(a,b) = 4

Going backwards:
$$
\begin{gather}
4 = 84 - 8 \cdot 10 \\
8 = 92 - 84\\
\Rightarrow\\
4 = 84 - (92-84) \cdot 10 = 11\cdot 84 - 10 \cdot 92
\end{gather}
$$
Then x = -10 and y = 11

## 12.2
The product of two natural numbers is 1260, and their lcm is 630. Find those numbers.
$$
a \cdot b = 1260
$$
$$
lcm(a,b) = 630
$$
We know that: 
$$
a \cdot b = gcd(a,b) \cdot lcm(a,b)
$$
Then: 
$$
1260 = 630 \cdot gcd(a,b)
$$
gcd(a,b) = 2

## 12.3
Positive divisors of the number ….


## 12.7 Diophantine equations
Integer solutions of Diophantine equations: 

1. 28 x + 36y = 44
	
	**Check possible solution**: If gcd(28,36)| 44
	gcd(28,36) = 4  and 4 | 44 => There is a  possible solution. 
	
	Get x y such as: 28 x + 36 y = 4
	
	**From Euclid’s theorem:** 
	$$
	\begin{gather}
	36 = 28 \cdot 1 + 8\\
	28 = 8 \cdot 3 + 4\\
	8 = 4 \cdot 2 + 0
	\end{gather}
	$$
	**Unrolling**: 
	$$
	\begin{gather}
	4 = 28 - 8\cdot 3\\
	8 = 36 - 28\\
	\Rightarrow\\
	4 = 28 - (36-28) \cdot 3 \Rightarrow 4 = 4\cdot 28 - 3 \cdot 36
	\end{gather}
	$$
	**Where** x = 4 ,  y = -3
	
	**Then**: 
	$$
	x_k = 4(11) + \frac{36k}{4} = 44 + 9k
	$$
	$$
	y_k = -3(11) + \frac{28k}{4} = -33 + 7k
	$$

2. 66x + 550y = 88
	
	**Check possible solution:**
	+ Get gcd(66,550)
	$$
	\begin{gather}
	550 = 66 \cdot 8 + 22\\
	66 = 22 \cdot 3 + 0
	\end{gather}
	$$
		gcd(66,550) = 22
		
	+ Check that gcd(a,b) | 88 => True, as 22 | 88
	+ Obtain a solution for x and y such as: 
	$$
	x\cdot a + y \cdot b = 22
	$$
	**Unroll Euclid’s (used for gcd)**
	$$
	\begin{gather}
	22 = -8 \cdot 66 + 1\cdot 550
	\end{gather}
	$$
	**Where:** x = -8 and y = 1
	
	**Then:** All solutions are given as: 
	$$
	\begin{gather}
	x_k = -8 (4) + \frac{550k}{22} \\\\
	y_k = 1(4) - \frac{66k}{22} 
	\end{gather}
	$$
	
	$$
	\forall k \in Z
	$$
	
## 12.8: Congruence equations.

1. 3x ≡ 5 (mod 13). 
	
	The congruence equation can be seen as: 
	$$
	5 = 3x + 13y \Rightarrow 3x + 13y = 5
	$$
	**CHECKS:**
	There is a solution if and only if gcd(3,13) | 5. Here gcd(3,13): 
	$$
	\begin{gather}
	13 = 3 \cdot 4 + 1\\
	3 = 1 \cdot 3 + 0
	\end{gather}
	$$
	gcd(3,13) = 1 and 1 | 5
	
	**THEN:**
	For some x and y: 
	$$
	\begin{gather}
	1 = 13 - 4\cdot 3
	\end{gather}
	$$
	Because we are only looking for values for the x: 
	$$
	x_k = 5 \cdot (-4) \frac{13k}{1} = 5(-4) \cdot 13k = -20 \cdot 13k
	$$
	This solutions can be expressed in terms of the congruence relation mod 13 as: $-20 \mod 13$
	This expression can be simplified to: 
	$$
	-20 \mod 13 \equiv 6 \mod 13 \equiv x
	$$
	**Remark:**
	This simplification done with division theorem: 
	$$
	-20 = 13 (-2) + 6
	$$
	
2. 8x ≡ 2 (mod 10). 
	
	The congruence equation can be expressed as: 
	$$8x + 10y = 2$$
	**Check:**
	This equation has solutions if gcd(8,10) | 2. 
	gcd(8,10) = 2
	$$
	\begin{gather}
	10 = 8 \cdot 1 + 2\\
	8 = 2 \cdot 4
	\end{gather}
	$$
	**Then:** 2 | 2 and there are solutions for the eq. 
	
	**Solve:**
	Get x and y unrolling: x = -1 and y = 1
	$$
	-1\cdot 8 + 10 = 2
	$$
	Obtain solution for all x: 
	$$
	x_k = -1(1) + \frac{k10}{2} = -1 + 5k
	$$
	This can be expressed as $-1 \mod 5$, equivalent to $4 \mod 5$
	
	However as the solution must be given mod 10. Then we get: 
	$$
	\begin{gather}
	4 \mod 10 \equiv x\\
	9 \mod{10} \equiv x
	\end{gather}
	$$

3. 5x ≡ 7 (mod 15). 
	The following congruence equation can be written as:
	$$
	5x + 15y = 7
	$$
	**Check:**
	Because c = 7. Then we know that unless gcd(5,15) is 7 there will be **no solution**. The gcd(5,15) is not 7 and therefore there is **no solution**

4. 3x ≡ 9 (mod 15).
	The following congruence equation can be written as: 
	$$
	3x + 15 y = 9
	$$
	This is a diophantine equation. We first check if it has a solution: 
	**Check:**
	Solution if gcd(3,15) | 9 => TRUE 3 | 9
	
	**Unroll:**
	A solution would be: 
	$$
	3 = 1\cdot 3 + 0 \cdot 15
	$$
	Then because we only care about the x: 
	$$
	x_k = 3(1) + \frac{k15}{3} = 3 + 5k/
	$$
	This solutions are equivalent to 3 mod 5. If we go back towards mod 15 we’ll get: 
	$$
	\begin{gather}
	x \equiv 3 \mod 15\\
	x \equiv 8 \mod 15\\
	x \equiv 13 \mod 15\\
	\end{gather}
	$$
