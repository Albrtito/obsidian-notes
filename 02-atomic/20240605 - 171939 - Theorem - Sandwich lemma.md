---
aliases:
  - Theorem - Sandwich lemma
  - Sandwich lemma
  - Pinching lemma
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-06-21
sr-interval: 10
sr-ease: 250
---
# Sandwich lemma: 


The sandwich lemma is a method used for the computation of limits. 

The idea is that if there are three functions g(x), g(x) and h(x) such as g(x) is smaller than h(x) but greater than f(x), something like this: 

![[Pasted image 20240605173722.png]]

Then if at some point f(x) and h(x) have the same value (x = 2 in the image below), f(x) also has that same value. 

Why? Because there is no room to go, we are saying that f is always on top and h always on the bottom, g(x) has nowhere to go but the same value that f and h are taking if they are equal. 

Why is this useful? Well, it tends to be less useful (in my humilde opinion) than what teachers and mathematicians say it is. But, and this is the important part: 
If **you need to find the value of g(x) at some point (lets say $x_0$), then if you can find two functions f(x) and h(x) that follow all what I have already explained, then you know that:**
$$\boxed{g(x_0) = f(x_0) = h(x_0)}$$

I wish u all the luck in the world in the journey to find f(x) and h(x)

## Formal definition: 

> [!NOTE] Theorem: 
> **IF** $g(x) \leq f(x) \leq h(x)$ for every $0< |x-x_0| < \sigma$  and:
> $$
> lim_{x\rightarrow x_0}g(x) = lim_{x\rightarrow x_0} h(x)= l
> $$
> **THEN:**
> $$
> lim_{x\rightarrow x_0}f(x)= l
> $$

**Remarks:**
+ Using this lemma is not straightforward. Mostly try to find an inequality for the limit. It is better to try anything else before going with this. 

## Examples: 

1. 
