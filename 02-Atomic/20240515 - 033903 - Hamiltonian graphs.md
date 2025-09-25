---
aliases:
  - Hamiltonian graphs
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-05-22
sr-interval: 2
sr-ease: 230
---
# Hamiltonian graphs: 
Hamiltonian graphs are those graphs that **contain a cycle on a graph G such that the cycle contains all vertices of G exactly once**

> [!NOTE] Hamiltonian cycle /graph
> The hamiltonian cycle is the cycle on a graph g containing all vertices of G.
> **IF:** A graph admits a hamiltonian cycle **THEN:** It is a hamiltonian graph

**Remark:**
+ We can also find **hamiltonian paths**. Open paths that contain all vertices of G
+ Finding any of these properties is hard in most graphs

## Finding hamiltonian graphs: 
There is one theorem we can follow in order to find whether a graph is hamiltonian or not: 


> [!NOTE] Theorem: Dirac
> **IF** a graph is:
> + Simple
> + n ≥ 3: n = nº of vertices
> + $\forall v \in V: d(v) \geq n/2$
> 
> **THEN:** The graph is Hamiltonian

**Remark:**
+ However this condition is not reversible. Not every hamiltonian graph satisfies the previous relation. 

