---
tags:
  - discrete
DateCreated: 2024-02-05
"References:":
  - "[[Basic Set Operations]]"
aliases:
  - Elementary Combinatorics
sr-due: 2024-05-27
sr-interval: 7
sr-ease: 256
---
# Elementary combinatorics
This is an introduction to combinatoric concepts. Combinatorics are also called counting methods. They are the main object of study of discrete mathematics. This methods are used to count possibilities. 

## Basic definitions: 

We’ll turn possibilities into sets, a set A is said to contain all the possibilities of some event happening. Then we can **count how many possibilities there are** inside that set, this count is called **cardinality**

> [!NOTE] Cardinality
> Given a set S, its cardinality |S| represents with integer value the number n of different elements inside the set S. Namely, the size of the set

**Remarks:**
+ Two sets have the same cardinality <=> There exist a bijective function between them 
	+ This means we can find a function that turns any value of A into an unique value of B and vice versa
+ A **countable** set is one with finite cardinality or cardinality = $\mathbb{N}$
	+ Zero element set: $\emptyset$ 
	+ Finite number of elements

### Sum and product principles:
Because we are defining the collection of possibilities as sets it is useful to us to define some operations that can be made between these sets and the number of possibilities each one contains. The two main operations used are **addition and multiplication** from which the **product principle** and **the sum principle** are obtained. 

> [!NOTE] Addition of cardinalities
> For two disjoint and finite sets, we can add their cardinality and obtain their union's cardinality
> **Conditions:**
> 	A and B disjoint
> 	A and B finite
> **Result:**
> 	|A U B| = |A| + |B|
> If the sets are **not disjoint**
> $|A U B| = |A| + |B| - |A\cap B|$
> 

+ This applies with  as disjoint possibilities can be summed. 

When this is generalised we get: 
![[20240515 - 010006 - Principle - Sum principle|Sum principle]]


Multiplication of cardinalities is given by the product principle: 
![[20240515 - 010522 - Principle - Product principle|Product principle]]

## Counting methods:
![[20240515 - 010716 - Counting methods|Counting methods]]


## The power set: 
![[1762459118-powerset|Power set]]


## Inclusion exclusion principle
For the discrete course we'll se cases with 3 sets, a maximum of 4 in the worst case.

![[20240515 - 013650 - Principle - Inclusion-exclusion principle|Inclusion-exclusion principle]]

## Pigeonhole principle

![[20240515 - 014153 - Principle - Pigeonhole principle|Pigeonhole principle]]

**Remark:** During the discrete math course it is useful for problems
 