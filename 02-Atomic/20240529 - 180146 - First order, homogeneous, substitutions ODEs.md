---
aliases:
  - First order, homogeneous, substitutions ODEs
  - Homogeneous, substitutions ODEs
tags:
  - diffcalc
"References:": 
cssclasses: 
sr-due: 2024-10-08
sr-interval: 11
sr-ease: 170
---
# First order, homogeneous, substitutions ODEs
Sometimes we can use an [[20240529 - 135228 - Method - u-substitution|u-substitution]] in order to transform an ODE to a form that we know and can solve. 
There are several known substitutions.

During the DiffCalc course we’ll only look at x/u substitutions.
## x/y Substitutions:

This kind of ODEs are those that can be solved by using a **change of variable**:
u → x/u or u → u/x 

### General form and solution:

All homogeneous non lineal first order ODEs have the following general form: 
$$
M(x,u) + N(x,u)u' = 0
$$
These functions must meet: 
$$
M(kx,ku) = k^nN(x,u)
$$
+ Where n is called **degree of homogeneity**
**NOTE:**
If the function is of the form of y/x substitution, then it proves that it is homogeneous. 

Those that can be solved with an x/u substitution must comply with the following **condition**: 
$$
\begin{gather}
{du\over dx} = u' = F(x/u) \\
\text{or}\\
{du\over dx} = u' = F(u/x) \\
\end{gather}
$$
In order to check that the condition holds, rearrange the equation for u’. 

Once checked that the condition holds we can apply [[20240529 - 135228 - Method - u-substitution|u-substitution]] with the following changes:

### Change of var: 

**Form 1:**
+ y = x/u 

Then u’ is: 
+ $u = x/y$
+ $\frac{du}{dx} = \frac{dx/y(x)}{dx}$

**Form 2:** (preferred form)
With this form the derivative of u is a product instead of a quotient.

+ y = u/x

Then u’ is:
+ $u = y\cdot x$
+ $u’ = x\cdot dy + y \cdot dx$



Finally, the new ODE is [[20240528 - 110528 - Separable ODEs|Separable ODEs]], and therefore solvable.
