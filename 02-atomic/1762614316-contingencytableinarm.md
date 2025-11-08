---
aliases:
- contingency table in ARM
tags:
- ms
---
# contingency table in ARM
> [!info] Intro: 
> The contingency table of a given rule X->Y lets us analyze how interesting the rule is.

The table takes the following form:

|               | X                   | $\overline X$                   |                         |
| ------------- | ------------------- | ------------------------------- | ----------------------- |
| Y             | X and Y             | $\overline X$ and Y             | Transactions with Y     |
| $\overline Y$ | X and $\overline Y$ | $\overline X$ and $\overline Y$ | Transactions with not Y |
|               | Transactions with X | Transactions with not X         | Sum of all transactions |
This table can show that confidence can be misleading, lets see the following example:

|               | X   | $\overline X$ |     |
| ------------- | --- | ------------- | --- |
| Y             | 15  | 5             | 20  |
| $\overline Y$ | 75  | 5             | 80  |
|               | 90  | 10            | 100 |
> In this example the confidence of X->Y is 0.75, however if we look into this from the probabilistic perspective:
> The probability of just X here $P(X) = 0.9$ while the probability of X given Y is smaller: $P(X|Y) = 0.75$. Then this means that there is sure a high probability of X if Y, **but that probability is still smaller than the probability of just X**. 
> This shows how the rule is misleading. It can be even further shown if we look at the probability of X if $\overline Y$. $P(x,\overline Y)=0.93$. This is even higher. 

***
### Up
### Down
***