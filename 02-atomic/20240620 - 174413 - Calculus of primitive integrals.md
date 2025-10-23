---
aliases:
  - Calculus of primitive integrals
tags:
  - calc
"References:": 
cssclasses:
---
# Calculus of primitive integrals: 

This note collects methods for the calculus of primitive integrals.
We’ll take the following list of integrals as elementary primitive integrals: 
+ [[20240620 - 174539 - Elementary primitive integrals|Elementary primitive integrals]]

## Direct integration: 
Direct integration uses the definition of the elementary primitive integrals as well as the following two properties in order to obtain the value of the integral directly from the definition: 


> [!NOTE] Theorem: Linearity of integration 
> The integral operator is lineal, thismeans that for two functions f(x) and g(x) and a constant K we have:
> $$
> \begin{align}
> &1. \int (f(x)+g(x)) dx = \int f(x) dx + \int g(x)dx \\\\
> &2. \int Kf(x)dx = K\int f(x) dx
> \end{align}
> $$


## Integration by parts: 
See: [[20240529 - 132751 - Method -Integration by parts|Integration by parts]]

## Rational functions: 
In order to compute the integral of a quotient such as: 
$$
\int \frac {P(x)} {Q(x)}
$$
The method to use is applying [[20240620 - 170611 - Method - Partial Fractions|Partial Fractions]] in order to simplify the integral into smaller and easier pieces separated by sums.

## Change of variable 
Apply [[20240529 - 135228 - Method - u-substitution|u-substitution]] method in order to simplify the integral. 

## Trigonometric integrals: 
