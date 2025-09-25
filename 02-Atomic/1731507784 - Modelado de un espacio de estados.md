---
aliases:
  - Modelado de un espacio de estados
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-29
sr-interval: 22
sr-ease: 230
---
# Modelado de un espacio de estados

> [!NOTE] Intro:
> 1. Un posible conjunto de valores específicos para cada una  de mis variables es un estado que se representa en forma de **nodo**
> 2. Realizar un cambio para obtener un conjunto diferente es una operación, que se representa como **una arista**
> 3. El resultado será un conjunto de nodos (estados) y aristas(operadores) que se puede representar en forma de grafo. 


> [!attention] Pregunta de examen:
> En el examen habrá seguro una **modelización de un problmea de búsqueda con espacios de estado**. 
> 

Modelar un problema de búsqueda con espacio de estados nos permite **obtener un grafo que representa el problema**

Utilizar las siguientes definiciones para realizar el modelado: 

> [!example] Nomenglatura y definiciones: 
> + **Estados:** configuraciones posibles del problema. Representan información **estática**
> 
> + **Operadores:** Transitar entre los estados. 
> 
> + **Vista estática del problema:** La estructura que tienen los estados del problema y la información que en ellos se presenta.
> 
> + **Espacio de problemas:**
> 	+ **Espacio de estados**: Un grafo: G(V,E)
> 	+ **Un estado inicial**, s: 
> 	+ **Min un estado final**, t: Se pueden definir explicitamente o implicitamente. La definición explicita apunta a problemas de **optimización** y la definición implícidta a problemas de **decibilidad.**
> + **Solución:** La solución contiene un conjunto de operadores(transformaciones), en orden, que transforman el estado inicial al final. Esto se ve **representado como un camino en el grafo**

## Representación gráfica: 
Se pueden representar los estaos y operadores como un [[1731511534 - ADT - Graf|Grafo]] en el que los **nodos serán estados** y las **aristas serán los operadores.** 

En esta representación también observamos que las **restricciones se ven representadas como los caminos que no se pueden realizar.**
+ Si no puedo llegar a un nodo desde otro tendremos una restricción. 
***