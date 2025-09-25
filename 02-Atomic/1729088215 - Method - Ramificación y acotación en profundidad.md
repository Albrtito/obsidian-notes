---
id: 1729088215 - Method - Ramificación y acotación en profundidad
aliases:
  - Method - Ramificación y acotación en profundidad
tags:
  - heuri
sr-due: "2025-01-14"
sr-ease: 232
sr-interval: 56
---
# Method - Ramificación y acotación en profundidad

> [!Attention] Examen: 
> En ejercicios de examen se suele preguntar como: Resolver con variables cumpliendo condiciones de integridad → Quiere decir que son enteras 

## Pasos:

Cuando tenemos que resolver un problmea lineal buscando únicamente números enteros realizamos el siguiente algoritmo, conceptualmente se hace lo siguiente. 

+ Inicializamos la variable B (valor de la función objetivo en la solución encontrada) a $-\infty$

1. Se resuelve el simplex para la región, esperando que alguna solución de las que tengamos sea entera. 
   + **Si $x^* \in \mathbb{N}$, HALT**
2. En el caso de que la solución factible no sea entera, reducimos el conjunto factible a dos subconjuntos. La división la hacemos sobre una de las variables → Aquí hay varios métodos para hacerlo.   
   Esto **ramifica y va creando un grafo con el resultado por simplex para las subregiones creadas**
   
3. Volvemos a calcular el simplex en **cada uno de los conjuntos, esto lo hacemos por profundidad** y vemos si alguno de ellos es entero. 
   
   **Calculamos $z_{F_i} \forall F_i$:** Donde F es una región factible de las que hemos partido. 
   Podemos ver varios casos una vez calculamos la solución a la función objetivo en la región factible:
   
	**Son nodos terminales (no seguimos partiendolos) aquellos que:**
   
	+ Si la región es infactible:  **Esto puede ocurrir pq las restricciones se contradigan entre ellas**
   + $x_{F_i} \in \mathbb{N} \land z_{F_i} > B$ $B \leftarrow z_{F_i}$ : Si la solución encontrada es entera y mayor a la solución guardad en B, la guardamos en B.
   + $z_{F_i} \leq B$ : La solución que encontramos es menor a la máxima solución (la guardada en B)

Volver al paso 2 si encontramos un nodo no terminal y repetir a partir a partir de ahí.

4. **HALT** si todos los nodos son nodos terminales


***
