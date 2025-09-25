---
aliases:
  - Theorem - Total probabilty theorem
tags:
  - ai
References: 
cssclasses:
---
# Theorem - Total probabilty theorem

> [!NOTE] Theorem: 
> Given some events $A_i$ that divide and contain the **whole S space and are disjoint(do not have an intersection)**. If we sum the probability of all the intersecctions $P(A,B) = P(A\land B)$ we’ll get the complete probability of B.

$$
P(B)=\sum_{i=1}^n P\left(B, A_i\right)=\sum_{i=1}^n P\left(B \mid A_i\right) P\left(A_i\right)
$$
+ We obtain that second formula by rearanging the [[1745501224 - Theorem - Conditional probability|Conditional probability]] theorem (using )
***