---
aliases:
- implementing decision trees in python
tags:
- review
- ms
References:
cssclasses:
---
# implementing decision trees in python
> [!NOTE] Intro: 
> To use decision trees in python there are several libraries. 
> 

With **scikit-learn**: 
```python
import DecisionTreeClassifier 
import DecisionTreeRegressor
```
where: 
- **DecisionTreeClassifier** → The class for classifying
- the other one is just for regression
- It uses the [[1758924692-giniindex|gini index]] by default
- Suports only numeric attributes 
- Only binary splits
- **Complexity:** $O(n\cdot m \cdot log_2(m))$ 
  Complexity not tested during ms course



***
### Up
- [[1758919079-decisiontrees|decision trees]]
### Down
- [[1758924692-giniindex|gini index]]
***
