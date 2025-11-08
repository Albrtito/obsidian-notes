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
> The stepsize will be important for evitar going into local min and tunning the way the descend is done. 


> [!example] Dictionary 
>+ Uses the **gradient** $\nabla E(\theta)$ where $E(\theta)$ will be the cost function. 
>	+ **remember:** During the ms course the cost funciton will be the [[1758737329-meansquarederrorfunction|MSE]]
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

Once we know a gradient for some coefficients we will know whether the slope is positive or negative at that point and how steep it is. Based on it we can know that: 
- If we have a positive slope (**positive gradient**) we have to **decrease the coefficients**
- If we have a negative slope (**negative gradient**) we need to **increase the coefficients**

This update of the coefficients is described in the following way:
$$
\theta^{t+1} = \theta^t - \eta \times \nabla_\theta E(\theta)
$$

where:
- $\eta$ → Applied learning rate

We’ll stop to perform gradient descend when whe have **convergence**, this means one of the following comply: 

- $\theta’ \simeq \theta$
- $E(\theta’) \simeq E(\theta)$

Basically until the coefficients or the gradient just does not change anymore. 

## adjusting hyper-parameters: 
The initial value for thetas as well as the learning rate and the number of iterations can make the model behave in different ways. These are the hyperparamets

The learning rate must be tunned (is a hyperparameter).
- if **really small** → May find a local minimun instead of a minimum 
- if **small** → It may take a lot to get convergence
- **if to large** → Possible divergence

A good solution would be to decrease the stepsize over size, once we get closer we can fine tune. 

Even with an ok learning rate we may go into a local minimum, to try not to do so we can start the algorithm with different values for theta and then compare the final points we have reached.

There is also another hyperparameter based on what is introduced in the next section. The batch size for mini-batched approach. 
## batch vs stochastic
while batch gradient descend uses all observations and sums them the stochastic gradient descend uses one random observation. See that when using one random observation we can drop the sum and the division by m as m is 1. 

This means: 
- Stochastic is really faster as it only uses one observation. 
- Stochastic is also noisier. There is no averaging. 
- Usually the stochastic is more used

We can take a mix of both ideas using **mini-batch gradient descend**. Just taking some small part of the data. 
***
### Up
- [[1758732030-regression|regression]]
### Down
- [[1758737329-meansquarederrorfunction|MSE]]
***
