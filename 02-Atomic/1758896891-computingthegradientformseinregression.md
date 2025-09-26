---
aliases:
- computing the gradient for MSE in regression
tags:
- review
- ms
References:
cssclasses:
---
# computing the gradient for MSE in regression
> [!NOTE] Intro: 
> 

The computations for the derivatives of thea gradient given that the cost function is MSE would be given based on $E(\theta)$
$$
E() = \frac{1}{m}\sum^m_{i=1}(\hat y^{(i)}-y^{(i)})^2
$$
where the prediction is based on the regression model so:
$$
\begin{align}
\hat y = \theta^Tx^{(i)}\\
E(\theta) = \frac{1}{m}\sum^m_{i=1}(\theta^Tx^{(i)}-y^{(i)})^2
\end{align}
$$
$$
\frac{\partial E(\theta)}{\partial \theta_k} = 
$$
***
### Up
### Down
***
