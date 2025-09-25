---
aliases:
  - Metodo de resolución SAT
  - Resolucion SAT
tags:
  - heuri
References: 
cssclasses:
---
# Metodo de resolución SAT


> [!NOTE] Intro: 
> Este método sirve para resolver problemas de satisfabilidad lógica.  

$$Res(F, l) = \begin{cases}  F &  l \notin F \\ F \backslash l & l \in F \space \text{y l es puro} \\ (C_1 \lor C_2) & l \in F, \text{l no es puro}\end{cases}$$
$$\text{F = Formula y l = Literal}$$
Lo que nos está diciendo este método es: Dadas dos cláusulas que contienen al literal l: 
+ Si el literal es puro, puedes eliminar todas las cláusulas que contengan ese literal 
+ Si el literal no es puro, entonces existen dos cláusulas, una de ellas tendra $l$ y la otra $\hat l$, se pueden sustituir esas cláusulas por una nueva: $(C_1 \lor C_2)$

> por ejemplo: para $F = (x_1 \lor \overline{x_2} \land (\overline{x_1} \lor \overline{x_2} \lor x_3))$, entonces $Res(F, \overline{x_2}) = \emptyset$.     


> [!bug] Problema: 
> Este método no resuelve siempre el SAT, simplemente elimina el literal elegido. Se pueden generar hasta $(\frac{n}{2}^2)$ clausulas. 

***