---
id: Order 2 linear ODE's
aliases: []
tags:
  - DiffCalc
---
When solving order two linear ODE's there'll be different cases based on how the coefficients of the equation are. There can be constant coefficients (easy ones, we like those) and function coefficients (harder ones we don't like cause they change)
The constant coefficients are a variation of the general case but I'll treat them as a separate case. Anyway the main form of this ODE's is: 
$$
P(t)y''+ Q(t)y'+R(t)y = G(t)
$$
+ In this case t is the independent variable we'll use (instead of x)


> [!NOTE] Theorem: Superposition
> If there are two solutions $y_1$  and $y_2$ then $C_1y_1(t) + C_2y_2(t)$ is also a solution. $\forall C_1, C_2 \in \mathbb{R}$


> [!NOTE] General solution 
> If two solutions are found for the ODE such as they are linearly independent or the determinant of the matrix W is different from 0. 

$$
W (y_1,y_2)(t) = det \begin{bmatrix}  
y_1(t) & y_2(t) \\  
y_1'(t) & y_2'(t)   
\end{bmatrix} = y_1(t)y'_2(t) - y_2(t)y'_1(t) \not = 0
$$

Then there's a general solution for the ODE of the form: 
$$
y(t) = c_1y_1(t)+ c_2y_2(t)
$$
Finally, the [Initial value problem](Initial%20value%20problem) can be used to obtain the values of C1 and C2 given some values of y and it's derivative
**REMARK:** This determinant is called the WRONKSKIAN of those solutions based on who invented it. 


### Homogeneous, constant coefficients
We say the ODE is homogeneous when G(t) is equal to 0. The constant coefficients mean that P(t), Q(t) and R(t) can be replaced by $C_1, C_2 \text{ and } C_3$. Then this type of ODE's are of the form: 
$$
C_1y''+ C_2y'+C_3(t)y = 0
$$

+ When solving this type of equations normally it's asked to solve the [Initial value problem](Initial%20value%20problem) and obtain a concrete solution to it. 
#### Solving: 
The objective is to find two solutions to the equations as the general solution will be the sum of those. 
The easy thing about constant coefficients is the solution is to **just compute the solutions of the following second degree equation:** 
For an ODE: $ay'' + by' + cy = 0 : a,b,c \in \R$ 



Obtain solutions for r.
$$
ar^2 + br + C = 0 
$$
This has a reasoning behind but it is not important or will be asked.
From this equation there are 4 possible solutions. 
1. Both solutions are real and different
	The general solution is the same as the theorem
2. Solutions are real and the same
	Multiply by t one of the solutions in the general form
3. Solutions are both complex
4. One solution is  complex the other one is real
For any of this cases, once obtained the solutions it is necessary to check that they create a matrix with a determinant different from 0. (general solution theorem)
Once this is checked, give it the form of the general solution and you're finished.  The solution will be of the form: 
1. Both real solutions and different
$$
y(t) = c_1y_1(t)+ c_2y_2(t)
$$
2. Both real and same: 
$$
y(t) = c_1y(t)+ c_2ty(t)
$$
## Non-Homogeneous, constant coefficients. 
This equations are of the form: 
$$
ay'' + by' + cy = g(t): a,b,c\in R
$$
 
In this case the coefficients are constant like in the last one but the equation does not equal 0 but a function. This solution is really similar to the #Discrete solution for non-homogeneous recursive equations.
1. Obtain the homogeneous solutions assuming that g(t) = 0
2. Obtain the specific solution that will be later added. 

The general form of the solution is: 
$$
g(t) = C_1y_1(t) + C_2y_2(t) + h(t)
$$
+ h(t) is the specific solution that is created because of the non-homogeneous part.
+ The y1 and y2 are obtained like in the homogeneous equations, assuming that for that computation g(t) = 0
#### Solving: 
1. Obtain the homogeneous solution. (general solution)
2. Obtain h(t)
3. Add h(t) to the homogeneous solution and equal it to g(t)
**Then the important question is: How do I obtain h(x)?** 
There are two methods: 
##### Method 1: 
**Conditions:** 
+ Constant coefficients
+ g(t) has to be one of the following types: $e^{\alpha t}, P(t) \text{ polynomial }, sin(t), cos(t)$

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
+ **SOLUTION:** Multiply by t al terms of the initial guess until the A and B are not canceled. ( so the first time is by one t, next time t squared, and so on)

##### Method 2: 
**Conditions:** 
+ It works for any coefficients
+ It works for any g(t) 



## Non-Constant coefficients: #Duda 
> [!NOTE] Theorem: Existence and uniqueness
> There's always a solution for non-constant coefficient with some initial conditions

