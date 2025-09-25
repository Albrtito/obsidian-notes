---
aliases:
  - Limit
  - Limits
Date: 2024-03-19
tags:
  - calc
"References:":
  - "[[Calc_Theory_Limits.pdf]]"
sr-due: 2024-11-08
sr-interval: 141
sr-ease: 252
---
# Limits: 

The formal definition of limit explained above is not simple to understand. 
What is saying is:
For any positive epsilon that you can take there is some delta (**that depends on epsilon**) such as the **distance from f(x) to the limit l** is smaller than epsilon and the distance from x to $x_0$ is smaller than delta.

![[Pasted image 20240620145246.png]]

> [!NOTE] Definition:
> **We say that the function f TENDS TO THE LIMIT l** IF when x approaches $x_0$ f approaches l. 
This is written: 
>$$
\lim_{x\rightarrow x_0}f(x) = l
>$$
>
>**Formally** this is written as:
>
**The function f tends to the limit l if:**
>+ $\forall \epsilon > 0$ 
>+ $\exists \delta> 0$
>+ $|f(x) - l| < \epsilon$
>
>
>**Satisfying**: 
>  + $0< |x-x_0| < \delta$
>  
>  
>  
> **On the oder hand: The function f does NOT tend to the limit l if:**
> 
>+ $\exists \epsilon > 0$ 
>+ $\forall \delta> 0$
>+ $|f(x) - l| > \epsilon$
>  
>**Satisfying**: 
>  + $0< |x-x_0| < \delta$
> 

**Remarks:**
 In order to show how to use this last part to prove that a limit is computed correctly we give an example: 
 
 f.e: 
	Example: 2.1. $\quad \lim _{x \rightarrow 4}(3 x-7)=5$ since $|3 x-7-5|=3|x-4|<\varepsilon$ is obtained if we take $\delta=\varepsilon / 3$.

This means that we **do not care** about the values of f far from x = $x_0$ , only the ones close to it. 

+ The definition of limit is based on points inside a [[20240603 - 102925 - Definition - Neighbourhoods|Neighbourhoods]]

## Properties: 

![[20240605 - 161701 - Properties of limits|Properties of limits]]

## Side limits: 
![[20240605 - 162249 - Theorem - Side limits|Side limits]]
## Limits at infty:

![[20240605 - 164028 - Limits at infty|Limits at infty]]



