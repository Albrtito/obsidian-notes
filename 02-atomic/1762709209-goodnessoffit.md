---
aliases:
  - goodness-of-fit
  - R squared
tags:
  - ml
---
# goodness-of-fit
> [!info] Intro: 
> Measure of how well a regression model fits.
> A good R squared value depends of the application. For finatial applications it is usually as low as 0.3 or 0.4 while for other physical applications it is expected to see higher values 0.8 and around it. 

$$
R^2 = 1 - \frac{\sum_{i}(y_{i}-\hat{y_{i}})^2}{\sum_{i}(y_{i}-\hat{y})^2}
$$
**where:**
- The fraction represents the residual sum of squares divided by teh total sum of squares.
- If $R^2=1$ the model fits data perfectly
- If 0 < $R^2$ < 1. THe model fits data better than the mean
- If $R^2=0$ the model fits data as good as the mean
- If $R^2 < 0$ model fits data worse than the mean (really hard to happen but could happen)

>[!attention] Remarks:
> - R square will never get worse if more variables are added. This is why the regression models provide with another value called **adjusted R-squared**, adjusted for the numbr of variables

***
### Up
- [[1758732030-linearregression|regression]]
### Down
***