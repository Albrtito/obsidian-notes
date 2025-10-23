---
aliases:
  - Principle of induction
Date: 2024-03-12
tags:
  - calc
"References:": 
sr-due: 2024-09-19
sr-interval: 122
sr-ease: 270
---
# Principle of induction

> [!NOTE] Definition
> The principle of induction is a method used with [[Natural numbers (set N)]] in order to **prove** some property defined earlier on this set.

**Remarks:**
+ It needs to be applied over a domain N (or a domain isomorphic to N)
+ If it is possible to prove through this method, then the proposition is true. If the method shows that the proposition suffers of any contradiction then we can say that the proposition is false.

## Example: 
For proving the property P which depends on a natural number n. The principle of induction establishes the following: 
**IF**
1. we **check that n = 1 verifies** the property P
2. we **assume** that n = k  $\in \mathbb{N}$ verifies the property P (hypothesis)
3.  Prove that n = k+1 $\in \mathbb{N}$ verifies the property P
**THEN:**
All natural numbers satisfy the property P

---
**Remarks:**
+ The difficult part is step 3. 
+ We need to obtain step 3 using step 2. That's the way to do it
+ If 1 is not on the specified domain. Then get the smallest possible natural number
### Examples: 
This property can be used to prove theorems such as [Gauss sum theorem](Gauss%20sum%20theorem.md)