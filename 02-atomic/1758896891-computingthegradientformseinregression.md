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
> For a regression model with the mean squared error function to compute loss we compute a gradient. The computation follows this notes contents.

The computations for the derivatives of thea gradient given that the cost function is MSE would be given based on $E(\theta)$
$$
E() = \frac{1}{m}\sum^m_{i=1}(\hat y^{(i)}-y^{(i)})^2
$$
where the prediction is based on the regression model so:
$$
\begin{align}
\hat y = \theta^Tx^{(i)}\\
E(\theta) = \frac{1}{m}\sum^m_{i=1}(\theta^Tx^{(i)}-y^{(i)})^2\\
E(\theta) = \frac{1}{m}\sum^m_{i=1}(\sum^n_{j=1}\theta_jx_j^{(i)}-y^{(i)})^2\\
\end{align}
$$
where: 
- The vector mul can be turned into a sum as it is the vectors have only one column.

Then based ont this function E we can obtain the derivative for a single theta component by:
$$
\frac{\partial E(\theta)}{\partial \theta_k} = \frac{2}{m}\sum^m_{i=1}x_k^{(i)}((\sum^n_{j=1}\theta_jx_j^{(i)})-y^{(i)})
$$
where:
- The term is squared so the two comes to the beginning of it all 
- Derivative of the inside is only the term for this theta so multiplied by x we get x as the derivative.
- Due to chain rule everything else is multiplied. 

***
### Up
- [[1758734414-gradientdescent|gradient descent]]
### Down
***
