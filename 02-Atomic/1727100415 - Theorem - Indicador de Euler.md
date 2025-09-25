---
aliases:
  - Theorem - Indicador de Euler
  - Indicador de Euler
  - Eulers totient function
tags:
  - cripto
  - discrete
References: 
cssclasses: 
sr-due: 2024-12-20
sr-interval: 13
sr-ease: 150
---
# Theorem - Indicador de Euler

> [!NOTE] Definition: 
> El indicador de euler da el número de elementos que tiene el conjunto reducido de restos de n.  
+ **Notation:** $\Phi (n)$ 
## Teorema de Euler: 
A la hora de calcular el indicador de euler de n podemos utilizar el teorema de euler:
$$
\boxed{a^{\Phi(n)}\mod n =1}
$$
Gracias a este teorema podemos deducir la siguiente expresión: 
$$
a^{-1} = a^{\Phi(n)-1} \mod n = 1
$$
+ Esta expresión nos permite **calcular el inverso de a mod n**[^1]
Si n es primo (p), todo se simplifica más aún (según la teoría del indicador de euler): 
$$
a^{-1} = a^{p-2} \mod p
$$


***

[^1]: [[20240520 - 171554 - Definition - Modular arithmetics - Multiplicative inverse of x|Modular arithmetics - Multiplicative inverse of x]]