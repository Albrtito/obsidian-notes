---
aliases:
  - Exercises - Real Variable functions
tags:
  - calc
"References:":
  - "[[20240602 - 172958 - Real variable functions|Real variable functions]]"
  - "[[Calc_Exercises_RealVarFuncs.pdf]]"
cssclasses:
  - page-manila
sr-due: 2024-06-23
sr-interval: 12
sr-ease: 265
---
# Exercises - Real variable functions. 

Collection of solving methods for exercises provided in UC3M calculus course. 

## Properties of sets of numbers: 
+ 
## Prove an inequality: 
Given:
$$
0< a < b: k > 0
$$
Prove:
$$
a < \sqrt{ab} < \frac{a+ b}{2} < b
$$
**Methods:**
Either go backwards or forwards. Backwards means start in the inequality to prove and end in some given fact or basic statement.

f.e: Go forwards: 
$$
\begin{gather}
a < b \\
a \cdot a < a \cdot b \\
a^2 < ab \Rightarrow \boxed{a < \sqrt{ab}}
\end{gather}
$$
f.e: Go backwards:
$$
\begin{gather}
\sqrt{ab}< \frac{a+b}{2}\\
2\sqrt{ab} < a + b \\
ab < \frac{(a+b)^2}{4}\\
ab < \frac{a^2 + b^2 + 2ab}{4}\\
0 < -2ab + a^2 + b^2\\
\boxed{0 < (a-b)^2 : a \not = b}
\end{gather}
$$

## Prove that some formula is multiple of m.

Basic method with this types of exercises is to first of all factor the relation. 
f.e: Given $n^2-n$ first obtain: $n(n-1)$

Once factored, reason what types of multiples those factors must be. For this last example, either n or n-1 must be even. Therefore $n^2 - n$ must be even. 

For composite numbers, find it’s decomposition in some of it’s multiples: 

### 2.3: Given $n^2-1$ with n odd, prove that it is multiple of 8: 
$$
n^2 - 1 = (n-1)(n+1)
$$
If n is odd both factors must be even. One multiple of 2 and the other multiple of 4. From this we get 8. 

### 5.1: $n\in N$ $10 ^n - 1$ => Multiple of 9
$$
\begin{gather}
10^n -1 = 9k\\
¿10^{n+1} -1  ?
\end{gather}
$$
Include a $-10^n + 10^n$ in order to obtain the following:
$$
\begin{gather}
10^{n+1} -1 + 10^n - 10^n = \\
10^{n+1} + 9k - 10^n = 10^n(10-1) + 9k =\\
10^n(9) + 9k = 9[10^n + k]
\end{gather}
$$

$$

$$
## Induction: 

### Induction with SUMs: 
Divide the n+1 sum into the sum until n plus the value for n+1: 
f.e: Given: $\sum_1^n j = \frac{n(n+1)}{2}$ 
	For n +1: 
$$
	\sum ^{n+1}_1 j = \sum^n_1j + (n+1)
$$
	Then use the relation assumed for n.

### Induction with inequalities: 
Use the assumed inequality for n in order to rearrange the n+1 inequality to obtain something that can be proven as greater than, etc…

***

## Domains of functions:

### 1.2. $\arcsin(ln x)$
The arcsin function is defined between -1 and 1. Then, find the values for the ln x such as ln x = 1 and ln x = -1. Those are directly obtained with the definition: 
$$
\ln x = 1: x = e^x
$$
$$
\ln x = -1 : x = e^{-1} = \frac{1}{e}
$$
## Trigonometric relations:

Prove: $\sin^2 x = \frac{1-\cos(2x)}{2}$ using [[20240603 - 171608 - Trigonometric relations|Trigonometric relations]]
