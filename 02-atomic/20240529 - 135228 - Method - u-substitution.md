---
aliases:
  - u-substitution
  - Method - u-substitution
tags:
  - diffcalc
  - calc
"References:": 
cssclasses:
---
The u-substitution method is useful when there are: 
+ Fractions and quotients
+ expressions such as: $nx^{n-1}(x^n + c)$. Where u can be equal to that expression and the derivative of what's inside the parenthesis can cancel the outside x (keep reading to understand what I mean)
Example, cause it's the best way to understand this
### Example: 
$$
\int 4x[x^2 + 5]^3 : u = x^2 + 5: du = 2x dx
$$
$$
dx = {du\over 2x}
$$
Variable change: **NOTE: We also need to change the derivative**
$$
\int 4x u^3 {du\over 2x} = {2u^4\over 4} + C
$$
Undo the variable change: 
$$
{1\over 2} u^4 + C = {1\over 2 }(x^2 + 5)^4 + C
$$
$$

$$


