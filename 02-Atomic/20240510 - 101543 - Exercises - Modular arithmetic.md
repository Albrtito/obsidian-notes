---
aliases:
  - Exercises - Modular arithmetic
tags:
  - discrete
"References:": 
cssclasses:
  - page-manila
---
# Exercises - Modular arithmetic: 
## 12.1: 
Given a = 92 and b = 84, use Euclid’s algorithm to compute d = gcd(a, b), Find integers x, y ∈ Z such that ax + by = d.

a = 92
b = 84
1. gcd(92,84) = d => gcd(92,84) = gcd(84,8) = gcd(8,4) = gcd(4,0) = 4
	$$
	\begin{gather}
	92 = 1\cdot 84 + 8 \Rightarrow 8 = 92 - 84\\
	84 = 10\cdot 8 + 4 \Rightarrow 4 = 84 - 10\cdot 8\\
	8 = 2 \cdot 4 + 0
	\end{gather}
	$$
+ 4 = d
2. Finc x, y $\in$ >; 
	+ ax + by = d
	$$
	4 = -10 \cdot 92 + 8 \cdot 11 \rightarrow x = -10, y = 11
	$$

## 12.7: Diophantine
Find the integer solutions of the Diophantine equations: 
1. 28x + 36y = 44. 
2. 66x + 550y = 88.

**Solving:**
1. Solve the first equation:

	i. Find greatest common divisor of 28 and 36. 
	+ gcd(28, 36) = gcd(7\*4, 6\*4) = 4

	ii. Because 4 | 44 => There is a solution
	
	iii. We can simplify the equation by dividing by 4. Obtaining: 7x + 9x = 11
	
	iv. Euclid’s algorithm to find d.
	$$
		\begin{gather}
		9 = 7 * 1 + 2 \Rightarrow 2 = 9 - 7\\
		7 = 3 * 2 + 1\\
		2 = 2 * 1 + 0
		\end{gather}
	$$
		Then: 
		$$
		\begin{gather}
		1 = 7 -3\cdot2 => \\1 = 7-3 \cdot(9-7) = 7 -3\cdot9 + 3\cdot7 = 4\cdot7 - 3\cdot1
		\end{gather}
		$$
   We have found d x, and y: 
	$$
	7 x + 9y = d \Rightarrow 7 * 4 + 9*(-3) = 1
	
	$$
	v. Now multiply by 11 it to get …= 11: 
	$$
		7 * 44 + 9*(-33) = 11
	$$
	We obtain x = 44, y = -33. Then we generalise using the formulas: 
	$$
		\begin{cases}
		x_n = 44 + 9n\\
		y_n = -33 -7n
		\end{cases}
	$$

## 12.8: Congruence relations
Solve the following congruence equations:
1. 3x ≡ 5 (mod 13)
2. 8x ≡ 2 (mod 10)
3. 5x ≡ 7 (mod 15)
4. 3x ≡ 9 (mod 15)

**Solving:**
1. The congruent relation is the same as: 
	$$
	3x + 13y = 5
	$$
	We know how to as it is a diophantine equation.
	$$
	\begin{gather}
		13 = 3 \cdot 4 + 1 \\
		\text{Turn it around}\\
		1 = 13-3\cdot 4\\ 
		\text{times 5 to get the initial d}\\
		5 = 13\cdot 5 + 3 \cdot(-20)
	\end{gather}
	$$
	Then the solutions for $x_o, y_0$ are: 
	$$
		\begin{cases}
		x_0 = -20 + 13n\\
		y_0 = 5 - 3n
		\end{cases}
	$$
	For congruent relations we **only care about the x.**
	$$
		-20 + 13 n \equiv -20 \mod 13 \equiv -7\mod 13 \equiv \boxed{6\mod 13}
	$$
4. **Reduction of the relation:**
	The applied reduction gives out the number of solutions that there should be at the end. If we have reduced by dividing by n, then there will be n solutions at the end of the problem (after undoing the reduction)
	$$
	3x \equiv 9\mod 15 \Rightarrow x \equiv 3 \mod 5
	$$
	Obtain the equivalence: 
	$$
		3x + 5n = x_n \equiv 3 \mod 5
	$$
	Undo the reduction by obtaining all values such  as in (mod 5) the remainder would be 3, however they fit inside the mod 15 equiv. classes (I don’t know if that is well explained)
	$$
	\boxed{
		\begin{cases}
		x_0 = 3 \mod 15\\
		x_1 = 8 \mod 15\\
		x_2 = 13 \mod 15\\
		\end{cases}}
	$$
	From that point on, the next value to comply with the definition stated above would be 18 as 3 mod 5 = 18 mod 15. However this value is equivalent to 3 mod 15. 
	