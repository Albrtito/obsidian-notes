---
aliases:
  - Definition - small-o
  - small-o
tags:
  - calc
"References:": 
cssclasses:
---
# small-o
The small-o notation is used to specify when a function is bigger than another one when tending to some value $x_0$. 

Formally: 

> [!NOTE] Definition: 
> We say that a function is small-o of g(x) as $x\rightarrow x_0$ and write: 
> $$
> f(x) = o(g(x))
> $$
> **IF:**
> $$
> lim_{x\rightarrow x_0} \frac{f(x)}{g(x)} = 0
> $$
> 

**NOTE:**
+ This concept is similar to the one we use when dealing with polynomial limits at infty. “If g(x) is greater then it goes to 0.”
+ $o(g(x))$ is **Landau’s notation**

