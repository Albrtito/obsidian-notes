---
aliases:
- using EAs to select features
tags:
- ms
---
# using EAs to select features
> [!info] Intro: 
> Evolutionary algorithms can also be used to select a subset of features that can later be used with other models. 
> This can be done by just creating and using a EA that then outputs a result in which some features had more impact than others. The more impactfull features can be kept while the rest of them are discarted.

This can be brought one step further by **using as fitness function the chosen classifier's accuracy**
> So if we want to use a KNN classifier and see what are the best features that should or should not be used. We can train an EA and see how good is the classifier doing for each invididuals features.
***
### Up
- [[1759827624-evolutionaryalgorithms|EAs]]
### Down
***