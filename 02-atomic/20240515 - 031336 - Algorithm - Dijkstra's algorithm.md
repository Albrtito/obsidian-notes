---
aliases:
  - Algorithm - Dijkstra's algorithm
  - Dijkstra's algorithm
tags:
  - discrete
"References:": 
cssclasses:
---
# Dijkstra’s algorithm
Dijkstra’s algorithm is used to **find the shortest path that joins an initial vertex s to any other vertex in the graph** given the following conditions: 
+ The graph must be simple
+ The graph must be connected and weighted such as **all weights are positive**
$$
G = (V,E,w): (w_e >0 , \forall e\in E)
$$
The basic idea is to assign to each vertex j two labels that might be temporary or permanent, these labels are $\left(\delta_j, P_j\right)$
+ $\delta_j$ : Estimate of the length of the path from initial vertex($v_o$) to j
+ $P_j$ : Is an estimate of the **predecesor** of the vertex j along the above path. (the previous vertex we’re coming from to reach j)
For programming applications, or even to write down the method, a list with all the vertices and their value (visited or not visited) is used. 

To recap: There will be three important lists:
+ Length from the initial vertex
+ Previous vertex for the shortest path
+ Bool list with visited or not

## Algorithm
Some references to understand the algorithm: 
[Freecodecamp guide](https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/)


