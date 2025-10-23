---
aliases:
  - Algorithm - Davis-Putnam-Logemann-Loveland
  - Algorithm - DPLL
  - DPLL
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-13
sr-interval: 2
sr-ease: 248
---
# Algorithm - Davis-Putnam-Logemann-Loveland

> [!NOTE] Intro:
> Algoritmo usado para resolver problemas SAT 

Este algoritmo es equivalente a realizar una búsqueda de [[1732114607 - Algorithm - Primero en profundidad|Algorithm - Primero en profundidad]] con todas las posibilidades de la fórmula lógica. 
+ Se va creando la tabla lógica
+ Permite **obtener todas las posibles soluciones** en el caso de que no se pare el algoritmo al encontrar una solución. 
  
> Por ejemplo: En este caso se probaría con: 
> $$p = T , q= T, t = T$$
>  Se llegaría a una fórmula falsa así que se haría backtracking:
> $$ t = \perp$$
>  Se obtendría una fórmula verdadera
>   ![[1733918229 - Algorithm - Davis-Putnam-Logemann-Lovelandj.png]]

## Eficiencia: 
**TIEMPO:** Exponencial 

**MEMORIA:** Si se expande el arbol completo para encontrar todas las posibles soluciones se guardarán $2^n$ posibilidades nodos (Lógica booleana => Dos posibles ramificaciones)
$$
O(2^n)
$$

***