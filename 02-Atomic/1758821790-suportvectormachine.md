---
aliases:
  - suport vector machine
  - SVM
tags:
  - review
  - ms
References:
cssclasses:
---
# suport vector machine
> [!NOTE] Intro: 
> A support vector machine works on finding the threshold hyperplane that divides two classes (so **binary classification**) performing linear separation.
> 
> **Remember:** To get the best linear separation possible we are looking for the **maximized margin** on the threshold.

- Assume that the hyperplane exists
- Assume that the classes are **linearly separable**, this means that there is no misclassification between them

> [!example] Dictionary:
> - $||a||$ → The normalized vector a. Using the **Euclidean normalization** (for ms course and usually)
> - **margin** → Usint $\rho$ to reference it
> - **soft margin** → A soft margin is one that **allows misclassification**. 
> - **soft classifier** → A classifier that allows misclassification

To maximize the margin we need to look into where each of the suporting vectors is. We’ll follow then:

$$
\begin{align}
w^Tx_a + b - 1 = w*Tx_b + b + 1\\
(q^tx_a+b)-(w^tx_b+b)=2\\
w^t(x_a-x_b)=2\\
||x_a-x_b|| = \frac{2}{||w||}
\end{align}
$$
where:
- a and b are the identifiers for each vector

What this tells us is that the difference between those two vectors (the margin) is equal to $2\over ||w||$. Ans so the smaller that w gets, the bigger that difference will be. 
If we can find a min(w) then we should get the best w possible. 

$$
\begin{align}
\text{we want: }\space min(\frac{1}{2}||w||^2)\\
\text{subject to: }\space y_i(w^tx_i + b)\geq 1
\end{align}
$$

## allowing misclassification
There are some non-separable patters that wont be classifiable with a hard SVM classifier. 

***
### Up
- [[1758819746-linearseparation|linear separation]]
### Down
***
