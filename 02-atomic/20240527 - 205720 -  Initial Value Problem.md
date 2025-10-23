---
aliases:
  - Initial Value Problem
  - IVP
tags:
  - diffcalc
"References:": 
cssclasses: 
sr-due: 2024-10-05
sr-interval: 1
sr-ease: 132
---
# Initial Value Problem (IVP):

When we are given a [[20240208 - 000000 - Definition - Differential Equations|Differential Equations]] **along with some initial conditions** we have an initial value problem.

**Remark:**
Initial conditions are specific values given to the function represented in the DE and it’s derivatives for some value of it’s independent variables. 

f.e: 
	Given the differential equation: 
	$$
	x'' = 2t
	$$
	And initial conditions: 
	$$
	x(1) = 1; x'(1) = 2
	$$
	We first obtain the **general solution of the DE**: For this example is given: 
	$$
	x(t) = \frac{t^3}{3} + c_1t + c_3
	$$
	And then we use the initial conditions to find both constants: 
	$$
	\begin{gather}
	x`(t)=t^2+c_1 \\
	\Rightarrow x'(1)=1+c_1=2\\\\
	 x(t)=t^3 / 3+c_1 t+c_2 \\
	\Rightarrow x(1)=1 / 3+c_1+c_2=1 .
	\end{gather}
	$$
	$$
	c_1 = 1, c_2 = -1/3
	$$
	We get **one solution** for the initial value problem: 
	$$
	x(t) = t^3 / 3 + t - 1/3
	$$
	
	
	
	
	
