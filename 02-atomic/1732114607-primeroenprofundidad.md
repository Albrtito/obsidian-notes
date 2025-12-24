---
aliases:
  - Primero en profundidad
  - dfs
tags:
  - heuri
References:
cssclasses:
sr-due: 2024-12-26
sr-interval: 19
sr-ease: 228
---
# Primero en profundidad

> [!NOTE] Intro: 
> Expande el primero de los nodos recién generados hasta que se encuentra la meta o se alcanza una profundidad máxima $d_max$ 
> + Necesitamos la profundidad máxima para no generar infinitamente profundizando en un nodo. → **No mola tener parámetros pero es necsario**
> + Esto es un algoritmo **memoryless**, esto quiere decir que no guardamos los caminos guardados, solo el que estamos guardando como “mejor”.

## Pseudocódigo: 
1. Generamos el nodo inicial y lo guardamos en la lista 
2. Expandimos el primer nodo de la lista, lo eliminamos de la lista. 
	-  Si el nodo se encuentra a una profundidad igual o mayor a $d_{max}$ lo eliminamos de la lista y **volvemos al paso 2**.
	+ Obtenemos los sucesores y los metemos en la lista en la primera posición cada vez que obtenemos un sucesor → **STACK**
	+ Esta la meta entre los sucesores=
		+ SI: **HALT**
		+ NO: **Vuelvo al paso 2**


> [!attention] Remark: 
>  + La lista es un **stack**, **FIFO**. **pila**.
>  + Al ser esto una pila se **implementa con funciones RECURSIVAS**

## Propiedades:

**Admisibilidad y completitud:**
+ Este algoritmo **no es complejo** puesto a que si la **solución esta más abajo que la distancia máxima no la encuentro**
+ Si el algoritmo no es complejo entonces **no es admisible**. 

## Eficiencia: 
### Tiempo: 
Obtenemos una complejidad de tiempo: $O(b^d)$  por la mismas razones que las que tenemos en el [[1732112181 - Algorithm - Primero en amplitud|Algorithm - Primero en amplitud]].
### Memoria: 
En el peor de los casos he creado una línea de profuncidad hasta la profundida d (máxima profundidad del arbol). Obengo entonces $bd$ nodos en memoria. 
La complejidad de memoria será: $O(bd)$ 

Si aplcamos **lazy evaluation** no generaremos más que el siguiente nodo por el que vamos a lanzarnos en la profundidad. 
En este caso obtenemos $O(d)$ espacio de memoria requreido en el peor de los casos. 

**Remark:**
+ Tener tan **poco requremiento de memoria** es la razon por la que elegimos este algoritmo. 


***