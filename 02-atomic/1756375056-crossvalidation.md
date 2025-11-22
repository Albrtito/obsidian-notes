---
aliases:
  - cross-validation
tags:
  - review
  - ml
References:
cssclasses:
---
# cross-validation
> [!NOTE] Intro: 
> Cross-validation is used in ms to measure how good a model is. We use it to look for overfitting and errors in our model. 
> For this method we’ll separate all the data into different sections based on the type of training that is gonna be done. 

**Remarks:**
- It is really important that the **sampling data of the different sections is REPRESENTATIVE** (it has random values). We can use two sampling techniques for this
	- Simple random sampling → Random
	- Stratified sampling → Apply some criteria
## Validation data:
Used to decide between different models before performing the final testing. When using the validation data we say that we are doing **model selection**

## Test data:
Test data is **not touched or used in any ways until the final model is done**

Then we can look at the results for our test data compared for the results for testing data. When the results for test data start to worsen we’ll know that the model is not generalising anymore but overfitting. 
The act of using the test data to asses how good a model is i s called **model assesment**

***
### Up
- [[1756374897-solutionsforoverfitting|solutions for overfitting]]
### Down
***
