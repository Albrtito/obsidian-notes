---
aliases:
  - Side limits
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-08-12
sr-interval: 53
sr-ease: 290
---
# Side limits: 

> [!NOTE] Definition: 
> We say that a **function tends to the limit l FROM THE RIGHT/LEFT** when if x approaches $x_0$ from the right/left f approaches l. 

## Example: 
This is really useful for functions that have two different definitions for points in the right/left of some given point.

For example: $f(x) = 1/x$

![[Pasted image 20240605162902.png]]
When approaching 0: 

+ From the right side, the function approaches +$\infty$. Then 
$$
\lim_{x\rightarrow 0^+} f(x)= \infty
$$
+ From the left side, the function approaches $-\infty$ 
$$
\lim_{x\rightarrow 0^-} f(x)= -\infty
$$





## Theorem: 

> [!NOTE] Theorem:
> The $lim_{x\rightarrow x_0} f(x)$ exists **if and only if** both side limits exists and: 
> $$
> lim_{x\rightarrow x_0^+} f(x) = lim_{x\rightarrow x_0^-} f(x) = l
> $$
> **THEN:**
> $$
> lim_{x\rightarrow x_0} f(x) = l
> $$


