---
aliases:
  - Definition - Local maximum and minimum points of a function
  - Local maximum and minimum points of a function
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-06-28
sr-interval: 8
sr-ease: 248
---
# Local maximum / minimum point of a function: 

The maximum/minimum points of a function or extrema are key points to understanding the behaviour of a function, how it changes and where it’s maximums values are. 

> [!NOTE] Definition: 
> A point $x_0$ in A is a **local maximum/minimum point** of f in A if $\exists \sigma  > 0$ such as: 
> + $x_0$ is the maximum/minimum value of f in : $A\cap(x_0 - \sigma, x_0 + \sigma)$

**Remarks:**
+ Sigma here is defining an interval in which to study the function. This is the reason we call it **local study**
+ By [[20240615 - 210541 - Theorem - Rolle|Rolle]] we know that for a **continuous bounded function** there must be a maximum and a minimum. However if the function is **not closed or not bounded or not continuous** the existence of a maximum and minimum is **not guaranteed**.

To study these points we need the most important theorem: 

> [!NOTE] Theorem:
> If $x_0$ is a local maximum or a local minimum of f and f is differentiable at $x_0$, then: 
> $$
> f'(x_0) = 0
> $$
+ This means that at the local maximums and minimums there must be **no slope**
+ **CAREFUL:** The opposite is **not true**, the value of the derivative **can be 0 without it meaning that it is a max/min**

## How to find these points: 

### Using the first derivative: 
We can apply the definition of [[20240616 - 141015 - Definition - Increasing, decreasing and continuous functions|Increasing, decreasing and continuous functions]] to obtain the following results: 

+ If the derivative is positive/negative at one side of a point a but negative/positive at the other side → a is a local maximum/minimum
Formally: 

> [!NOTE] Application: 
> **Maximum:**
> If for some $\delta > 0$ we have f’(x) > 0 for x $\in (a - \delta,a)$ and f’(x) < 0 for x $\in (a, a + \delta)$. Then a is a local maximum
>  
>  **Minimum:**
>  If for some $\delta > 0$ we have f’(x) < 0 for x $\in (a - \delta,a)$ and f’(x) > 0 for x $\in (a, a + \delta)$. Then a is a local minimum.


### Using second derivative: 
Using the [[20240616 - 143013 - Second derivative|Second derivative]] and the information on convexity that it gives we can say the following: 

> [!NOTE] Theorem:  
> 1. If f’(a) = 0 and f’’(a) > 0 → **f has a local minimum at a**
> 2. If f’(a) = 0 and f’’’(a) < 0 → **f has a local maximum at a**

**CAREFUL**, when applying it in reverse it is not exactly the same: 

> [!NOTE] Theorem: 
> 1. If f’’(a) exists and f has a local minimum at a **then f’’(a) ≥ 0**
> 2. If f’’(a) exists and f has a local maximum at a **then f’’(a) ≤ 0**



