---
aliases: 
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-07-25
sr-interval: 86
sr-ease: 232
---
# Intro: 
A generating function is created as the infinite sum of the terms of a sequence $(a_k)^\infty_{k=0}$ multiplied by their respective power of x. 

The infinite sum can be sometimes simplified in order to obtain an expression for the generating function (this is usually what we are aiming for)

Using generating functions many times resolves in knowing the simplification for several of the functions and where these functions come from, therefore I have created the following list with [All Generating Functions (list)](list))

## General form of a generating function:

![Definition 113](20240408%20-%20185315%20-%20Definition%20113%20Generating%20function.md)

# Basic operations with GFs: 
## The sum of two GF: 
The sum of two generating functions can be computed by summing inside the Sum the terms of each sequence that generates them. 

**Then:**

IF:
$$F(x)=\sum_{n=0}^{\infty} a_n x^n;G(x)=\sum_{n=0}^{\infty} b_n x^n$$THEN:

$$F+G)(x)=\sum_{n=0}^{\infty}\left(a_n+b_n\right) x^n$$
### Adding K zeroes on the left: 
If we have a sequence $\{a_n\}^\infty_{n=0}$ that generates the GF F. Then in order to create a GF for the sequence: $$(\underbrace{0,0, \ldots, 0}_k, a_0, a_1, \ldots) $$
We’ll just multiply the previously generated GF by $x^k$, such we’ll get G(x)

$$
 G(x)=x^k F(x) \text {. }
$$
#duda  : Why does it work like that??
# Practical problems