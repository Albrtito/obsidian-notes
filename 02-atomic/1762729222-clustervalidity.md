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

In order to do this we compare the data using the **Hopkings Statistic** to see if the data is uniformly distributed (random).
- Values close to 0.5 sugest random data
What we would like to see is data distributed in bimodal|multimodal distributions. 
***
### Up
### Down
***