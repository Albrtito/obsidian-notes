---
aliases:
  - Minimum weight spanning tree
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-05-21
sr-interval: 4
sr-ease: 270
---
# Minimum weight spanning tree
There are several possible [[20240515 - 025717 - Definition- Spanning subgraph|Spanning subgraph]]s of any graph G, however the spanning tree graph of G is a subgraph that follows the following definition: 

> [!NOTE] Spanning tree
> The spanning tree of a connected graph G is a subgraph of G that: 
> + Is a tree
> + Contains all vertices of G

For unweighted graphs we can leave it there, however when the graph is weighted we can obtain the minimum-weight spanning tree where the sum of the weights of all the edges is as minimal as possible. 

> [!NOTE] Minimum-weight spanning tree
> Connected weighted graph G = (V,E,w) is a spanning tree T = (V, A) of G such that: 
> $$
> w(A) = \sum_{e\in A} w(e)
> $$
> takes the minimum possible value

In order to obtain this minimum-weight spanning graph we can use two algorithms. 
## Algorithms to obtain the minimum-weight spanning tree: 
+ [[20240515 - 030554 - Algorithm - Prim's Algorithm|Prim's Algorithm]]
+ [[20240515 - 030836 - Algorithm- Kruskal's algorithm|Kruskal's algorithm]]