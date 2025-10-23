---
aliases:
  - evaluation in regression
tags:
  - review
  - ms
References:
cssclasses:
---
# evaluation in regression
> [!NOTE] Intro: 
> How do we evaluate regression models, these are the ones fitting some function for **continuous data.**

We’ll have three different measurements: 

1. **Mean squared error:** (MSE)

$$
\text{Cost} = \frac{1}{n} \sum ^n _ {i=1} (\hat y_i - y_i) ^2 
$$
- Small errors get more important.

2. **Mean absolute error error:** (MAE)

$$
\text{Cost} = \frac{1}{n} \sum ^n _ {i=1} |\hat y_i - y_i| 
$$
- Just dont make any error

3. **Root mean squared error** (RMSE)

$$
\text{Cost} = \frac{1}{n} \sum ^n _ {i=1} \sqrt{(\hat y_i - y_i)^2}
$$



***
### Up
### Down
***
