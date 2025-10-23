---
aliases:
  - Algorithm - Davis-Putnam
tags:
  - heuri
References: 
cssclasses:
---
# Algorithm - Davis-Putnam

> [!NOTE] Title
> Algoritmo para la resolución de problemas de satisfabilidad lógica. 

1. Elegir un literal l de F
2. Aplicar [[1733916831 - Metodo de resolución SAT|Resolucion SAT]] → Res(F,l), anotando la variable que usamos y la cláusulas involucradas (tanto de F como las nuevas que se crean)
3. Si resulta $\{\emptyset\}$ → **UNSAT**
4. Si resulta $\emptyset$ → **SAT** → **Ir a 6**
5. **Ir a 1**
6. Considerar las cláusulas en orden inverso para ir viendo que valor deberá de tomar cada variable.

## Eficiencia: 
#duda Esto esta bien?
**Tiempo:** Resolución entiempo cuadrático
$$
O(n^2)
$$
+ Para n variables atómicas/binarias

**Memoria:** Complejdiad exponencial?
$$
O(2^n)
$$
## Ejemplos: 

![[1733917531 - Algorithm - Davis-Putnamj.png]]

![[1733917531 - Algorithm - Davis-Putnamj-1.png]]

***