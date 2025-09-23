---
aliases:
  - weight adjustment in neural networks
tags:
  - review
  - ms
References:
cssclasses:
---
# weight adjustment in neural networks
> [!NOTE] Intro: 
> As in any other machine learning approach we’ll need to compute the loss (error) that the model has and minimize it, then obtain the necesary changes that need to be performed to the weights to reduce the error. 

For the ms course we’ll use the [[1758649312-sumofsquarederrorfunction|SSE]] error. 

## weight impact: 
In order to know how each of the weights impact the error that we are making we are asking: "What is the change in y wrt some weight?", that is the same as saying derivative (change in… → Derivative!). 

This derivatives are all gathered under the **gradient**.  $\nabla J(w)$
$$
\nabla J(\boldsymbol{w})=\left[\begin{array}{c}
\frac{\partial J(\boldsymbol{w})}{\partial w_1^{(1)}} \\
\frac{\partial J(\boldsymbol{w})}{\partial w_1^{(1)}} \\
\ldots \\
\frac{\partial J(\boldsymbol{w})}{\partial w_{13}^{(2)}}
\end{array}\right]
$$
- Each term is asking, how much does J(w) change for some variable in w
  > the first term would be: How much does J(w) change based on $w_1^1$
  
Knowing the gradient we can apply **gradient descend** and correct each weight. 
$$
w^{t+1} = w^t - n * \nabla J(w^t)
$$
where:
- n → Learning rate
***
### Up
### Down
***
