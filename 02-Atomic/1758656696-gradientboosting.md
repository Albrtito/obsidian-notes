---
aliases:
- gradient boosting
tags:
- review
- ms
References:
cssclasses:
---
# gradient boosting
> [!NOTE] Intro: 
> Gradient boosting applies boosting by **fitting a model into the last model residuals**.
> - For this we use trees
> 

> [!example] Dictionary: 
> - **input** → The input of this model is given as: 
>   $$ Data\{(x_i,y_i)\}^n_{i=1}$$
>   where:
>   - $x_i$ → Is a vector with all variables for the row i
>   - $y_i$ → Is the class for that row
> - **loss function** → Defines the error that the model is making for some observation|row i:
>   $$L(y_i, F(x_i))$$
> - **m** → Use to identify a tree. The algorithm uses m tree models

## algorithm:
The algorithm works performing the following steps: 

1. Initialize the model with a constant value for the loss function. $L(\_,\_) = cnst$
2. For each tree (given some number m of trees)
	1. Check how big is the error
	2. Build another tree to fit the error
	3. Check how good we did, update the error
3. Update the predicted value after the m trees

***
### Up
- [[1757411969-boosting|boosting]]
### Down
***
