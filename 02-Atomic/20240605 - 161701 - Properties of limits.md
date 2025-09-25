---
aliases:
  - Properties of limits
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-07-16
sr-interval: 26
sr-ease: 250
---
# Properties of limits: 

> [!NOTE] Uniqueness of the limit:
> If a limit exists, it is unique. If l and m both satisfy as the limits of f in $x_0$, then l must be equal to m: l = m

Given: 
$$
\begin{gather}
lim_{x\rightarrow x_0}f(x) = l \\\\
\lim_{x\rightarrow x_0} g(x) = m
\end{gather}
$$
1. A constant can be taken out of the limit
   $$\lim _{x \rightarrow x_0}(c f(x))=c \ell, \quad if: c \in \mathbb{R}$$
2. Limit of the sum is equal to computing limits apart.
   $$\lim _{x \rightarrow x_0}(f(x)+g(x))=\ell+m$$
3. Limit of the multiplication of two functions is equal to the multiplication of the both limits.
   $$\lim _{x \rightarrow x_0}(f(x) g(x))=\ell m$$
4. Limit of the quotient of two functions is equal to the quotient of the limits
   $$\lim _{x \rightarrow x_0} \frac{f(x)}{g(x)}=\frac{\ell}{m}, \quad if: m \neq 0$$
5. The **limit of a composition** is obtained directly if all limits involved exists and  the operations make sense. 
$$
\begin{gather}
\lim _{x \rightarrow x_0} f(x)=\ell \quad \text { and } \quad \lim _{x \rightarrow \ell} h(x)=m \quad\\
 \Longrightarrow \quad \lim _{x \rightarrow x_0} h(f(x))=m \text {. }
\end{gather}
$$
+ This can be used for: 
	+ **Square roots:**
	   $\lim_{x\rightarrow x_0} \sqrt{f(x)} = \sqrt{l}: l>0$
	  
	+ **Powers:** 
	  $\lim_{x\rightarrow x_0} {f(x)}^{h(x)} = l^m: l^m \not = 0$
	  
	+ **Logarithms:** 
	  $\lim_{x\rightarrow x_0} \log_a{f(x)} = \log_a{l}: l>0 ,a>0$

