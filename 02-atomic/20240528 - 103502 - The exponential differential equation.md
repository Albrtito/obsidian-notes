---
aliases:
  - The exponential differential equation
  - Exponential differential equation
tags:
  - diffcalc
"References:": 
cssclasses: 
sr-due: 2024-10-13
sr-interval: 11
sr-ease: 170
---
# Exponential Differential equation. 

One of the most important DEs there is is the growth/decay exponential DE. 
This equation is has the following form: 
$$
y' = ay
$$
This means: 
$$
\text{The rate of change of y is proportional to y}
$$
The solution for any a for these types of equations is: 
$$
y(t) = Ce^{at}
$$
We can see that this is true by comparing both expressions: 
$$
\begin{gather}
y' = ay \\
y' = Cae^{at}\\
y' = a(Ce^{at})\\
\end{gather}
$$
Then the expression holds for any C (constant). 

The importance of this equation is huge in DiffCalc because of the immediate solution we can obtain. We’ll see that there are several arithmetic solutions that are based on this proof. 

Lastly: This equation models one of two things, based on the value of a: 
+ a > 0: **Exponential growth**
+ a < 0: **Exponential decay**