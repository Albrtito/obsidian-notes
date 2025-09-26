---
aliases:
  - decision trees
  - CART
tags:
  - review
  - ms
References:
cssclasses:
---
# decision trees
> [!NOTE] Intro: 
> One of the most widely used techniques for classification, very efficient while still being a simple concept. Can be used both for classification and regression 
> Super nice cause it is a white box model


> [!example] Dictionary:
> - **CART** → Classification And Regression Tree
> - **root node** → The initial node, parent to any other note
> - **internal|split node** → NOt a leaf node or decision node
> - **rule** → Change applied to get to the next node 
> - **leaf node** → Final node that defines a class (solution)
> - **gini →** Purity marker, how good is this node. How many instances of each class there is in this node 

The goal of decision trees is to **output a SET OF RULES that classify the data into the required classes.**

1. Start in the root node
2. If we are in a leaf node return the class
3. If were are in a split node, perform the operator to decide to which leaf node to go

The **complexity** of this trees will be: 
$$
O(log_2(m))
$$
where: 
- m → number of examples in the training set

This is super nice because it means that the **complexity goes independentily from the number of variables**. 

## analysis of a tree: 

Given a tree each node will not only contain the rules but also some other interesting values. 

> looking at the iris db tree

![[1758919079-decisiontreesj.png|center]]

- The **gini and value** properties tell us about the purity of the split and number of instances there is at the node from each class. 
- The **** property gives us the value for the class that that node represents.

- We can get some class probabilities based on the number of observations from each class at each leaf. So if we have 20 observations and at a leaf we have one observation of one type. Is a class probability of 1/20. This can be calculated based on the value vector shown. 

## how do we generalize this?

The idea is nice, buthow can we do it with a computer? Which values do we choose?
The solution is **recursive partitioning**. 

One value is chosen at random and several values are chosen for it. Then measure how pure the resulting portions are (measure the gini). After getting the purest split the algorithm goes for the next split. 

Ok but doing this is irreal if we want to perform all the actual splits that exists in the tree. 
With n binary attributes we have $2^{2^n}$ truth tables. 
> 6 attributes → $10^{20}$ different trees

## hyperparameters:
- **minimum leave size | samples per split** → Minimum number of observations that need to be in each leaf after a split. So this regulates if we can split a leave or not based on the number of observations that will end up in each of the leaves.
  - Really small leaf size can easily **overfit** to noise. So it looses generalisation.
- **maximum depth** → How many splits can we make downwards. 
- **maximum leaf nodes** → Max number of terminal nodes there can be
- **purity function** → Function that is used to determine the purity of a split. An example is the **gini**

## making splits: 
Splits depend on the attribute type, usually for binary values we’ll do a two way split, however a **multi-way split** can also be done for variables with more than one value.


> [!attention] Remark:
> Never do splits on ID. DONT USE ID. 

**multi-attribute variables**
But this is not the only solution as we can also put more than one value for the variable at each of the splits. 
However **binary splits must preserve the order of the values**

> So for a variable x = {1,2,3,4} a split: 
> - S1 → {1,2}
> - S2 → {3,4}
> Is possible, however the split:
> - S1 → {1,4}
> - S2 → {3,2}
> Is not preserving the order and therefore is not a binary split 

 
**continuous variables**
Usually either set them into different classes or set a rule (inequality) to make it into a binary split. 

### impurity measurements:
To determine the best split we must use some measurement to compare things with, we could use: 
- [[1758924692-giniindex|gini index]]
- entropy
- simple missclassification error: How many  points are not classified in their class

This can also be done applying weights to each class, solving he problems that appear when some classes are greater than others. 

We can use the missclassification as a weight. #duda → Not really getting this


***
### Up
### Down
- [[1758924692-giniindex|gini index]]
***
