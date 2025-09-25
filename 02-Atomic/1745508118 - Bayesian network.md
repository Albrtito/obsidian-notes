---
aliases:
  - Bayesian network
tags:
  - ai
References: 
cssclasses:
---
# Bayesian network (BN)
> [!NOTE] Intro: 
> A Bayesian network is a probabilistic method based on [[1745507844 - Conditional independence|Conditional independence]] that is used to obtain the probability of some state given the probability of previous states.
> It represents “graphically” the conditional independence idea, where a **previous state** will be used as the condition for the next state probability. 

+ THey are really compact wich is great as it has **lower parameters and easier computation** therefore a more efficient way of performing inference, in the form of [[1745510100 - Bayesian inference|Bayesian inference]]
The formal definition of the probability of one particular case in the bayesian tree can be defined by the joint probability distribution but also by the product of local distributions. 
$$
\begin{aligned}
P\left(X_1, \ldots, X_n\right) & =\prod_{i=1}^n P\left(X_i \mid X_1, \ldots, X_{i-1}\right) \\
& =\prod_{i=1}^n P\left(X_i \mid \operatorname{Parents}\left(X_i\right)\right)
\end{aligned}
$$
## Eficiency:
+ **Max number of parameters:** Given a maximumn of k parents a single variable can have $2^k$ parameters. The complete BN can have a maximum number of parameters of:
$$
  O(n\cdot 2^n)
$$

***