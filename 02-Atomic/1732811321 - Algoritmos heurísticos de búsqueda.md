---
aliases:
  - Algoritmos heurísticos de búsqueda
tags:
  - incomplete
  - heuri
References: 
cssclasses:
---
# Algoritmos heurísticos de búsqueda

> [!NOTE] Función heurística: 
> Una función heurística devuelve, para todos los estados de un problema de búsqueda, un número real. 
> Este número real es **una estimación del coste desde el esado S a la meta**
> Definimos e la función como: 
> $$
> h: S \rightarrow \mathbb{R}^+
> $$

## Propiedades: 
+ **Admisibilidad:** Decimos que una heurística es admisible si **no se sobreestima el coste para ningún estado**. 
  > Esto lo podemos analizar utilizando los últimos estados de la búsqueda. 


***