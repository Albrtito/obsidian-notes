---
aliases:
- apriori algorithm
tags:
- ms
---
# apriori algorithm
> [!info] Intro: 
> Algorithm (pseudocode) for the apriori principle. 


> [!important] Pseudocode 
> 1. Set minsup to some value, set k=1
> 2. Generate frequent itemsets of lenght 1
> 3. Repeat until no new frequent itemsets are identified:
> 	1. generate lenght k+1 candidate itemsets from lenght k frequent itemsets
> 	2. Prune candidate itemsets containing subsets of lenght k that are infrequent
> 	3. Count the support of each candidate
> 	4. Eliminate candidates that are infrequent leaving only those that are frequent
> 	5. Increment k by 1


***
### Up
### Down
***