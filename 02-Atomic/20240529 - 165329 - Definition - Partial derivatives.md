---
aliases:
  - Partial derivatives
tags:
  - calc
"References:":
  - https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives
cssclasses: 
sr-due: 2024-07-03
sr-interval: 22
sr-ease: 264
---
# Partial derivatives
In single variable calculus the derivative is defined as the rate of change in the function for changes in the independent variable: 
$$
df\over dx
$$
This same expression could also be applied to multi-variable functions, for example, for the function: 
$$
f(x,y)
$$
If we compute: 
$$
df\over dx
$$
We are studying the changes in f for variations in x. However we are not taking into account changes in y, another independent variable introduced. We could see that the changes in f for variations in y are given by the following expression: 
$$
df\over dy
$$
However this same thing happens, now we do not take into account changes in x.

In order to represent both changes we use the partial derivatives.
This derivatives have the same meaning that the ordinary ones, however use different symbolisation:

This would be the partial derivative of f with respect to x: The result would be the same as the derivative of f wrt to x. However with this notation we know that f is a multivariable function.
$$
\delta f\over \delta x
$$

> [!NOTE] Definition:
> For the function: 
> $$
> f(x_1,x_2,x_3,...,x_n)
> $$
> It’s partial derivatives are: 
> $$
> \frac{\partial f}{\partial x_i} \forall i \in N
> $$
> 

## Computation of the partial derivatives: 

When solving the partial derivatives of a function f. All independent variables that are not the one stated in the expression are **treated as constants.** This is better understood with an example: 

For the function: 
$$
f(x,y,z) = 2x^2 + y + 4zx
$$
It’s partial derivative with respect to x is:
$$
\frac{\partial f}{\partial x} = 4x + 4z
$$
+ See that y and z are evaluated as constants. The second term goes to 0 (as if y was any Real) and the third term stays as 4z. (as if z was any Real)

## Evaluation of a function with it’s partial derivatives: 

Because each derivative represents the changes in f wrt one of it’s independent variables. For each possible input combinations there is a value for each of the partial derivatives, these values all together represent the total change for that point.

A nice visual example would be  a three dimensional function for which we only take the partial derivatives of two of it’s variables. 
At any combination of values for those two variables we have a the value of the slope of the curve generated from the intersection of a plane in the position of the values used for the variables and the function. 


### Example: 
Given a function f with two independent variables:
$$
f(x,y) = 2x^2 + 3y^4x 
$$
Partial derivative for x
$$
{\delta f\over \delta x} = 4x + 3y^4 
$$
Partial derivative for y
$$
{\delta f\over \delta y} = 12y^3x
$$