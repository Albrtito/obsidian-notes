---
aliases:
- reduction of candidates in rule association mining
tags:
- ms
---
# reduction of candidates in rule association mining
> [!info] Intro: 
> This note explains ways reduce the number of possible candidates (possible itemsets from which then create rules in ARM).  

>[!important] Properties:
> 1. **anti-monotone property:** In order to do so we first need to realize that any subset of an itemset has at least the same support or more as its parent. $$ \forall X,V: (X\subseteq  Y) \Rightarrow s(X) \geq s(Y)$$


Same thing works in the other direction. If a subset has some support, then any superset that contains it needs to have that support or less. 
This can be used to prune the number of candidates by analising sets from those that only have one item onwards. This is called the **apriori principle**. 

   > If item A has a support of 0.4 then no set containing A can have a greater support than 0.4. 
   > If some itemset already has a support < minsup then we can disregard any set that uses that item. 

Once we have reduced the number of candidates the next step could be to reduce the number of comparisons between the candidates. 
***
### Up
- [[1762530825-frequentitemsetsinarm|frequent itemsets in ARM]]
### Down
- [[1762528990-apriorialgorithm|apriori algorithm]]
- [[1762532451-reductionofthenumberofcomparisonsinarm|reduction of the number of comparisons in ARM]]
***