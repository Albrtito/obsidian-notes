---
aliases:
  - Problemas de satisfaccion de restricciones
  - CSP
  - Problemas CSP
tags:
  - heuri
  - incomplete
References: 
cssclasses:
---
# Problemas de satisfacción de restricciones

> [!NOTE] Intro: 
> En esta nota veremos como se modelan y se resuelven los problemas de satisfacción de restricciones.  


Una **red de restricciones** (una tarea de satisfacibilidad de restricciones) es $X_iD_iC$ donde:
- $X = \{x_i\}_{i=1}^n$ son sus variables
- $D = \{D_i\}_{i=1}^n$ con el dominio de $x_i \in X$
- $C = \{R\}_{j=1}^m$ son las restricciones. Pueden ser binarias o con n-elementos

Una restricción $R_{ij}$ es una relación binaria entre $x_1 \text{ y } x_j$ que nombra las combinaciones $(a_i, a_j)$ que son permitidas $a_i \in D_i \space \space a_j \in D_j$

Una **instanciación** es una asignación de valores a $S \subset X$ :
- $S \subset X$: instanciación parcial
- $S = X$: instanciación total

**Objetivo**: dada $(X_iD_iC)$ encontrar una instanciación total que sea compatible con todas las restricciones.

Un problema clásico y una forma de resolverlo es el [[1759830817-nqueensproblem|n queens problem]].

## Grafos en Satisfacción de restricciones

**Grafo de restricciones**: $G(V, E)$ donde $v_i \in V_i, \space \forall x_i \in X$ y $e_{ij}: v_i \rightarrow v_j, \space e_{ij} \in E, \space \forall x_i, x_j; \space R_{ij} \neq \emptyset$

**Arco-Consistencia**: especialmente útil para problemas con dos variables. $x_i$ y $x_j$ son arco-consistentes sí y solamente sí: $$\exists \space a_j \in D_j; \space \forall a_i \in D_i \rightarrow (a_i, a_j) \in R_{i,j}$$Es decir, si existe un valor común en los dos dominios que cumpla una restricción entre dos variables.

*Punto Fijo*: ejecución del algoritmo, hasta que el dominio de las variables no cambie (se ha llegado a un resultado final).

>[!DANGER]
>No es lo mismo verificar la arco-consistencia de $(x_i, x_j)$ que de $(x_j, x_i)$ (en el primer caso eliminamos dominios de $x_i$, mientras que en el segundo lo hacemos respecto a $x_j$). La Arco-Consistencia es **direccional**.

**Camino-Consistencia**: útil para problemas con tres variables, somos capaces de resolver la insatisfacibilidad antes de computar todo el problema. $x_i$ y $x_j$ son camino-consistentes respecto de $x_k$ (variable de referencia) sí y solamente sí:
$$\forall (a_i, a_j) \in R_{ij}; \space \exists \space d_k \in D_k; \space (a_i, a_k) \in D_{i, k}; \space (a_j, a_k) \in R_{jk}$$
El Camino-Consistencia **no es direccional**.
 
>[!NOTE]
>Si se nos pide comprobar la Arco-Consistencia/Camino-Consistencia, debemos de ejecutar el algoritmo correspondiente. Al final, debemos de comprobar si $D_i$ se queda vacío $\rightarrow$ entonces **no serán Arco-Consistentes/Camino-Consistentes**.

>[!QUESTION] ¿Podemos aplicar Camino-Consistencia a un problema de cuatro o más variables?
>No. Tenemos que hacer varios Caminos-Consistencia entre las distintas variables.






***