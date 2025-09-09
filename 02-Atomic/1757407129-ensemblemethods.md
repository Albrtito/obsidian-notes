---
aliases:
- ensemble methods
tags:
- review
- ms
References:
cssclasses:
---
# ensemble methods
> [!NOTE] Intro: 
> Use several types of classifiers, all mostly good at what they do, aggregate all their predictions to get a new one.
> - How do we get this new prediction? What about ties?

## Why does this work?
The error of an ensemble is given by:
$$
\epsilon_{ensemble} = \sum^N_{i = ceil(N/2)} \binom{N}{i}(1-\epsilon_i)^{5-i} 
$$
This means that **as long as the agents inside the ensemble ARE INDEPENDENT, and their errors therefore too,** the error of the ensemble would be smaller than the individual errors. 
The logic here is that if the **individual error rate is less than 50%** then it would just be outvoted as there are allways more agents making the correct choice.
For **errors greater than 50%** the ensemble just makes it worse. It’ll also get worse the more agents there are

If we are going to apply this then we would also want for our base classifiers to **not do worse than a classifier doing random guessing**

Based on how indepent are the agents between them:
- If they are all trained on the same data partition they are not independent. We would say this type of agents are **perfectly correlated**
- If the agents are **partially correlated** then the ensemble gives some improvement and the error rate drops
- If the agents are completely **uncorrelated, completely inddependent** then **theoretically the ensemble error rate would go to 0**

***
### Up
### Down
- [[1757408342-ensemblebasemodels|ensemble base models]]
***
