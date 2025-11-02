---
aliases:
- action-value methods in RL
tags:
- ms
---
# action-value methods in RL
> [!info] Intro: 
> The action-value methods of a reinforced learning model are those that define the value that each action has. In other words, how good each action is. The agent does this by analyzing the rewards obtained after each action. 

The agent will try the action a and see what the reward is. Then update the estiamte with that reward (all estimates start at 0).Of course all actions must be tried, if not some good rewards at the begining  would obscure some better rewards waiting further along. The agent tries multiple times and averages the estimate. 
$$
Q_{t}(a) = \frac{\text{sum of rewards when a taken prior to t}}{\text{number of times a taken prior to t}} = \frac{\sum^{t-1}_{i=1}R_{i} \cdot 1_{A_{i}=a}}{\sum_{i=1}^{t-1}1_{A_{i}=a}}
$$
**where:**
 - When using $1_{A_{i}=a}$ we mean: 1 if $A_{i}=a$. So only take into account the rewards for the action we are estimating. 
 - For the lower part, we are just summing the number of actions of this type that we took in order to compute the average. 

## the greedy choice
If the agent chooses the action that gives the highest expected reward **in the next step** we say that it chooses the greedy action. 
$$
A*_{t} = arg \max _{a} Q_{t}(a)
$$

We always have the 

***
### Up
### Down
***