---
aliases:
  - Conditional probability
  - Theorem - Conditional probability
tags:
  - ai
  - stat
References:
cssclasses:
---
# Theorem - Conditional probability

> [!NOTE] Theorem: 
> The conditional probabilty of a [[1745500044 - Random variables|Random variables]] can be interpreted as the **updated probabilty of the variable** once another variable has been observed:

$$
P(A|B) = \frac{P(A,B)}{P(B)} : P(B) \not = 0
$$
+ With the given formula we are asking, what is the probability of A knowing the probability of B?
+ We can ask ourselves what is the probability of A for any value that Y can take, then we’ll obtain the [[1745501051 - Conditional distribution|Conditional distribution]] of X knowing Y. 
+ A redistribution of this formula creates the [[1745503400 - Probability product rule|Probability product rule]]
+ And by using this rule we get the [[1745503587 - Theorem - Bayes rule|Theorem - Bayes rule]]
+ It is also interesting to know whether the variables being used are [[1745504803 - Probabilistic variable independence|Probabilistic independence]] or not, if they are we can easily simplify the problem. See more ate 
***