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
> A neural network is a bunch of [[1758647070-neuron|neurons]] together. Of course one single neuron is already a neural network but once we add more we’ll call it a **multilayer neural network**.
> 
> By introducing additional layers in between we are creating **hidden steps** to the user. A **blackbox method**
> 
> What we do when creating a neural network is **learning the weights** for this we’ll use some loss function.  

![[1758644145-neuralnetworksj.png|center]]


> [!example] Dictionary:
> - Usually the leter **l** is used for **level**
> - Notation for weights:
>  $$
> 	w^{(\#layer)}_{\text{To From}}
>   $$
>> $w^{(1)}_{34}$ → A weight on layer 1 comming from input 4 on previous layer and going to input 3 in this layer.
>
> - Notation for activation vectors:
>   $$
>   a^{(\#layer)}_{position}
>   $$
>   >$a^{(1)}_{2}$: Activation vector 2 for layer 1

## model definition:
Now how do we define this all mathematically, we know how to define a neuron: 
$$
\hat y = \phi(\sum_{i=0}^m w_ix_i)
$$
Scaling this into several neurons, creating an activation vector: 
> Some numbers given as example. This would give the first activation vector with three neurons (three outputs **a**) and five input values with five weights each neuron.

$$\left[\begin{array}{l}
x_0 \\
x_1 \\
x_2 \\
x_3 \\
x_4
\end{array}\right]\left[\begin{array}{l}
a_1^{(1)} \\
a_2^{(1)} \\
a_3^{(1)}
\end{array}\right]=\phi\left(\left[\begin{array}{ccc}
w_{10}^{(1)} & \cdots & w_{14}^{(1)} \\
\vdots & \ddots & \vdots \\
w_{30}^{(1)} & \cdots & w_{34}^{(1)}
\end{array}\right] *\left[\begin{array}{c}
x_0 \\
x_1 \\
x_2 \\
x_3 \\
x_1
\end{array}\right]\right)
$$

Now the prediction is not the output but the value of some next layer node. And we are not taking the sum based on the inputs anymore but the values for the previous layers outputs.
Then modifying the first equation by substution of x for a we get:

> Again, not genraliset but some example. This would be the value for the second activation vector if there was only one activation neuron in that vector. For more neurons there would be a second line of weights.
$$
\left[a_1^{(2)}\right]=\phi\left(\left[\begin{array}{lll}
w_{11}^{(2)} & w_{12}^{(2)} & w_{13}^{(2)}
\end{array}\right] *\left[\begin{array}{c}
a_1^{(1)} \\
a_2^{(1)} \\
a_2^{(1)}
\end{array}\right]\right)
$$
## hyperparams:
The hyperparameters of a neural network are **not the weights, as those are just parameters**. When talking about hyperparams on networks we have: 
- Learning rates
- Number of hidden layers
- Number of neurons in each layer
- Activation function 
- …

### Up
- [[1758647070-neuron|neuron]]
### Down
- [[1758649000-weightadjustmentinneuralnetworks|weight adjustment in neural networks]]
- [[1758892749-overfittinginneuralnetworks|overfitting in neural networks]]
- [[1758651868-hyperparameter|hyperparameter]] 
***
