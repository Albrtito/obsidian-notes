---
aliases:
- rule generation in ARM
tags:
- ml
---
# rule generation in ARM
> [!info] Intro: 
> When generating rules we'll focus on the **confidence of the generated rules** to choose them or not. 

>[!important] Properties:
> 1. **Anti-monotone property for items in the SAME ITEMSET:** Confidence does not have a generalised anti-monotone property, it does however have a it for rules generated from the same itemset.
>    $$c(ABC\to D)\geq c(AB\to CD) \geq c(A\to BCD)$$

Same as with the generation of frequent subsets we can generate a lattice with all the rules based on the anti-monotone property for each itemset. Because this rules, again, derive from each other. We can again just prune all child once we see that a parent has a confidence < minconf. 

However the algorithms creating this rule association tend to produce to many rules making many of then uninteresting or redundant.
To analyze the created rules we can use several measures: 
- [[1762614316-contingencytableinarm|contingency table in ARM]]
- [[1762617187-statisticalindependenceinarm|statistical independence in ARM]]

***
### Up
### Down
***