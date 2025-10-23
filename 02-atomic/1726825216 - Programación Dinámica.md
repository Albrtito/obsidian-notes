---
aliases:
  - Programación Dinámica
tags:
  - heuri
References: https://aulaglobal.uc3m.es/pluginfile.php/7277686/mod_resource/content/3/dynamic_programming.pdf
cssclasses: 
sr-due: 2024-12-04
sr-interval: 49
sr-ease: 290
---
# Programación Dinámica
## Biblio:

> Steven S.Skiena: **The algorithm Design Manual**. Ch:8 
> Dejan Zivkovic: **Foundations of Algorithm analisis and Design**. Ch: 7

> [!NOTE] Definición: 
> La programación dinámica es una **técnica bottom-up** en la que se **guardan resultados intermedios** para luego reusarse durante la resolución de un problema. 
+ Util cuando podemos obtener **subproblemas ordenados**. 

La técnica se puede descomponer en los siguientes pasos: 
1. **Descomponer el problema** en subproblemas similares
2. Definir recursivamente la solución óptima del problema 
   
> [!check] Duda: Que significa esto:
> Esto quiere decir que la solución se obtiene de forma recursiva (con funciones recursivas). El backtracking the esta recursividad se ve en el siguiente paso.  

3. Calcular los subproblemas de abajo hacia arriba 
4. Calcular la solución global usando los resultados intermedios

## Ejemplos: 
### Serie de fibonacci: 
![[1726827729 - Defninition - Serie de Fibonacci#Implementación de la serie]]
### All-pairs shortest-path
Dado un grafo G(V,E), obtener el coste del camino más corto entre todos los pares de vértices i y j, D(i,j). 
+ **Algoritmo Floyd-Warshall**
