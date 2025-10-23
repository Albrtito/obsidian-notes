---
aliases:
  - Derivative
  - Differentiability of a function
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-06-21
sr-interval: 5
sr-ease: 244
---
# Differentiability: 
Differentiability is defined as the capacity for a function to be differentiable.

> [!NOTE] Definition:
> We say that a function is **differentiable at a point a** if the following limit exits and is finite: 
> $$
> \lim_{h \rightarrow 0} \frac{f(a+h) -f(a)}{h}
> $$
> This limit is equivalent to: 
> $$
> \lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}
> $$
> 

**Remarks:**
+ If this limit exists then it is called the **derivative of f at a.** This has several notations: 
	+ **Newton’s notation:** $f’(a)$
	+ **Leibniz’s notation** $\frac{df(a)}{dx}$
+ A function can be differentiated several times. This new derivatives are called **high order derivatives of a function** and are denoted by(again, several notations, all equivalent): 
	+ **Newton’s notation:** $f’’(x), f’’’(x), …, f^{(n}(x)$ → (yes, only one parenthesis)
	  
	+ **Leibniz’s notation**: $\frac{d^nf(x)}{dx^n}$

+ Derivatives of the most common functions can be seen here: [[References_Derivatives&Integrals.pdf]]
+ Derivatives have a direct impact on:
  +  [[20240605 - 211212 - Continuity of a single variable function|Continuity of a single variable function]]
    This is because **if f is differentiable at a, then it is also continuous at a**. This goes both ways. **If f is not continuous at a then it is also not differentiable at a**. 
    BUT CAREFUL: Because if f is continuous then it is not mandatory differentiable. Corner points cannot be differentiable. 

+ See derivation in several variables at [[20240529 - 165329 - Definition - Partial derivatives|Partial derivatives]]


## Differentiable on an interval: 

> [!NOTE] Definition:  
> We say that a function f is differentiable on an interval (a,b) if it is differentiable a all the points of (a,b).
> The points where f is differentiable are given by the **domain of f’**
> 

## Side derivatives: 
Same as with limits, or because we can do side limits, we can also do side derivatives with those same limits. 

> [!NOTE] Definition: 
> Using the concept of side limits we can define side derivates as: 
>$$
> \lim_{h \rightarrow 0^+} \frac{f(x) - f(a)}{h}
> $$
> $$
> \lim_{h \rightarrow 0^-} \frac{f(x)-f(a)}{h}
> $$

## Properties: 
Basic properties, rules we use for the computation of derivatives: 

1. Derivation is linear: 
$$
(cf)' = cf'
$$
$$
(f+g)' = f' + g'
$$
2. Derivation of the **product:**
$$
(fg)' = f'g + fg'
$$
3. Derivative of:
$$(\frac 1 g)’ = \frac {-g’}{g^2}: \text{ for } g ≠ 0
$$
4. Derivative of a **quotient:** 
$$
(\frac{f}{g})' = \frac{f'g - fg'}{g^2}
$$
+ g ≠ 0
### Continuity of the derivative: 

> [!NOTE] Theorem: 
> IF f is continuous at a and the limit of the derivative of f at a exists and is finite. Then the derivative is continuous at a.Meaning:
> $$
> f'(a) = \lim_{x\rightarrow a}f'(x)
> $$


**Remark:**
+ A derivative never has an avoidable discontinuity

## Relations with the inverse function: 
Given the inverse function of f defined as [[20240615 - 202910 - Definition - Inverse function|Inverse function]]. 
+ ![[20240615 - 202910 - Definition - Inverse function#Differentiability of a function and it’s inverse]]

The application of this theorem is used to compute the derivatives of the inverse of trigonometric functions.
+ [[20240615 - 204101 - Main Derivatives#Inverse functions|Derivatives of the inverse trigonometric functions]]

## Applications: 

+ [[20240615 - 211237 - Theorem - Cauchy Mean Value theorem|Theorem - Cauchy Mean Value theorem]]
+ [[20240616 - 155016 - Theorem - L'Hôpital-Bernoully rule|Theorem - L'Hôpital-Bernoully rule]]
