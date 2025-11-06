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
> - **confidence|c->** Measures how often items in Y appear in transaction that contain X. 
>   $$
> c = \frac{\sigma(X,Y)}{\sigma(X)}
$$

When creating this rules we would like to find **reliable rules** and make relations not only on correlation. In order to create reliable rules there are two important considerations, **support and confidence**
***
### Up
### Down
***