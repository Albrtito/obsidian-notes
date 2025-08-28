---
aliases:
  - confiusion matrix
tags:
  - review
  - ml
References:
cssclasses:
---
# confusion matrix
> [!NOTE] Intro: 
> Method for evaluation of results of a **discrete/clasification** ms model. It creates a matrix defined by the actual category in one axis and the predicted category on the other one. Then we obtain four (for binary) cells. 
> 
> 1. **True values predicted true**
> 2. True values predicted false 
> 3. False values predicted true
> 4. **False values predicted false**
>
> *The ones in bold are the good ones

### The problem with accuracy
Just knowing that the accuracy of a model is really high does not tell us if it’s a good model or not. This is because there may be some problems with the prediction of one of the classes, this is called **class inbalance**
> example: 
> For a model that needs to predict the illnes of 10 patients out of 10000, if it predicts that everyone is healthy the accuracy will still be really high (99.9%), however it did not actually predict the important thing (the sick people)

This problem with accuracy will happen if:
- The class distribution is **skewed**
- Error cases are not equally important

### How precision and recall solves it:
The recall will give us the total of **positive cases that are correctly predicted**. This lets us know how good are we clasifying one of the classes. (usually the one we care about in binary classification)

The precision focusses on the prediction of **positive values**, when do we predict something as positive, both for aactual positives and negative predicitons. 
So it is measuring how many times **the model predicted some positive values and it was right**. 
> So if a model predicted 6 values to be true and only 4 of them are, then the recall is 4/4 (all the true values were correctly predicted) but the precision is 4/6, of the positive predicted values only 4 where right.

#### The tradeoff: 
There is a tradeoff between precision and recall based on the threshold from which we detect a true value. Every prediction will have some assurance (%), if the threshold for a true value is smaller, the recall will be bigger but the precision smaller. If we turn it around same thing happens but in reverse, for a big threshold the precision gets better but the recall gets worse. 

This is not a linear relation, although it depends on the model we can get a value near to 80% for both precision and recall. Of course we allways want to maximize both as most as possible. 
The action of looking for this threshold is called **thresholding.** 

The better model is the one that can maintain a higher precision for a longer time. The larger the area the better. 
***
### Up
### Down
***
