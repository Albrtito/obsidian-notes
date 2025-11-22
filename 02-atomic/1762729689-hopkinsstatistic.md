---
aliases:
- hopkins statistic
tags:
- ml
---
# hopkins statistic
> [!info] Intro: 
> Used to test if some data is randomly distributed and if no, if it could be used for clustering.

>[!example] Dictionary:
> - $u_{i}$-> The minimum distance of $y_{i}\in Y$ to its nearest neighbour in X
> - $w_{i}$-> The minimum distance of $x_{i}\in X \subseteq X$ to its nearest neighbour in X. Where $x_{i}$ is different from the neighbour in X (the sample was done without replacement)

Really straightforward actually, compare some data against random data. Lets see how.

Let X be a set of n data points
1. Generate a random sample X of m << n data poitns sampled without replacement from X
2. Generate a set Y of m uniformly randomly distributed data points
3. Compare how far are both samples from the original points. (Hoping that the ones sampled from the original points are closer)
   This comparisson is done in the following way:
$$
H = \frac{\sum_{i=1}^m u_{i}^d}{\sum_{i=1}^mu_{i}^d + \sum_{i=1}^mw_{i}^d}
$$
**where:**
 - The result can be:
	 - 0.01 to 0.3 -> Data is evenly spaced but with no cluster tendencce
	 - Around 0.5 -> Uniformly random distributed
	 - 0.7 to 0.99 -> High tendency to cluster

***
### Up
- [[1762729222-clustervalidity|cluster validity]]
### Down
***