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
>   $$ data= \{(x_i,y_i)\}^n_{i=1}$$
>   where:
>   - $x_i$ → Is a vector with all variables for the row i
>   - $y_i$ → Is the class for that row
> - **loss function** → Defines the error that the model is making for some observation|row i:
>   $$L(y_i, F(x_i))$$
> - **m** → Use to identify a tree. The algorithm uses m tree models

The algorithm works performing the following steps: 
#duda → This whole algorithm is a little dizzy for me
#incomplete → Relook at the node while looking again at the class it was tought at
- Create a note for xgboosting (implementation of gradient boosting in python with sctlearn)

1. Initialize the model with a constant value for the loss function. $$L(\_,\beta) = cnst$$
   But which constant? For that we we’ll look at the minimum value for the constant so that the loss is minimum, the following equation defines the value for the hypothesis in the first iteration, in need of the minimum value for beta.
   $$
   F_0(x) = argmin_\beta\sum^n_1L(y_i,\beta)
   $$
   Here we are looking for the value of beta (the constant) that minimizes it all. So we will just take the derivative and see when is it that that derivative equals 0 → max or min. 
   $$
   \beta = \frac{dL}{d \beta}
   $$
2. For each decision tree (given some number m of trees)
	1. Check how big is the error
	   We’ll do this using the pseudo-residuals (difference between the predicted value and the actual one)
	   $$
	   r_{im} = -[\frac{\partial L(y_i, F(x_i)}{\partial F(x_i)}]_{F(x)=F_{m-1}(x)}
	   $$
	   where:
	   - **m** → Tree number
	   - **i** → Variable number
	     
	2. Build another tree to fit the error
	   This new tree will fit several residuals for each leaf, this means that we have to somehow leave only one value for each leaf.
	   The solution is to perform again the argminus given those two values and the actual values. This will pan out to be the mean if we are using MSE
	   At the end this new model corrects the last one based on some **learning rate** so that we dont overfit.
	   $$
	   F_m(x) = F_{m-1}(x) + n \sum y_{jm}I (x\in R_{jm})
	   $$
	   where:
	   - The learning rate will usually be a small value, if not it would overfit
	3. Check how good we did, update the error
	   
3. Update the predicted value after the m trees

Using an example to understand all of this better:

***
### Up
- [[1758919079-decisiontrees|decision trees]]
- [[1757411969-boosting|boosting]]
### Down
- [[1758737329-meansquarederrorfunction|MSE]]
***
