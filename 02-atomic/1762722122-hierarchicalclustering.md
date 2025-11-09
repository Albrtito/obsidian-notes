---
aliases:
- hierarchical clustering
tags:
- ms
---
# hierarchical clustering
> [!info] Intro: 
> A clustering approach that focuses on creatinga hierarchical decomposition of the set of data using some criterion

- For this approach the euclidean distance is the one usually used. 

The first question is, how can we measure the similarity of one point to a group points? Do we just use distance? How do we use distance to a group of points?
There are several ways of doing so: 
- **Complete linkage:** Take just the max distance to the group of poitns
- **Single linkage:** Take the min distance to the group of points
- **Average linkage:** Take the average of the distances to the group of points

Now that we have solved that main question the next thing is to look at the **two main hierarchical clustering approaches, Agglomerative and Divisive**. They use opposing strategies:
- **Agglomerative** starts with as many clusters as points, then joins points to create clusters.
- **Divise** starts with one big cluster, then divides it. 


The created clusters are then represented in a **dendogram**. 
> A possible dendogram would look like:
> ![[1762724507-agglomerativehierarchicalclusteringwithcompletelinkagej.png]]

>[!bug] Problems:
> 1. See that in the given example the algorithm joined the two clusters into one big one. If we dont stop, this will always happen. So the thing is when to stop.

> Example with more clusters:
> ![[1762724507-agglomerativehierarchicalclusteringwithcompletelinkagej-1.png]]

In order to **stop the clustering** it is important to look at the lenght of the branches. If the lenght is hight then it means that a **higher difference (Distance)** between the points is being tolerated. We can set a bound for that distance to specify when to stop the clustering. 

As seen in the example above, when the clustering is stoped, the number of clusters is equal to the number of branches neede dto be cut. 
***
### Up
- [[1762721286-clustering|clustering]]
### Down
***