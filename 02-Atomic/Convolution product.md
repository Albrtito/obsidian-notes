---
id: Convolution product
aliases: 
tags:
  - diffcalc
---
# Intro: 
Suppose that we've the [The Laplace transform](The%20Laplace%20transform.md) H(s) = $\zeta\{h(t)\}$ , with H(s) = F(s) G(s) where F(s) = $\zeta\{f(t)\}, G(s) = \zeta\{g(t)\}$ (f,g known)

f.e: 
$$
H(s) = \frac{1}{s^2(s-2)} = \frac{1}{s^2} * \frac{1}{s-2} = \zeta\{t\} * \zeta \{e^{2t}\}
$$
The asked question is: 
**Can we obtain h(t) using the fact that it is the product of other two functions whose transformes are known?**
In this type of cases we can use the convolution product in order to solve this type of problem .

# Definition: 
In general we cannot say the following for the general product and the Laplace transform: 
$$
\begin{gather}
IF\\
H(s) \not= \zeta\{f(t)g(t)\}\\
THEN\\
h(t) \not= f(t)g(t)
\end{gather}
$$
Things change if we introduce a **"generalised" product**
![20240319 - 000000 - Theorem - Convolution](20240319%20-%20000000%20-%20Theorem%20-%20Convolution.md)

**Remark:** We use convolution product to solve some of the IVP problems when the function we have complies with what the conditions of the convolution product. However we could always try first to apply partial fractions and then use the table provided (aulaglobal)
# Practice cases: 
## Example 1: 
$$
H(s) = \frac{1}{s^2}\frac{1}{s-2} = \zeta\{t\} \zeta\{e^{2t}\}
$$
Then: 
$$
	h(t) = \int ^t _0 (t-\alpha) e^{2\alpha}d\alpha
$$
Computing the [20240529 - 132751 - Method -Integration by parts](20240529%20-%20132751%20-%20Method%20-Integration%20by%20parts.md): 
u = $(t-\alpha)$
dv = $e^{2\alpha} d\alpha$
$$
\begin{gather}
	h(t) = [\frac{1}{2}(t-\alpha)e^{2\alpha}]^{\alpha =
	t}_{\alpha = 0} + \frac{1}{2}\int ^t _0 e^{2\alpha} d\alpha =\\
	 -\frac{1}{2}t + \frac{1}{4}[e^2\alpha]^{\alpha = \\
	t}_{\alpha = 0} =\\
	 -\frac{t}{2} + \frac{1}{4} - \frac{1}{4}
\end{gather}
$$
## Example 11: 
**Objective:** Obtain h(t)
$$
H(s) = \frac{a}{s^2(s^2 + a^2)} = \frac{1}{s^2} \frac{a}{s^2+ a^2} = \zeta\{t\}\zeta\{sin(at)\}
$$
Then we can use the convolution product to obtain h(t): 
$$
h(t) = t\ast sin(at) =_{def.} \int_0^t(t-\alpha)sin(a\alpha)d\alpha = _{homework} \frac{at. sin(at)}{a^2}
$$
# Using the convolution product to solve ODE's. 
+ [Using the convolution product to solve ODEs](Using%20the%20convolution%20product%20to%20solve%20ODEs.md)
