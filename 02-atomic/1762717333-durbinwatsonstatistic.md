---
aliases:
- durbin-watson statistic
tags:
- ml
---
# durbin-watson statistic
> [!info] Intro: 
> Used to detect the presence of autocorrelation at lag 1
> - DB >> 2 -> Negative autocorrelation
> - DB = 2 -> No autocorrelation
> - DB << 2 -> Positive autocorrelation

$$
DB = \frac{\sum^T_{t=2}(e_{t}-e_{t-1} )^2}{\sum_{t=1}^Te_{t}^2}
$$
**where:**
 - The part up top is measuring the distances from one residual to another
***
### Up
- [[1762711563-analyzingtheresidualsofaregressionmodel|analyzing the residuals of a regression model]]
### Down
***