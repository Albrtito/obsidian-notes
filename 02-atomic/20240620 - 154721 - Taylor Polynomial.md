---
aliases:
  - Taylor Polynomial
tags:
  - calc
"References:":
  - https://www.youtube.com/watch?v=8SsC5st4LnI
  - https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=1s
  - "[[Calc_Theory_Taylor.pdf]]"
cssclasses: 
sr-due: 2024-06-27
sr-interval: 3
sr-ease: 250
---
# Taylor polynomial 
Taylor polynomial is used to **approximate a function near a given point using a polynomial**

**NOTE:** Remark that is an approximation **near a given point** → Remember this for limits


> [!NOTE] Definition: General form: 
> We define the Taylor polynomial of **degree n of f** near the point $x_0$ as:
> $$
P_{n,x_0}f(x) = \sum_{k = 0}^{n}\frac{f^{k)}(x_0)}{k!} (x-x_0)^k
> $$

**Remarks:**
+ When the point $x_0 = 0$ then the taylor polynomial is known as **McLaurin polynomial**
+ The following list compiles the basic taylor and McLaurin polynomials: [[20240620 - 160937 - Main Taylor Polynomials|Main Taylor Polynomials]]


> [!NOTE] Theorem:  
> If f and its derivatives up to order n exists at $x_0$, then:
> $$
> lim_{x \rightarrow x_0} \frac{f(x)-P_{n,x_0}f(x)}{(x-x_0)^n} = 0
> $$
> 

This means that the taylor polynomial gives out a **better approximation** the closer it is to the point $x_0$

## Usage of small-o
With taylor polynomials the [[20240620 - 162021 - Definition - small-o|small-o]] definition is used to gather all terms of the polynomials bigger than some x.

f.e:
	For the taylor polynomial of $e^x$ when x tends to 0 we have: 
	$$
	\frac 1{n!}x^n
	$$
	If we just want to express the first three terms and notate that all bigger terms are under some small-o:
	$$
	e^x = 1 + x + \frac{x^2}{2} + o(x^2)
	$$
## Properties: 

1. If we want to obtain the taylor polynomial from a function that **is a polynomial** then it’s resulting taylor polynomial will be given by that **same function in terms of $(x-x_0)$ instead of x**

## Taylor remainder:
> [!NOTE] Definition: 
>  We call Taylor remainder of order n at $x_0$ of the function f to the difference:
>  $$
>  R_{n,x_0}f(x) = f(x) - P_{n,x_0} f(x)
>  $$

**Remarks:**
+ This implies: $R_{n,x_0}f(x) = o((x-x_0)^n)$ #duda : Why?


> [!NOTE] Theorem: **Lagrange form of the remainder**
> $$
> R_{n,x_0}f(x) = \frac{f^{n+1)}(t)}{(n+1)!}(x-x_0)^{n+1}
> $$

This means that the remainder for some degree n of the polynomial is equal to the value of the next term of the polynomial.


