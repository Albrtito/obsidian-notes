---
aliases:
  - Algorithm - Primero en amplitud
  - Primero en amplitud
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-11-24
sr-interval: 2
sr-ease: 228
---
# Algorithm - Primero en amplitud

> [!NOTE] Intro: 
>  Nunca expande un nodo a profundidad d hasta que no ha expandido todos a la profundidad (d-1). 
>  > Se va buscando **por capas**, primero a profundad 1, luego 2, 3, 4 …
>  
## Pseudocódigo: 
1. Genera el nodo original y guárdalo en la lista 
2. Expandir el primer nodo de la lista. Al expandir lo eliminamos de la lista. 
	+ Obtener sus sucesores y append to the list 
	+ Esta la meta entre los sucesores?
		+ SI: **HALT**
		+ No:**Vuelvo al paso 2**


> [!attention] Remark: 
>  + La lista será **una cola**, **LIFO** (Last in first out)
>  + Al ser la lista una cola se implenta con **un BUCLE**: `while true`

## Propiedades: 

**Admisibilidad y completitud:**
+ Este algoritmo será **completo** pues siempre encontrara una solución 
+ El algorimo será **admisible** si y solo si **todos los operadores tienen el mismo coste**

**Remarks:**
+ Al encontraruna solución a este algoritmo a profundad d, se asegura que **no existe ningua solución a profundidad menor que d** puesto que todos los nodos a menor profundidad ya se han analizado. 

## Eficiencia: 
### Tiempo: 
El tiempo de ejecución de este algoritmo se guía por el **tiempo requerido para expandir un nodo**. 

Para el **left most** nodo en de máxima profundidad d. Este será el mejor caso dentro de todos los peores casos con los que nos podemos encontrar. 
Para generar este nodo tendremos que generar $\sum_{i = 0}^{d-1} b^i$ nodos donde d es la profunidad máxima del arbol. 

Para el **right most** nodo de la máxima profundida, el peor de los casos dentro de todos los peores casos con los que nos podemos encontrar. 
Para generar este nodo tendremos que haber generado $\sum^{d}_{i =0} b^i$

Podemos expresar este último caso en forma de notación: $O(b^b)$
### Memoria: 
Como para obtener el  **right most**  nodo en el peor de los casos tendremos que mantener en memoria todos los nodos de ese útlimo nivel, esta cantidad de nodos máxima será de: $b^d$ .
Entonces la complejidad de memoria de este algoritmo será:  $O(b^d)$ 

**Remark:**
+ Esto quiere decir que la complejidad de memoria es **exponencial y por ello malísima**


> [!check] Duda: Y si el factor de ramificación no es constante?
> Para todos estos cálculos definimos el factor de ramificación como el **número medio de sucesores**. 
> > Esto no es del todo cierto pq hay un límite y un calculo matemático relacionado aquí que no estamos teneindo en cuenta. 
> > 




***