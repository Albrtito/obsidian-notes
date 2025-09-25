---
id: Second order, linear ODEs
aliases:
  - Second order, linear ODEs
tags:
  - diffcalc
---
# Second order ,linear ODEs
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
For an ODE: $ay'' + by' + cy = 0 : a,b,c \in \mathbb{R}$ 



Obtain solutions for r.
$$
ar^2 + br + C = 0 
$$
This has a reasoning behind but it is not important or will be asked.
The basic form of each solution will be: 
$$
y_i = e^{xr_i}
$$

From this equation there are 4 possible solutions. 
1. Both solutions are real and different. Then the general solution is given by: 
$$
y(t) )= c_1y_1 + c_2y_2  = c_1e^{xr_1} + c_2e^{xr_2}
$$
2. Solutions are real and the same. Then one of the solutions is multiplied by t to obtain linearity. 
$$
y(t)= y_1 + y_2t + C = c_1e^{xr_1} + c_2te^{xr_1}
$$
3. Solutions are complex: For a complex solution we transform the solution $e^{xr_i}$ using eulers formula. And we get, for the solution $r = \alpha \pm i\beta$
$$
y_i = c_1 e^{x\alpha} cos(\beta x) + c_2 e^{x\alpha}sin(\beta x)
$$


For any of this cases, once obtained the solutions it is necessary to check that they create a matrix with a determinant different from 0. (general solution theorem). This matrix, as said before, is the wronskian. 

## Non-Homogeneous, constant coefficients. 
This equations are of the form: 
$$
ay'' + by' + cy = g(t): a,b,c\in R
$$
 
In this case the coefficients are constant like in the last one but the equation does not equal 0 but a function. This solution is really similar to the #discrete solution for non-homogeneous recursive equations.
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

- [[1750692203 - method-of-undetermined-coefficients|method-of-undetermined-coefficients]]

## Final remarks:
Besides these methods there are other ways of solving without computing the homogeneous then the particular part, the main one uses the laplace transform: 

- [[Using the Laplace transform to solve IVP]]




