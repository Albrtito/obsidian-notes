---
aliases:
  - Exact ODE
  - First order exact ODE
tags:
  - diffcalc
"References:": 
cssclasses: 
sr-due: 2024-10-12
sr-interval: 4
sr-ease: 150
---
# First order exact ODEs:
Exact ODEs are those that can be written in the form: 
#duda : Esto es así con f solo derivada en x? No me cuadra si luego utilizamos la parcial solo en x para resolver. 
$$
\begin{gather}
M(x,u) + N(x,u)u' =0 \\
\text{and}\\
M(x,u) + N(x,u)u' = \frac{d}{dx}f(x,u(x)) = 0
\end{gather}
$$
And follow the **necessary condition:** 
$$
{\partial M\over \partial u} = {\partial N \over \partial x}
$$
**Remarks:**
+ [[20240528 - 110528 - Separable ODEs|Separable ODEs]] **are exact**: We can write them with the form: 
$$
M(x) + N(u)u' = 0
$$
## General form and solution:
The general solution for this type of equation is: 
$$
f(x,u(x)) = c
$$
This means that in order to find the solution we need to **find f(x,u(x))**

To find f we use [[20240529 - 165329 - Definition - Partial derivatives|Partial derivatives]] based on the following equalities: 
$$
\frac{\partial f(x,u)}{\partial x} = M(x,u)
$$
$$
\frac{\partial f(x,u)}{\partial u} = N(x,u)
$$
1. Choose one of the two equalities stated above. Use it to compute part of f(x)

+ Chosen the first one (partial derivative over x) (the one with M)
$$
f(x,u) = g(u) + \int [M(x,u)] dx
$$
+ Chosen the second one (partial derivative over u)(one with N)
$$
f(x,u) = g(x) + \int [N(x,u)] du
$$
Where g(x) is the **integration constant**

2. From this last step we’ll obtain some expression from f(x,u), this expression can be now derived by the other variable (the one not chosen in the first step)


Both options in order based on the last step:

1. Now derive partially over u. Knowing that it has to be equal to N
$$
\begin{gather}
\frac{\partial f}{\partial u} = \frac{g(u) + \int [M(x,u)]dx }{\partial u}\\
\frac{\partial f}{\partial u} =  g(u)' + {\int [M(x,u)]dx\over \partial u} = N
\end{gather}
$$
Then we can get the value of g(u)
$$
g(u)' = N - {\int [M(x,u)]dx\over \partial u}
$$
$$
g(u) = \int g(u)' du 
$$
Finally this value is inputted in f(x,u) to obtain the complete form of the function.

2. Now derive partially over x Knowing that it has to be equal to M

$$
\begin{gather}
	\frac{\partial f}{\partial x} = \frac{g(x) + \int [N(x,u)]du }{\partial x}\\
\frac{\partial f}{\partial x} =  g(x)' + {\int [N(x,u)]du\over \partial x} = M
\end{gather}
$$
Then we can get the value of g(u)
$$
g(x)' = M - {\int [N(x,u)]du\over \partial x}
$$
$$
g(x) = \int g(u)' du 
$$
Finally this value is inputted in f(x,u) to obtain the complete form of the function.


The final solution for both cases is: 
$$
f(x,u) = c
$$
This can later be rearranged in order to show the implicit form of u. (give u directly as a solution)


