---
aliases:
  - method-of-undetermined-coefficients
tags:
References:
cssclasses:
---
# Method of undetermined coefficients

> [!NOTE] Intro: 
> This method is used to obtain the particular part of the solution to a non-homogeneous second order, linear ODE. 

## Conditions needed

+ Constant coefficients
+ g(t) has to be one of the following types: $e^{\alpha t}, P(t) \text{ polynomial }, sin(t), cos(t)$

## Method:
A general form will be created for h(x) then the unknowns A and B will be specified for the general form. Based on the type of function that g(x) can be the general forms are the following: 

+ $g(t) = e^{\alpha t} \Rightarrow h(x) = Ae^{\alpha t}$ 
+ $g(t) = sin(\alpha t) \Rightarrow h(x) = Asin(\alpha t) + Bcos(\alpha t)$ 
+ $g(t) = cos(\alpha t) \Rightarrow h(x) = Asin(\alpha t) + Bcos(\alpha t)$ 
+ $g(t) = P_n(t) \Rightarrow h(x) = Q_n(t)$ 
  
Once obtained the expression for h(x) substitute y for h(x), y' for h'(x) and y'' for h''(x) in the initial equation. Once it is all substituted compute the value for the constants A,B,C, etc in the h(x).

Then go back to step 3 and finish solving.

**WHAT IF I DON'T GET ANYTHING?** 
There are some special cases for which when trying to compute the values for A and B all instances of A and B in the equation cancel each other. This means that **the initial guess we made is actually one of the solutions for the homogeneous.** If it's one of the solutions then the initial guess is invalid. We need to change the guess: 

+ First do the homogeneous to check that the initial guess is not going to be an specific solution of the homogeneous
+ **SOLUTION:** Multiply by t all terms of the initial guess until the A and B are not canceled. ( so the first time is by one t, next time t squared, and so on)

***
### Down

### Up
- [[20250623 - 000000 - Second order, linear ODEs|Second order, linear ODEs]]