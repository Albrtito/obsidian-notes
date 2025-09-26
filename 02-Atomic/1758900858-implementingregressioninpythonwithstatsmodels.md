---
aliases:
- implementing regression in python with statsmodels
tags:
- review
- ms
References:
cssclasses:
---
# implementing regression in python with statsmodels
> [!NOTE] Intro: 
> How can we use regression models in python with the library statsmodels.

We use statsmodels instead of sklearn because it gives out more info.

1. Installing statsmodels

2. Model creation: 

```python
import statsmodels.api as sm
# add a first row of ones for theta zero. Doing it to Xnorm, the X matrix
Xconst = sm-add_constant(Xnorm)
# OLS -> Ordinary least squares
model = sm.OLS(y,Xconst).fit()
```

3. Getting the model info:
```python
summary = model.summary()
print(summary)
```

The structure of this summary is the following

***
### Up
### Down
***
