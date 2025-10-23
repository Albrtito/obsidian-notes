---
aliases:
  - Continuity of a single variable function
tags:
  - calc
"References:":
  - "[[Calc_Theory_Continuity.pdf]]"
cssclasses: 
sr-due: 2024-06-26
sr-interval: 6
sr-ease: 170
---
# Continuity of a single variable function:


> [!NOTE] Definition: 
> A function f(x) is **continuous at $x_0$** if: 
> $$
> lim_{x\rightarrow x_0}f(x) = f(x_0)
> $$
> 

## Properties of continuity:
Given f and g continuous at $x_0$ we define the functions as continuous or not (at point $x_0$)
1. $f + g$ is **continuous** 
2. $f\cdot g$ is **continuous**
3. **If:** $g(x) \not = 0$ : $\frac{f(x)}{g(x)}$ is **continuous**
   
4. **If:** g is continuous at f($x_0$) then: 
   $$
   \boxed{lim_{x\rightarrow x_0}g(f(x)) = g(\lim_{x\rightarrow x_0}f(x))}
   $$

If a function f is **not continuous** then we must differentiate between [[20240614 - 122756 - Definition - Discontinuity types|Discontinuity types]]. 

***
## Fundamental theorems:
All main theorems related to continuity can be found here: 
+ [[20240614 - 123442 - Theorem - Continuity theorems|Theorem - Continuity theorems]]

If a function is continuous on (a,b) then it is said to be continuous at any point on the interval. 

For the function to be continuous on the **closed interval** \[a,b\] then the limits for those points from the left and right must agree with it: 
$$
\begin{gather}
lim_{x\rightarrow a^+} = f(a)\\
lim_{x\rightarrow b^-} = f(b)
\end{gather}
$$
The continuity of closed intervals relates directly to one of the main theorems in this area, used to evaluate these intervals. This theorem is the [[20240614 - 123841 - Theorem - Bolzano|Theorem - Bolzano]] and the evaluation on closed intervals is part of the **local study of a function**

## Max and min: 

Given a function f, continuous or not, we can define a maximum/minimum point and value in the following way: 


> [!NOTE] Definition: Maximum/Minimum
> 1. For $c \in A$ such as: 
>    $$
>    f(c) \geq f(x) \forall x \in A
>    $$
>    We say: 
>    + c is a **maximum point**
>    + f(c) is a **maximum value of f on A**
>
>2. For $c \in A$ such as: 
>    $$
>    f(c) \leq f(x) \forall x \in A
>    $$
>    We say: 
>    + c is a **minimum point**
>    + f(c) is a **minimum value of f on A**


## Uniform continuity: 
#duda : No entiendo nada de esta definición 

![[Screenshot 2024-06-14 at 13.32.01.png]]
