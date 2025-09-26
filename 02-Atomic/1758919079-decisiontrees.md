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

## how do we generalize this?

The idea is nice, buthow can we do it with a computer? Which values do we choose?
The solution is **recursive partitioning**. 

One value is chosen at random and several values are chosen for it. Then measure how pure the resulting portions are (measure the gini). After getting the purest split the algorithm goes for the next split. 

***
### Up
### Down
***
