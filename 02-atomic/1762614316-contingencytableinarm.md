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
> In this example the confidence of X->Y is 0.75, however 

***
### Up
### Down
***