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

+ It works iteratively
+ Uses the **gradient** $\nabla E(\theta)$
$$
\nabla E(\boldsymbol{w})=\left[\begin{array}{c}
\frac{\partial E(\boldsymbol{w})}{\partial \theta_1}} \\
\frac{\partial E(\boldsymbol{w})}{\partial \theta_2} \\
\ldots \\
\frac{\partial E(\boldsymbol{w})}{\partial \theta_n}
\end{array}\right]
$$
***
### Up
### Down
***
