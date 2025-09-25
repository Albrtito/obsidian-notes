---
aliases:
  - Algorithm - Busquedas de el mejor primero
tags:
  - incomplete
  - heuri
References: 
cssclasses:
---
# Algorithm - Busquedas de el mejor primero


> [!BUG] Problemas y sus soluciones: 
> +  Cuando hay costes las soluciones óptimas podrían ser soluciones más largas. Con algoritmos de fuerza bruta estas soluciones mas largas nunca las vamos a encontrar. 
> 
> Este algoritmo sale por consecuencia a los siguientes problemas en los problemas de búsqueda y sus algoritmos. Propone la creación de dos listas.
> 
> 1. **OPEN:** Lista de nodos generados esperando a ser expandidos. Estos nodos se ordenan ascendentemente por una función de prioridad/función de mérito $f(n)$. 
>    
> 2. **CLOSED:** Lista de nodos ya expandidos
> 3. Se sugirere que no nos detengmos cuando encontramos la meta sino cuando **expandimos la meta**. Se crea un criterio que será el **criterio de terminación**, que se cumplirá cuando t(el nodo meta) va a ser expandido.

## La función $f(n)$: 
+ **Algoritmo de heurística pura: (GBFS)** $f = h$ 
  Utilizamos la función heurística. Esto **no nos sirve para encontrar soluciónes óptimas pero se utiliza debido a su valocidad**
+ [[20240515 - 031336 - Algorithm - Dijkstra's algorithm|Dijkstra's algorithm]] $f = g$: Ordenamos según el coste que tiene cada nodo a la meta. 

Podemos juntar ambos tipos, utilizando el valor exacto de g y la estimación de h para obtener una función f: 
$$
f = g + h
$$
**Esta unión da como resultado el algoritmo [[1733324893 - Algorithm - A*|A estrella]]**







***