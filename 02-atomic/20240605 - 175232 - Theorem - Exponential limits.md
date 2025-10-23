---
aliases:
  - Theorem - Exponential limits
  - Exponential limits
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-06-24
sr-interval: 4
sr-ease: 210
---
# Exponential limits theorem: 

> [!NOTE] Theorem: 
> **If**:
> + $lim_{x\rightarrow \alpha} f(x) = 1$
> + $\lim_{x\rightarrow \alpha} g(x) = \infty / -\infty$
>   
> **Then:** 
> $$
> lim_{x\rightarrow \alpha}(f(x))^{g(x)} = e^{\lim_{x\rightarrow \alpha}(f(x) - 1)g(x)}
> $$
> **Remark:**
> There is no restriction for which value $\alpha$ can take. $x_0, x_0^+, x_0^-,\infty , -\infty$

**f.e:**
$$
\lim_{x\to\infty}\left(\frac{2x+3}{2x-7}\right)^{x+5}=\mathrm{e}^{\lim_{x\to\infty}(x+5)\frac{10}{2x-7}}=\mathrm{e}^{5}.
$$

