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

![[1758900858-implementingregressioninpythonwithstatsmodelsj-1.png|center]]

The model coefficients here is one of the most important part. 
- The first column “**coef**” will giveo uot the solutions for the model, the actual thetas
- **std err** → Estandar error of the result
- **Last three columns** → The distribution of the errors. Probability of it being between the given percentails (two last values)


***
### Up
### Down
***
