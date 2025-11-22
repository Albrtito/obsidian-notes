---
aliases:
  - weight adjustment in neural networks
tags:
  - review
  - ml
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
- t → Represents old and new weights, not layer


> [!bug] computation of partial deriv
> The gradient uses all of this partial derivatives, but how can we actually compute those?
> - The solution is backpropagation

### backpropagation:
In order to obtain the partial derivatives we can divide the orignal expression into three parts for the weight on the **last level(output)** going back on how each weight is being used.

Applying the chain rule:
$$
\begin{align}
\frac{\partial J(w)}{\partial w^{(l)}} =
\frac{\partial J(w)}{\partial a^{(l)}} * 
\frac{\partial a^{(l)}}{\partial z^{(l)}} * 
\frac{\partial z^{(l)}}{\partial w^{(l)}} = \\\\
= ((a)^{(l)} - y) * \phi ' (z^{(l)}) * a^{l-1}
\end{align}
$$
where: 
- The first part is the variance based on the lattest node
- The second part is the variance of that node based on the input to that node
- The last one is the variance of that input based on the weight that alters it.
However this goes into larger and larger expressions once the level goes deeper and deeper into the neural network. 
**See the ms course sliedes or more info about backpropagation for a deeper view into this**
***
### Up
- [[1758644145-neuralnetworks|neural networks]]
### Down
***
