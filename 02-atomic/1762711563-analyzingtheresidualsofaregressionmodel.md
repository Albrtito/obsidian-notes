---
aliases:
- analyzing the residuals of a regression model
tags:
- ms
---
# analyzing the residuals of a regression model
> [!info] Intro: 
> When looking into the residuals of a regression model a distribution of them will appear as well as some pattern (when plotting residuals agains the variables). 
> If the model is fitting nicely then the residuals should **have a normal distributtion and no pattern**. Both properties at the same time. If any of the two properties is not checked then it may be that the model is not really good.

Important to notice that this analysis is checking that all the [[1758732030-linearregression#Properties of linear regression|linear regression properties]] are met.

For this properties we have the following tests:
1. Homoskedasticity can be checked using the **Breusch-Pagan test**
2. Using the [[1762717333-durbinwatsonstatistic|durbin-watson statistic]] (for autocorrelation)
   If there is a correlation between two variables then we'll remove one of them form the model. 
3. ...
4. Use the **Jarque-Bera test** (for normality of the distribution).
   The residuals can be shifted to obtain a more normal distribution. #duda The residuals or the data?

***
### Up
- [[1758732030-linearregression|regression]]
### Down
***