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
> What we do when creating a neural network is **learning the weights**

![[1758644145-neuralnetworksj.png|center]]


> [!example] Dictionary:
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

## math:
Now how do we define this all mathematically, we know how to define a neuron: 
$$
\hat y = \phi(\sum_{i=0}^m w_ix_i)
$$
Now the prediction is not the output but the value of some next layer node. And we are not taking the sum based on the inputs anymore but the values for the previous layers outputs.
$$
a^{layer}_{pos} = \phi(\sum_{i=0}^m w^{layer}_{\text{pos}, i}x_i)
$$


### Up
- [[1758647070-neuron|neuron]]
### Down
***
