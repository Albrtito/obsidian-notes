---
aliases:
- cluster validity
tags:
- ms
---
# cluster validity
> [!info] Intro: 
> How do we know that a cluster is a good cluster? We want to evaluate clusters to know:
> - Is it just noise?
> - Compare clustering algorihms
> - Compare two sets of clusters
> - Compare two clusters

## Are there clusters? Clustering tendency
If we try to find clusters in random points, all clustering methods will find some clusters. But there where no clusters. Then how can we know this beforehand to then not apply a clustering algorithm?

In order to do this we compare the data using the [[1762729689-hopkinsstatistic|hopkins statistic]] to see if the data is uniformly distributed (random).
- Values close to 0.5 sugest random data
What we would like to see is data distributed in bimodal|multimodal distributions. 

## How many clusters should there be?
We can always guess, with low dimensional space it is even a nice idea and easy, but what happens when otherwise?
If we look into the 2D example, the most important observation is that the bigger the number of clusters, the smaller the distances from the centroid to the points in the cluster. This means we want to minimize the [[1762731193-withinsumofsquares|WSS]]. 
But if we just add more and more clusters this will be minimized. This is why there are other methods that will use this measure along with some other analysis,such as:
- [[1762731713-elbowmethod|elbow method]]
- [[1762732216-silhouettemethod|silhouette method]]
***
### Up
### Down
***