---
Date: 2024-03-18
tags:
  - discrete
"References:": 
sr-due: 2024-06-07
sr-interval: 21
sr-ease: 205
---
> [!NOTE]  Generalisation
> Based on the [Theorem 110 Solution of a homogeneous Fibonacci-type recurrence relation](Theorem%20110%20Solution%20of%20a%20homogeneous%20Fibonacci-type%20recurrence%20relation.md) we now know that or solving an order two recurrence relation we can transform it into a polynomial of degree 2. This concept can be generalised
> For any order homogeneous recurrence with constant coefficients, the relation can be transformed into a polynomial of degree k (order of the relation) starting from the first term that appears (the lowest n-i). This term will be transformed into x to the power of 0. From that point, following terms each get transform to the following power of x. 
> But what happens now with the **repeated roots**? Same thing it happened before but for each group of repeated roots we do the following. 
> + If the root $x_i$ is simple: $a_n ^î = K_ix_i^n$
> + If the root $x_i$ is double: $a_nî = (K_i + K'_{i}n)x^n_i$
> + If the root $x_i$ is repeated m times then: $a_nî = (K_i + K_i'n + K_i^{''}n^2+...+ K_i^mn^m)x_i^n$
> 
> **Conditions:**
> + We need to know the k initial conditions (to get the Ks at the end)
> 
> **Solution:**
> General solution that no one will use at first but surely summarises it all once u understand it. 
>$$
> a_n=\sum_{i=1}^r\left[\sum_{j=1}^{k_i} K_i^{(j)} n^{j-1}\right] x_i^n, \quad n \geq 1
>$$

**Remark:**
+ There's a really important property for this relations and the non-homogeneous ones. This property is the **superposition principle**.
   
  This principle states the following: **If $a_n , b_n$ are two solutions for a linear homogeneous recurrence relation then the linear combination $\alpha a_n + \beta b_n$ is also a solution of that recursion**
  #duda : Does this mean that (going back to the generalisation defined a moment ago) the equation we obtain for one single root is also valid and can be even specified with some initial conditions? 
  
+ Another property of recurrence relations is that the space of solutions has a vector space structure. This means that there is infinite possible solutions before we compute the constants K.Once some initial conditions are given , one single solution remains. 