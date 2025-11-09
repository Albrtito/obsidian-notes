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


## analysis of results
```python
summary = model.summary()
print(summary)
```

The structure of this summary is the following

![[1758900858-implementingregressioninpythonwithstatsmodelsj-1.png|center]]

### Model coefficients:
The model coefficients here is one of the most important part. 
- The first column “**coef**” will giveo uot the solutions for the model, the actual thetas
- **std err** → Estandar error of the result
- **Last three columns** → The distribution of the errors. Probability of it being between the given percentails (two last values)
- **P value** →  Is the coefficient of each value important enough? We care about this because we may get a value diff than 0 but that takes no importance really in the model, so it could be deleted. The P value is the probability of this happening. 
### Model fit: 
- The main value here is the [[1762709209-goodnessoffit|R squared]] to see how good the model is (closer to 1 is good)
- Then there is the [[1762709866-fstatistic|f-statistic]]
- Akaike Information Criterion ([[1762710178-akaikeinformationcriterion|AIC]]) and Bayesian Information Criterion ([[1762710368-bayesianinformationcriterion|BIC]]) are both used for model selection based on the fit and number of used variables. 

### Residuals and residual analysis:
Outputs for tests such as [[1762717333-durbinwatsonstatistic|durbin-watson statistic]] or [[1762717786-jarqueberatest|jarque-bera test]] are shown here. 
***
### Up
- [[1758732030-linearregression|regression]]
### Down
+ [[1758902314-pvalue|p value]]
***
