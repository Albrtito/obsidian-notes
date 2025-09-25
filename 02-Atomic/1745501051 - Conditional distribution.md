---
aliases:
  - Conditional distribution
tags:
  - ai
References: 
cssclasses:
---
# Conditional distribution

> [!NOTE] Intro: 
> The conditional distribution of two [[1745500044 - Random variables|Random variables]] is given as a vector of vectors with the value of one of the variables and the conditional probabilty of the other once that value has been observed, see [[1745501224 - Theorem - Conditional probability|Conditional probability]]

Going further into the idea of a vector of vectors..
As we can see in [[1745500044 - Random variables|Random variables]], the random variable is represented as a variable with a set of possible values it can take and the set of probabilities attached to those values.
A conditional distribution is a set of those set of probabilities attachaed to the values of some variable

>f.e: For Y domain going from 0 to 99 we can obtain the probabilities of X 
>$$
\begin{aligned}
P(X \mid Y) & =\langle P(X \mid Y=0), \ldots, P(X \mid Y=99)\rangle \\
& =\left\langle\left\langle\frac{1}{100}, \ldots, \frac{1}{100}\right\rangle, \ldots,\left\langle\frac{1}{100}, \ldots, \frac{1}{100}\right\rangle\right\rangle
\end{aligned}
$$
We can see that the first set of values are the probabilities of X when Y = 0 and the last one the set of probabilities of X when Y = 99.


***