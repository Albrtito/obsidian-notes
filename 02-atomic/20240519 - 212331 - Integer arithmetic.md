---
aliases:
  - Integer arithmetic
tags:
  - discrete
"References:": 
cssclasses:
---
# Integer arithmetic: 
Integer arithmetic is the arithmetic that appears when the only set of numbers used is Z with the properties it has. The main property we’ll see that changes things is the existence of division for most of the integer numbers. We’ll see how to work around it and study those numbers that can be divided and the properties they have.
## Integer divisibility: 
### Properties of the set Z:
The set of integers Z is a **closed set** with respect to the operations sum, subtraction and product (closed = this operations can be used without obtaining a result outside of the set).
+ The 0 is the identity with respecto to the sum
+ 1 is identity with respect to the product 
+ For every element in Z, there exist an **unique inverse element** such that the sum of the two elements equals 0.

**THE IMPORTANT PART:** The result of division might not always be an integer. 

> [!NOTE] Definition:
> Given two integers a $\not = 0$ and b.
> + We say **a divides b** if there is an integer q such that: 
> $$
> b = a\cdot q
> $$
> + **IF:** a divides b 
> 	+ **THEN:** a is **a factor of** b 
> 	+ **THEN:** b is a multiple of a
> 
> Relation a divides b is denoted as **a|b**, when a does not divide b it is written as: **a$\not{|}$b**
> 

**Remarks:**
+ Every non-zero integer divides 0
+ 1 divides any integer
+ Any nonzero integer divides itself.

## The division algorithm
![[20240519 - 214201 - Algorithm - The division algorithm|The division algorithm]]
## Properties of integer division
### Relatively prime numbers: 
![[20240519 - 232552 - Definition - Relatively prime numbers|Relatively prime numbers]]
## Euclid’s lemma
Euclid’s lemma is used in Euclid’s algorithm to obtain the gcd(a,b) when a and b are to big to obtain their prime divisors and compute their gcd in the general way: 
![[20240519 - 233523 - Algorithm - Euclid's algorithm|Euclid's algorithm]]
## Bézout’s identity
![[20240429 - 114501 - Theorem -Bézout's Identity|Bézout's Identity]]
## Least common multiple
![[20240520 - 131833 - Least common multiple|Least common multiple]]
## Prime numbers: 
![Prime numbers](20240429%20-%20111500%20-%20Prime%20numbers.md)

## Linear Diophantine equations: 
![[20240429 - 113931 - Linear Diophantine equations|Linear Diophantine equations]]

