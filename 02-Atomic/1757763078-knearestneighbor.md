---
aliases:
  - k-nearest neighbor
  - knn classifier
tags:
  - review
  - ms
References:
cssclasses:
---
# k-nearest neighbor
> [!NOTE] Intro: 
> The k nearest neighbor classifier compares each point (sample) with the k nearest neighbors around it. It uses the data it already has to categorize new points. 
> 
- **Class likelyhood:** Is decided based on how many observations of each type where found inside the k neighbors. 
- There is no really any training involved into this method. We are just comparing the data based on some rules. This is called **lazy learing or instance based learning**

# Choice of k: 
Chosing a good number for k is crucial for the model, as a very big or small k will drastically alter the results. 

- Small values could give to much importance to outliers. (**overfitting**)
- Big values could take out the importance of actual data if there is few of it. (**underfitting**)

In order to chose a good k value we need to test empirically. Also the used distance function is crucial. (euclid or manhattan distance)

## Distance function: 
The distance function could be: 
- Manhattan 
- Eculidean 
- Other

Take into account that this classifier can be used for 

## Voting:
In order to choose the actual value for the point we can either perform: 
- Mayority vote (what type of neighbor does it have more)
- Weight according to the distance: $w = 1/d^2$

# Preprocessing:


***
### Up
### Down
***
