---
aliases:
  - Algorithm - Euclid's algorithm
  - Euclid's algorithm
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-05-21
sr-interval: 1
sr-ease: 186
---
# Euclid’s algorithm: 
This algorithm is based on:
![[20240519 - 233059 - Theorem - Euclid's theorem in integer arithmetic|Euclid's theorem in integer arithmetic]]

The algorithm is applied recursively to compute the gcd(a,b). This is better understood with an example: 

f.e: 
	gcd(662, 414)
	$$
	\begin{gather}
	a = bq + r\\\\
	662 = 414 \cdot 1 + 248\\\\
	414 = 248 \cdot 1 + 166\\\\
	248 = 166 \cdot 1 + 82\\\\
	166 = 82 \cdot 2 + 2\\\\
	82 = 2 \cdot 41 + 0\\\\
	\end{gather}
	$$
	Then gcd(662, 414) = gcd(82, 2) = 2

## Generalisation: 
In general, given two integers a and b: 
$$
\gcd(a,b) = \gcd(b, r_1) = \gcd(r_1,r2)  = ...= \gcd(r_{n-2}, r_{n-1})
$$
+ where $r_{n-1}$ is the last non-zero remainder.
+ **Then:** $$\boxed{\gcd(a,b) = r_{n-1}}$$
