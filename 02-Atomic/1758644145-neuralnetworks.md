---
aliases:
- neural networks
tags:
- review
- ms
References:
cssclasses:
---
# neural networks
> [!NOTE] Intro: 
> Neural networks are based on the way actual biological neurons work. Whenever a neuron recieves a certain signal, if that signal is bigger than some threshold then it transmits the idea to the next neuron.

If we take this idea into math we could say: 
$$
\sum_i w_i x_i = z
$$
- If z ≥ T then accept
- ElseIf z ≤ T decline
   (this will later be defined as the “phi function” → $\phi ()$)

This way we are creating this mechanism where the “neuron” decides based on some coefficients w over some decision variables x. 
- The coefficients represent **weight of each variable** 
- In order to normalize the threshold we’ll add a **bias ($w_0$)** that will leave the threshold function with a jump at 0 instead of some random threshold.
$$
 w_0 +\sum_i w_i x_i = z  
$$
## phi
Finally we represent the function to use when going from acceptance to rejection with the leter **phi**: $\phi$. Thus function will take the weights and variables as input and output the final prediction. 
$$
\hat y = \phi(w_0 + \sum_i w_ix_i)
$$
And because we w


***
### Up
### Down
***
