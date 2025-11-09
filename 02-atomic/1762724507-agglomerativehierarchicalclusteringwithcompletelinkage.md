---
aliases:
- agglomerative hierarchical clustering with complete linkage
tags:
- ms
---
# agglomerative hierarchical clustering with complete linkage
> [!info] Intro: 
> In this type of clustering we use complete linkage (so for each cluster we test we test against the max distance of that cluster) and a hierarchical agglomerative approach(each point starts as its own cluster, then go from that point onwards)

At each repetition we can:
- Create a new cluster joining two points
- Add a point to an existing cluster
- Join two clusters
In order to do so look at the distances from a point to all the points in each of the clusters. Choose the max distance to each cluster. Then compare them and put the point into the min distance cluster.





***
### Up
- [[1762722122-hierarchicalclustering|hierarchical clustering]]
### Down
***