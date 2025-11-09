---
aliases:
  - linear regression
  - OLS
tags:
  - review
  - ms
References:
cssclasses:
---
# linear regression
> [!NOTE] Intro: 
> Linear regression is a method for fitting a linear function through some data points (observations). For this we’ll use some cost function and try to minimize it.

>[!attention] Remarks:
> - During the ms course we’ll almost always use the [[1758649312-sumofsquarederrorfunction|SSE]] function as cost function. Because we are doing so we'll be using the **OLS(Ordinary Least Squares)** method. 

> [!example] Dictionary:
> - **prediction | hypothesis** → The prediction of a model, also called hypothesis is given based on some input x and follows a function usually denoted by $h_{\Theta}(x)$ or $f_{\Theta}(x)$. Then:
>   $$ \hat y = h_{\Theta}(x) | f_{\Theta}(x)$$
> - **Coefficients** → In the hypothesis function we’ll use some coefficients, denoted by $\hat \Theta_i$ for each $x_i$. 
>   The cap is there as we are also **estimating coefficients**. Altough most times the hat is not shown
> 

## modeling linear regression
A regression model would generalize to:
$$\hat y = \theta_0 + \theta_1*x_1 + ... + \theta_D*x_D$$
where:
- Each x is a feature
- Each theta is a coefficient
- $\theta_0$ Is the initial starting point (ordenada en el origen)

This can eb rewriteen as: $\hat y = \theta^TX$ where now we have $\theta$ as a vector (transposed and X as a matrix):
$$Vector \space \theta=\left[\begin{array}{c}\theta_0 \\ \theta_1 \\ \cdots \\ \theta_D\end{array}\right] \quad Matrix\space x=\left[\begin{array}{ccc}1 & 1 & \cdots \\ x_1^{(1)} & x_1^{(2)} & \cdots \\ \cdots & \cdots & \cdots \\ x_D^{(1)} & x_D^{(2)} & \cdots\end{array}\right] $$
where:
- In the matrix each row represents a variable and each column an observation. The parenthesis number with x means the observation number. 

Using the **MSE** error function we could now generalize to:
$$
J(w) = \frac{1}{n} \sum^N_{n=1}((\theta_nx_n^{(i)}) - y_n^{(i)})^2
$$
where:
- **i** → The observation

And then try to minimize that cost function, **the whole objective of this all**, to **obtain the coefficients for the min**:
$$
min_{\theta_0,...\theta_D} \frac{1}{n}\sum^n_{i=1}(h_\theta(x)-y^{(i)})^2
$$
**where:**
- **The residual(e)->** The difference between the predicted and real value. In this case because we are squareing it the order does not matter but usually the residual is given by: 
  $$ e = y - \hat{y}$$
  A better analysis of the residuals can be done.
 - [[1762711563-analyzingtheresidualsofaregressionmodel|analyzing the residuals of a regression model]]

> If we this whole structure in a 2d space with only one variable and the prediction in the other axis we’ll have to minimize the cost given by: 
> $$Cost = \frac{1}{n}\sum^n_1(\theta_1*x_1^{(i)}-y^{(i)})^2$$
> And if we try some values for the theta we’ll see that the costs based on values (secondary cost plot) will be something parabolic. So a best value and then some worsening to the sides. 
> 
> When working with data that needs an “ordenada en el origen”, justa add the $\theta_0$.


> [!attention] Remark:
> So **the objective here is to find the values for thetas so that we get the min value for the cost function.**
> But we cannot just “try some values randomply”. So we’ll use gradient descent

## Properties of linear regression:
>[!important] Properties:
> 1.  **Independence of variables:** The explanatory variables are linearly independent. If not we'll rul into colinearity problems.  
> 2.  **Residuals:** The residuals of OLS must comply with the following properties:
> 	2.1  **Zero mean property** $$E(e) =0$$
> 	2.2  **Variance is constant and finite (Homoskedasticity)** $$var(e) = \sigma^2 < \infty$$
> 	2.3 **Linearly independent of one another** $$cov(e_{i},e_{j}) = 0$$
> 	2.4 **No relationship between residuals and each of the explanatory variables** $$cov(e,x_{i}) = 0$$
> 	2.5 **The residuals are normally distributted** $$e \sim N(0,\sigma^2)$$

How can we check that this properties comply?
See more about these tests in [[1762711563-analyzingtheresidualsofaregressionmodel|analyzing the residuals of a regression model]]
***
### Up
### Down
- [[1758734414-gradientdescent|gradient descent]]
- [[1756374226-evaluationinregression|evaluation in regression]]
- [[1758900858-implementingregressioninpythonwithstatsmodels|implementing regression in python with statsmodels]]
***
