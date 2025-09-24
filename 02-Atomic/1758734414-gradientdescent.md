---
aliases:
- gradient descent
tags:
- review
- ms
References:
cssclasses:
---
# gradient descent
> [!NOTE] Intro: 
> The idea under gradient descent is to look for the values for some vector so that it minimizes a fuction. In order to do so it performs small steps towards the goal going downhill (if imagining some slope) with the slopes defined by the gradient (a vector of partial derivatives.)


![[1758734414-gradientdescentj.png]]

+ It works iteratively using an stepsize

> [!attention] Remarks:
> The stepsize will be important for 


> [!example] Dictionary 
>+ Uses the **gradient** $\nabla E(\theta)$ where $E(\theta)$ will be the cost function. 
>	+ **remember:** During the ms course the cost funciton will be the [[1758649312-sumofsquarederrorfunction|SSE]]
>
>The gradient is defined by the partial derivatives of the cost function over the thetas.
>$$
>\nabla E(\boldsymbol{\theta}) = \left[
>\begin{array}{c}
>\frac{\partial E(\boldsymbol{\theta})}{\partial \theta_1} \\
>\frac{\partial E(\boldsymbol{\theta})}{\partial \theta_2} \\
>\vdots \\
>\frac{\partial E(\boldsymbol{\theta})}{\partial \theta_{n}}
>\end{array}
>\right]
>$$

***
### Up
- [[1758732030-regression|regression]]
### Down
***
