---
aliases:
- linear separation
tags:
- review
- ms
References:
cssclasses:
---
# linear separation
> [!NOTE] Intro: 
> Linear separatino is a method to classify data by creating a threshold that divides the data. 


> [!example] Dictionary:
> **margin →** the creates a margin, the space from the threshold to nearest object of a class. 

The objective in linera separation will be to obtain the **biggest margin possible (IT IS ALL ABOUT THE MARGIN)**. This margins can be represented as support vectors and are given by the threshold definition. 


> looking at the following example in 2D
>![[1758819746-linearseparationj.png|center|700]]

$$
\begin{align}
B1: w^Tx+ b = 0\\
b11: w^Tx+b = 1\\
b12: w^Tx+b = -1\\
\end{align}
$$

The decision then would be given by a function classifying into one class when something goes past either of the vectors. 
Where the vectors are defined by a line (as seen above). 
And the decision function between classes 1 and -1 will be given by: 
$$f(x)= \begin{cases}1 & \text { if } w^T x+b \geq 1 \\ -1 & \text { if } w^T x+b \leq-1\end{cases}$$

Because of this definition of the threshold and support vectors any point that when inputted into the equation ($w^Tx+b$) gets a value between -1 and 1 is inside the support vectors. If the value is 0 then it is in the threshold. 

The solution then for this kind of separations is the pair of values w, b. With w being a vector of coeficients and b the “ordenada en el origen”

**But how do we find this two values?** → Using [[1758821790-suportvectormachine|suport vector machine]]


***
### Up
### Down
- [[1758821790-suportvectormachine|suport vector machine]]
***
