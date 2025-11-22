---
aliases:
- bias vs variance
tags:
- review
- ml
References:
cssclasses:
---
# bias vs variance
> [!NOTE] Intro: 
> **Bias:** Measures how far of in general a model predictions are from the correct value. (one model, one data, general error)
> **Variance:** The variability of predictions for a point if different training data were used. (difference between data, models, error?)

# Comparing both of them (matrix)

If we create a matrix, similar to the [[1756371053-confusionmatrix|confiusion matrix]], but with variance and bias, then we get: 

|           | Low Variance     | High variance   |
| --------- | ---------------- | --------------- |
| Low Bias  | WE WANT THIS     | **Overfitting** |
| High Bias | **Underfitting** | Real bad        |
- **Overfitting**: The result is really close to the actual result (on average) but is really different if different training data is used (high variance)
- **Underfitting:** The variance is really low because the model is the problem and it is allways doing similar predictions not regarding the training data. The bias is high as it is not close to the actual values.

![[1757409110-biasvsvariancej.png|center|400]]


***
### Up
- [Understanding the bias-variance tradeoff (web)](https://scott.fortmann-roe.com/docs/BiasVariance.html#fnref:4)


### Down
***
