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
>[!attention] Remarks:
> - For the ms course we'll keep on using complete linkage (max)

Now that we have solved that main question the next thing is to look at the **two main hierarchical clustering approaches, Agglomerative and Divisive**. They use opposing strategies:
- Agglomerative starts with as many clusters as points, then joins points to create clusters.
- Divise starts with one big cluster, then didives it. 


***
### Up
- [[1762721286-clustering|clustering]]
### Down
***