---
aliases:
  - statistical independence
tags:
  - ms
  - stat
---
# statistical independence
> [!info] Intro:
> Statistical independence occurs when the occurrence of one event does not affect the probability of another event occurring. Two events A and B are independent if:
> P(A ∩ B) = P(A) × P(B)

This means the joint probability equals the product of individual probabilities.

Seen from a [[1745501224 - Theorem - Conditional probability|Conditional probability]] perspective. Two variables are statistically independent if **knowing one of them does not affect the probabilty of the other one**

> Independence is:
> • Flipping two fair coins - the outcome of one doesn't affect the other
> • Rolling dice multiple times
> • Drawing cards with replacement

If two variables are not independent then the correlation between them can be measured. 
They'll have a **possitive correlation** if: 
$$
P(X|Y) > P(X)
$$
And a **negative correlation if:**
$$
P(X|Y) < P(X)
$$
When the measurement is expressed as P(X|Y)/P(x) it's called **lift:**
$$
\text{Lift}=\frac{P(X|Y)}{P(X)}
$$
**where:**
 - The lift can be > 1 for positive correlation. 1 for no correlation (independence) and <1 for negative correlation. 
***
### Up
### Down
***