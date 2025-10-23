---
aliases:
  - Theorem - Convolution
  - 1D convolution
Date: 2024-03-19
tags:
  - diffcalc
"References:": 
sr-due: 2024-11-09
sr-interval: 158
sr-ease: 247
cssclasses:
---

> [!NOTE] Theorem: 
> **Conditions:**
> Let 
> $$
> F(s) = \zeta\{f(t)\}
> $$
> $$
> G(s) = \zeta\{g(t)\}: \text{for } s>a (a>= 0)
> $$
> 
> **Consequences:**
> Then :
> $$
> \zeta\{h(t)\} = H(s) = F(s)G(s): (s>a)
> $$
> With: 
> $$
> h(t) = \int ^t_0 f(t-\alpha)g(\alpha)d\alpha
> $$
> This can also be computed with the shift in g instead of f
> $$
> h(t) = \int ^t_0 f(\alpha)g(t-\alpha)d\alpha
> $$

**Remarks:**
+ The independent variable of h is t. This variable is **defined using an integral** (the variable t is used in the range of the integral (from 0 to t))
+ For the function f(t-alpha) we are using alpha as a **shift variable**. 
+ h(x) is an integral function. So **we can compute that function h(t)** 
+ The function h(t) defined with the integral as above is called the **convolution product**
+ **NOTATION:** $h(t) = (f\star g)(t)$.
  This notation is used for the convolution product between two functions. 
  + **$\zeta\{h(t)\}$. which is the L.transform of the convolution product of f and g. Is the product of the corresponding transforms ($F(s) G(s)$)** :This is kind of the key concept of all of this

**Why would we call this operation a product?**
The "generalised" product preserves some of the properties of the standard product between functions...such as: 
+ $f\ast g = g\ast f$
+ $f\ast(g_1 + g_2) = f\ast g_1 + f\ast g_2$
+ $(f\ast g)\ast l = f\ast (g\ast l)$
+ $f\ast 0 = 0\ast f = 0$

However **not all properties hold**, for instance
+ $f \ast 1 \not = f$

f.e: 
	$$
	H(s) = \frac{1}{s^2}\frac{1}{s-2} = \zeta\{t\} \zeta\{e^{2t}\}
	$$
	Then the function h(t) is of the form: 
	$$
	h(t) = \int ^t _0 (t-\alpha) e^{2\alpha}d\alpha
	$$

