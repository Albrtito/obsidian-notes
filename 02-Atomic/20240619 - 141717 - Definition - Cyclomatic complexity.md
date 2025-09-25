---
aliases:
  - Cyclomatic complexity
tags:
  - softwareDev
"References:":
  - https://www.geeksforgeeks.org/cyclomatic-complexity/
cssclasses:
---
# Cyclomatic complexity: 
The cyclomatic complexity measures the number of **linearly independent paths**. It is given by the formula: 
$$
M = E - N + 2P
$$
+ M : Cyclomatic complexity
+ E : Number of edges
+ N : Number of nodes
+ P : Number of connected components 

**Remarks:** 
+ During the #softwareDev second course we almost never have separately connected components, this means that the basic formula is to use: $M = E - N + 2$
+ 