---
aliases:
- jarque-bera test
tags:
- ml
---
# jarque-bera test
> [!info] Intro: 
> Used to test that a distribution is normally distributed or not. 
> Uses the skewness and kurtosis of a distribution. The normal distribution is not skewed (Skewness = 0) and has a centain level of tailedness (Kurtosis = 3). This creates a excess kurtosis of kurtosis-3 = 0.

$$
W = n \cdot \left[ \frac{S^2}{6} + \frac{(K-3)^2}{24} \right]
$$
**where:**
 - The up part of both fractions represents the Skewness (S) and excess kurtosis (K-3)

***
### Up
- [[1762711563-analyzingtheresidualsofaregressionmodel|analyzing the residuals of a regression model]]
### Down
***