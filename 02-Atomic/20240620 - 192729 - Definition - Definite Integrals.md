---
aliases:
  - Definition - Definite Integrals
  - Definite integrals
tags:
  - calc
"References:": 
cssclasses:
---
### Definite integrals:

> [!NOTE] Definition: 
> For some bounded interval \[a,b] we say that f is **integrable on \[a,b]**, this type of integral is called **definite integral or Riemann integral** of f on \[a,b]. Denoted by: 
> $$
> \int^b_a f = \int_a^b f(x) dx
> $$


**Remarks:**

 + The definite integral represents **the area below the graph of the function f(x) and above the X axis on interval \[a,b]**
 
> [!NOTE] Theorem: Continuous then integrable
> If a function f is continuous on an interval [a,b] then it is also integrable on [a,b].

**Remark:**
+ If f has discontinuities on a **FINITE amount of points inside the interval** it is still integrable on that interval. 
## Solving: 
The solution of definite integrals is given by the **Barrow’s rule:**
![[20240620 - 200345 - Method - Barrow's rule|Barrow's rule]]
## Properties: 

1. We can take constants out and separe the integrals that are composed out of sums and subtractions
> [!NOTE] Theorem: Linearity 
> Given f and g integrable functions on [a,b]
> $$
> \int_a^b c_1 f + c_2 g = c_1 \int_a^b f + c_2 \int_a^b g: c_1, c_2 \in \mathbb R
> $$

2. Absolute value
> [!NOTE] Theorem: Absolute value
> Given f and g integrable functions on [a,b]
> $$
> |\int^b_a f| \leq \int^b_a |f|
> $$
> 

3. The integral in the reverse way is just the negative inverse. With b > a
$$
\int_b^a f = -\int_a^b f
$$
 4. If a function is integrable on some interval, then it is integrable on any subinterval within the first one.
 5. We can divide the integration into parts, so if an interval \[a,b] has a < c < b. The integral that went from a to b can be divided into two integrals. One from a to c another one from c to b. 

