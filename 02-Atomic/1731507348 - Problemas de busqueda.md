---
aliases:
  - Problemas de busqueda
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2025-02-04
sr-interval: 57
sr-ease: 248
---
# Problemas de búsqueda

## Modelado de un espacio de estados:
El modelado de problemas de búsqueda se realiza siempre como un espacio de estados. Este modelado posee las siguientes características: 

1. Un posible conjunto de valores específicos para cada una  de mis variables es un estado que se representa en forma de **nodo**
2. Realizar un cambio para obtener un conjunto diferente es una operación, que se representa como **una arista**
+ Este modelado se explica en profundidad en su nota: [[1731507784 - Modelado de un espacio de estados|Modelado de un espacio de estados]]
+ Como resultado de este modelado **obtenemos un grafo**
##  Resolución
> [!attention] MAIN IDEA: 
> Dado el [[1731511534 - ADT - Graf|Grafo]] G(V,E) obtenido utilizamos un [[1732193365 - Algoritmos de busqueda|Algoritmo de busqueda]] para generar el árbol de búsqueda $T_G(s,t)$ que muestra el resultado del problema. 
> 

*** 
**Esta parte habría que añadirla a una nota a parte**
### Árboles de decibilidad:
Definimos dos factores de importancia de los árboles de decibilidad:
1.  factor de ramificación: Lo ancho que puede llegar a ser el arbol (anchura max)
2. factor de profundidad: Lo alto que puede llegar a ser el arbol. 

***