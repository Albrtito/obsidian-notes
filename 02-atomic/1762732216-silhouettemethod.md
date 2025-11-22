---
aliases:
- silhouette method
tags:
- ml
---
# silhouette method
> [!info] Intro: 
> The silhouette method is used to numerically determine a suitable number of clusters. 
> For an observation, measure the average dissimilarity to its own cluster and the average dissimilarity to the closest cluster it does not belong to.

>[!example] Dictionary:
> - **a(i)->** Average dissimilarity of i to all other objects in A
> - **d(i,C)->** Average dissimilarity of i to all other objects in C
> - **b(i) = $min_{C\not=A}d(i,C)$->** Find closest cluster(that is not the current cluster A),for some point in cluster A

We looking to see that d is large while a is small. Then:
$$
s(i) = \frac{b(i) - a(i)}{max\{a(i),b(i)\}}: -1 \leq s(i) \leq 1
$$
Repeat the calculation for each observation, then average over all observatoins to get Silhouette score
**The closest to 1 the better**

When looking at a visual representation. There is usually a peak indicating what the best number of clusters is. 
***
### Up
- [[1762729222-clustervalidity|cluster validity]]
### Down
***