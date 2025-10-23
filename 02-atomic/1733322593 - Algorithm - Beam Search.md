---
aliases:
  - Algorithm - Beam Search
  - Busqueda en haz
  - Algoritmo de búsqueda beam search
tags:
  - incomplete
  - heuri
References: 
cssclasses:
---
# Algorithm - Beam Search

> [!NOTE] Intro: 
> 
> Se utiliza el **parámetro k:** Igual al número de nodos simultáneamente expandidos
> 
> > Se expanden los k mejores nodos a cada profundidad de forma recursiva. 
> > 
+ El resto de nodos no expandidos no se mantienen en memoria 
+ Se puede ver como un algoritmo de [[1732112181 - Algorithm - Primero en amplitud|Primero en amplitud]] con una restricción de cuantos nodos se pueden expandir por nivel. (Si k = $\infty$ entonces es el algoritmo de primero en amplitud tal cual)
+ **Falta de monotonía** No se encontrará una solución igual o más óptima aumentando el valor de k. Debido a este problema **este algoritmo no se utiliza**

Para implementar este algoritmo se guarda cada grupo de k nodos como un “contenedor” de nodos, guardándolos en un vector. 

## Propiedades: 
+ **Completo:** → NO
  Como se desestiman nodos (se eliminan de la memoria), la función heurística puede haber desestimados estos nodos de forma optimista(se llegaba a una solucion con menos coste). 
+ **Admisible:** → NO
  Si no es completo no es admisible
## Eficiencia: 
+ **Memoria:** Guardamos k nodos por cada nivel expandido, visitamos un número de niveles d. 
  $$
   O(kd)
   $$
 

***