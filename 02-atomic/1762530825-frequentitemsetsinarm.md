---
aliases:
- frequent itemsets in ARM
tags:
- ml
---
# frequent itemsets in ARM
> [!info] Intro: 
>  If a subset has some support, then any superset that contains it needs to have that support or less. 
>  This can be used to prune the number of candidates by analising sets from those that only have one item onwards. 
>  We'll prune and choose itemsets that are frequent (or have a good support.


Without applying any operations on the possible itemsets bruteforcing this wont be efficient at all. The number of itemsets grows exponentially. To solve this prunning techniques are used, such as:
- [[1762529626-reductionofcandidatesinruleassociationmining|reduction of candidates in rule association mining]]
- [[1762532451-reductionofthenumberofcomparisonsinarm|reduction of the number of comparisons in ARM]]
***
### Up
### Down
***