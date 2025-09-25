---
aliases:
  - Exercises - First order ODEs
tags:
  - diffcalc
"References:":
  - "[[20240528 - 121302 - First order linear  ODE|First order, Linear  ODE]]"
cssclasses:
  - page-manila
sr-due: 2024-10-17
sr-interval: 13
sr-ease: 208
---
# Exercises - First order, linear ODEs

## 1. $u’ + u = 2e^{-x} + x^2$

**Homogeneous:**
$$
u' + u = 0
$$
$$
{u'\over u} = -1
$$
$$
u_h = e^{-x}
$$
**Particular:**
$$
\begin{gather}
u_p = e^{-x}\int e^x F(x)\\
u_p = e^{-x}\int e^x[2e^-x + x^2]
\end{gather}
$$
After integration by parts we get:
$$
\begin{gather}
u_p = e^{-x}[2x+e^x[x^2 -2x -2]] = \\2xe^{-x} + x^2 -2x -2
\end{gather}
$$

**Final solution:**
Sum of the particular and homogeneous parts
$$
u(x) = Ce^{-x} + x^2 -2x -2 + 2xe^{-x}
$$
**Notes:** 
+ Integration by parts is done twice
+ Careful when integrating by parts between the - signs and what is multiplying what when doing one inside of another. 


## 2. $y’ + \frac{y}{x} = x^2 -1$ , with x > 0

**Homogeneous:**
$u_h = Ce^{-\ln x} = {C\over x}$ 

**Particular:** $u_p = e^{-\ln x}\int e^{\ln x}(x^2 -1) = e^{-\ln x}\int (x^3 -x)$

**Final solution:** 
$$
u(x) = \frac{C}{x} + \frac{x^3}{4} + \frac{-x}{2}
$$
**Notes:**
+ Remember: $e^{\ln x} = x$


## 3. $y’ + y\cos (x) = \sin (x) \cos (x)$

**Homogeneous:**
$$
u_h = Ce^{-sin(x)}
$$

**Particular:**
$$
u_p = sin(x) -1
$$
**Final solution:**

$$
u = Ce^{-\sin (x)} - 1 + sin(x)
$$

**Notes:**
+ Apply integration by parts with $e^{sin (x)} cos(x)$ as dv in order to obtain it’s antiderivative easily.

