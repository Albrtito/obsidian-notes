---
sr-due: 2024-10-09
sr-interval: 9
sr-ease: 190
date: 2024-02-08
tags:
  - diffcalc
"References:":
  - https://www.youtube.com/watch?v=p_di4Zn4wz4
  - https://ocw.uc3m.es/pluginfile.php/3662/mod_page/content/20/tema-1.pdf
aliases:
  - Definition - Differential Equations
  - Differential Equations
  - DE
---
# Differential equations:

> [!example] Dictionary:
>+ **DE** → Differential equation
>+ **ODE** → Ordinary differential Equation
>+ **PDE** → Partial differential equation
>+ **IVP** → Initial Value Problem
>+ **IC** → Initial Conditions

Differential equations are **relations between a function and its derivatives**
f.e: 
	The following differential equation states a relation between x(t) and its derivatives:
	$$
	x'' + 8x' + 7x = 0
	$$
	Where $x’’$ is the second derivative of x and $x’$ is the first derivative of x. 

> [!NOTE] Diff Equation: 
> A differential equation is an equation where we have a function and the derivative of that same function. Namely: **An equation containing a function and its derivative** 

+ When **solving a differential equation** the **objective is to find the function that satisfies the equation.** 

Solving differential equations can be hard or impossible. However it is really **simple to check whether a solution is right** as it only requires to substitute the values in the initial equation. 

## Family of solutions:

The solution to Differential Equations is usually not only one function but a **family of functions**, infinite solutions, all valid as solutions. 

This family of solutions appears because of how constants are derived. We know that any constant is always derived to 0. Then the value of that constant does not matter for the derivative. However it matters when differencing between functions.

f.e: 
	For this differential equation: 
	$$
	x'' = 2t
	$$
	We find that all functions such as: 
	$$
	x(t) = \frac{t^3}{3} + c_1t + c_2
	$$
	Are solutions for the equation. For all possible values of c1 and c2.

Always, when looking for solutions, an essential part is to look for [[20240528 - 115005 - Lost solutions in a DE|Lost solutions in a DE]]

## ODEs and PDEs
When analysing a differential equation, the resulting function we find can be of two types: 
Lets say that the function is f(x):
1. IF the function **only depends on one independent variable**: $f(x)$ → The differential equation is an **Ordinary Differential Equation** or [[20240307 - 000000 - ODEs|ODE]]
	+ The derivatives of f(x) are **ordinary derivatives**
   
2. IF the function **depends on more than one independent variable:** $f(x_1,x_2,...,x_n)$. 
   Then the differential equation is a **Partial Differential Equation** or [[20240418 - 193416 - Partial Differential Equations (PDEs)|PDEs]]
   The derivatives of $f(x_1,x_2,…,x_n)$ are partial derivatives. 
### Properties:
There are two important properties of DEs: 

> [!NOTE] Order: 
> Highest order deriative in the equation.
> > f(x) + 3 f'(x) + f``(x) = 3: Order 2
> > f(x) + 3f'(x) = 3: Order 1

> [!NOTE] Linearity: 
> An DE is linear when the unknown and its derivatives satisfy:
> 1. Their exponent is equal to 1
> 2. No products or ratios between them
> 3. They are not composed with other functions
>
> > -y + yy' = 3: Non linear. Product between solution and its derivative


## Solving methods: 

There exist a lot of types of DEs for which we can apply **analytic methods** in order to obtain their solutions. 

However most of the DEs are not solvable using these methods. In most of the cases, solvable DEs are lineal.

When we cannot use analytic methods, the best chance is to approach the DE looking for a **similar** equation that we do know how to solve. Then use this similarity to obtain **approximate solutions** using **numeric methods**. 

For the **UC3M DiffCalc course** we’ll be learning analytic methods with a quick mention to the numeric ones at the end of the course. 