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
> Method for evaluation of results of a ms model. 

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
#duda: Not really getting what is this used for. 


***
### Up
### Down
***
