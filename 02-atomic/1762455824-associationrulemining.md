---
aliases:
  - association rule mining
  - ARM
tags:
  - ms
---
# association rule mining
> [!info] Intro: 
> The general idea of association rule mining is based on how some events are related with others. So when learning about how events are happening, algorithms can create rules relating them. 
> > When people buy ice cream then they usually also by cookies.
> > {Ice cream} -> {Cookies}
> The objective of association rule mining is to **find the relations**

This could be used to order a warehouse based on which items are stored together or for marketing applications. 

>[!example] Dictionary:
> - **Itemset->** An itemset is a colletion of one or more items
> - **k-itemset->** An itemset with k items
> - **Relation->** The relation between two itemsets is defined as $X \to Y$ where X and Y are both itemsets.
> - **support count $\sigma$->** Frequency of occurence of an itemset 
> - **support|s->** Fraction of transactions that contain an itemset $$s = \frac{\sigma(X,Y)}{|T|}$$
>   **where:**
> 	- **T->** Total number of observations
> - **frequent itemset->** An item whose support is greater than or equal to a minsup threshold. 
> - **minsup->** Minimal support threshold
> - **minconf->** Minimal confidence threshold
> - **confidence|c->** Measures how often items in Y appear in transaction that contain X. 
>   $$
> c = \frac{\sigma(X,Y)}{\sigma(X)}
$$


>[!important] Properties:
> 1. **Given transitivity {A,B} -> {C}; {A,C}->B and {C,B}->A:** The support for both cases will be the same (see that we are just joining and dividing by the total count), however the confidence will be different (the itemset below changes)
> 2. #incomplete Maybe add into the properties the math for the number of possible subsets and the number of possible rules.

## Creating and selecting rules:
When creating this rules we would like to find **reliable rules** and make relations not only on correlation. In order to create reliable rules there are two important considerations, **support and confidence**. Based on this, when we look for rules we want that: 
- The support >= minsup threshold
- confidences >= minconf threshold

Lets say we want to make a rule with items of some itemset X. We can perform binary partitions (cut the itemset into two pieces to create a rule X->Y). 
Based on property 1 we can now say that any rule with those items will have the same amount of support. Then it is only a matter of choosing the relations with the best confidence (>= minconf). 
This means that when selecting rules we can, before even partitioning, just compute the support for the initial itemsets and choose those with a high enough value (>= minsup). 

But first of all, how many possible sets are there to create rules from? The answer is straight forward as all subsets can be obtained by the [[1762459118-powerset|Power set]]. 
And now, how many rules can there be created:
$$
R = \sum^{d-1}_{k=1}\left[ \binom{d}{k}\times \sum^{d-k}_{j=1}\binom{d-k}{j} \right]
$$
- This grows... #duda exponentially?

What this tells us is that there is a shit ton of possibilities, so going and bruteforcing it may just not be the best of ideas. What other options are there though?
1. **Reduce number of candidates:** Reduce some items with some prunning.
   In order to do so we first need to realize that any subset of an itemset has at least the same support or more as its parent. $$ \forall X,V: (X\subseteq  Y) \Rightarrow s(X) \geq s(Y)$$ Same thing works in the other direction. If a subset has some support, then any superset that contains it needs to have that support or less. 
   This can be used to prune the number of candidates by analising sets from those that only have one item onwards. 
   > If item A has a support of 0.4 then no set containing A can have a greater support than 0.4. 
   > If some itemset already has a support < minsup then we can disregard any set that uses that item. 
2. **reduce the number of transactions:** Reduce the size 
3. **Reduce the number of comparisons**

***
### Up
### Down
***