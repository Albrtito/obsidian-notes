---
Date: 2024-03-12
tags:
  - diffcalc
"References:": 
sr-due: 2024-10-11
sr-interval: 11
sr-ease: 148
---
======# The laplace transform  
 + This technique can be also applied for non-homog. terms with discontinuities(g(t))
+ Useful for ODEs of order higher than 2
+ Transform an initial value problem ode to an algebraic equation 

> [!NOTE] Theorem
> Let f be a function satisfyin some conditions (later), given for t >= 0. The laplace transform of f is: 
$$
> \zeta \{f(t)\} = \int ^\inf _o e^{-st} f(t) dt = F(s)
$$

**Remarks:**
+ f is the function to be transformed (input)
+ F(s) is the output of the transformation. What is called Laplace transform
+ s is the variable on which the new function depends on. (Parameter of the transform)
+ $e^{-st}$ is called **kernel**
+ The integral obtained is improper. 
	**Recall:** [20240620 - 201418 - Improper Integrals](20240620%20-%20201418%20-%20Improper%20Integrals.md)

# Applying the $\zeta$: 
**Remark:** f is **piecewise continuous** on \[ $\alpha, \beta$  \] if f is cont on the interval except for a finite number of points where f has "jumps" (of finite size)
+ Piecewise continuous: This means defined in pieces (definida a trozos)

> [!NOTE] Theorem 
> Let f be a funct such that:
> **CONDITIONS:**
> 1. f is piecewise cont. on 0<= t <= A, $\forall A >0$ 
> 2. $|f(t)| <= ke^{\alpha t}$ for t >= M
> (k >0, $\alpha$, M>0 constants)
> 
>**OUTPUT:**
> The Laplace transform of f($\zeta{f(t)} = F(z))$ exist for s> $\alpha$

**Remarks:**
+ Condition 2 means that "f grows less than some exponential function"
	If this is true f is said of exponential order(for large t)
+ **For #diffcalc we'll always work with functions that satisfy this last theorem**
+ We'll only be able to compute a valid $\zeta$ when $s>\alpha$. The value of $\alpha$ will depend on the practical case.
# Properties of $\zeta$:
## 1. Linearity of $\zeta$
Let f1 and f2 be two functions such that their Laplace transforms exist for $s>\alpha_1$ , $s> \alpha_2$, respectively. Then:
$$
\zeta \{c_1f_1(t) + c_2f_2(t)\} = c_1\zeta\{f_1(t)\} + c_2\zeta\{f_2(t)\}
$$

for z > max $\{\alpha_1, \alpha_2\} (c_1, c_2 \in \mathbb{R})$
+ Sum of functions inside the transform can be separated into two independent transforms. 
+ The multiplication by a constant inside the transformed can be taken out of it(after all it's an integral)
## 2. Transform of derivatives: 

> [!NOTE] Theorem 
> **CONDITIONS:**
>1. Let f be cont. on o <= t <= A, $\forall A > o$ , of exponential order (namely $|f(t)| <= ke^{\alpha t}$) . 
>2. Let f' be piecewise cont. on 0<= t<= A. $\forall A>0$ . 
>
>**OUTPUT:**
>Then $\zeta\{f'(t)\}$ exist for s>$\alpha$ and we've the following transform of f':
$$
\zeta{f'(t)} = s\zeta\{f(t)\} -f(0)
$$
>**CONDITIONS:**
>If the same property is satisfied for f' and f''. 
>**OUTPUT:**
>Then $\zeta \{f''(t)\}$ exist for s> $\alpha$ and we've
$$
\zeta \{f''(t)\} = s^2\zeta{f(t)} - sf(0) - f'(0)
$$


**Remarks:**
+ For #diffcalc course see the [PDF n aula global](https://aulaglobal.uc3m.es/pluginfile.php/6903203/mod_resource/content/1/Laplace_Transforms.pdf) stating the generalised formula for derivatives of order n: $f^{(n)}(t)$

# Practical examples: 
## Remarks:
+ During exams some Laplace transforms will be provided (in the classroom blackboard). Not all of them must be used, students must choose which ones to use for the required exercises.
+ All useful Laplace transforms for the #diffcalc  course are provided in the following [link in aula global](https://aulaglobal.uc3m.es/pluginfile.php/6903203/mod_resource/content/1/Laplace_Transforms.pdf)

## Example 1:
**Initial conditions:**
$f(t) = 1, t>= o$
**Formal definition and solution of the transformation:**

$$
\begin{aligned}
\zeta \{f(t)\} = \zeta \{1\} = \int _0 ^\inf e^{-st} 1 dt = \\ lim_{A\rightarrow \inf} \int_o^A e^{-st} dt = \\
lim_{A\rightarrow \inf} [{-1 e^{-st}\over s}]^{t= A}_{t= 0} =\\ lim_{A\rightarrow \inf} [{-1 e^{-sA}\over s} + {1\over s}]\\
\end{aligned}
$$

**Remarks:** 
+ If s<= 0: Then the limit goes to infinity(**not** conv. : **BAD**)
+ If s>0: Then the limit has the term $1\over s$ (**we like this**)
With s>0 we get: 
$$
\zeta \{f(t) = 1\} = {1\over s}, s>0
$$
+ Based on the definition provided above we know that $\alpha$ = 0
## Example 2: 
**Initial conditions:**
$f(t) = e^{at}, t>= 0 (a\in R)$
**Formal definition and solution of the transformation:**
$$
\zeta \{e^{at}\} = \int ^\inf_0 e^{-st} e^{at} dt = \int ^\inf_0 e^{-(s-a)t} dt = {1\over s-a}, s>a
$$
## Example 3:
**Initial conditions:**

$$f(t) = sin(at), t>= 0 (a\in R, a\not = o)$$

**Formal definition and solution of the transformation:**

$$
\zeta\{sin(at)\} = {a\over s^2+a^2}, s>0
$$


---

