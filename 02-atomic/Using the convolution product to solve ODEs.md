---
Date: 2024-03-19
tags:
  - diffcalc
"References:": 
sr-due: 2024-12-28
sr-interval: 207
sr-ease: 230
---
How is the [Convolution product](Convolution%20product.md) used to solve ODEs?
+ We are given an [Initial value problem](Initial%20value%20problem) 
+ The final function Y(s) is a product (or maybe has a term that's a product) of two transformed functions from which we know their initial functions (see [[#Practice cases]]
# Practice cases: 
## Example 1: 
For the following ODE, find the value of y using the convolution product. 
$$
\begin{gather}
y'' + 4y = g(t)\\
y(0) = 3, y'(0) = 1
\end{gather}
$$
After solving for Y(s) = $\zeta\{y(t)\}$  and for G(t) = $\zeta\{g(t)\}$we get: 
$$
Y(s) = \frac{3s -1}{s^2 + 4} + \frac{G(s)}{s^2 + 4}
$$
Because the transformation we know by the table [DiffCalc_Resources_Laplace_Transforms](../00.References/DiffCalc_Resources_Laplace_Transforms.pdf) needs a to be squared below and non squared above we do the following: 
$$
Y(s) = \frac{3s -1}{s^2 + 4} + \frac{2}{2(s^2 + 4)}G(s)
$$

We can now apply convolution as we know the function g(t) and the function that the term multiplying G is. Then applying it we get that the inverse transform of the second term would be equal to: 
$$
\zeta^-\{\frac{2}{2(s^2 + 4)}G(s)\} = \frac{1}{2} \int ^t_0 sin(2(t-\alpha)) g(\alpha) d\alpha
$$
# Types of exercises that will be provided for the differential calculus course: 
## Type 1: 
Given the function h(t) as an integral function (the type provided by the convolution product), obtain the transform of h(t) as well as the transform of the two functions in the product.
## Type 2: 
Given the transform of a function. Obtain the inverse transform of the functions.