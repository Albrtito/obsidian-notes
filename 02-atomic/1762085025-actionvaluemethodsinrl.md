---
aliases:
- action-value methods in RL
tags:
- ms
---
# action-value methods in RL
> [!info] Intro: 
> The action-value methods of a reinforced learning model are those that define the value that each action has. In other words, how good each action is. The agent does this by analyzing the rewards obtained after each action. 

>[!important] Properties:
> - **Convergence->** If we average over enough trials ourestimate will. be equal to the actual action-value (rewards):
>   $$\lim_{ N_{t}(a) \to \infty } Q_{t}(a) = q_{*}(a)$$
> - **Equally important values->** All values (times we have seen rewards) are equally important.
First of all, we need to know if the rewards are stationary or not: [[1762090583-stationaryvsnonstationaryrewarddistribution|stationary vs nonstationary reward distribution]]

**Stationary rewards:**
The agent will try the action a and see what the reward is. Then update the estiamte with that reward (all estimates start at 0).Of course all actions must be tried, if not some good rewards at the begining  would obscure some better rewards waiting further along. The agent tries multiple times and averages the estimate. 
$$
Q_{t}(a) = \frac{\text{sum of rewards when a taken prior to t}}{\text{number of times a taken prior to t}} = \frac{\sum^{t-1}_{i=1}R_{i} \cdot 1_{A_{i}=a}}{\sum_{i=1}^{t-1}1_{A_{i}=a}}
$$
**where:**
 - When using $1_{A_{i}=a}$ we mean: 1 if $A_{i}=a$. So only take into account the rewards for the action we are estimating. 
 - For the lower part, we are just summing the number of actions of this type that we took in order to compute the average. 

This can be simplified:
**Efficient averaging**
In order to not save all rewards to get the average we'll just use the last average and update that with the new found values. 
   $$Q_{t+1}=\frac{1}{t}\sum_{i=1}^tR_{i}\rightarrow Q_{t+1} = Q_{t} + \frac{1}{t}[R_{t}-Q_{t}]$$
**where:**
   - See that we add to the old average $Q_{t}$ the difference between the new reward and the old average. #duda Why is is that the reward is $R_t$ not $R_{t+1}$?

**Non-stationary rewards:**
Updating each reward is not done with the average value but with a fixed alpha value. The new efficient averagin is then:

$$
Q_{t+1}= Q_{t} + \alpha[R_{t}-Q_{t}]: 0 < \alpha \leq 1
$$
 Here we see that each new value has an impact of $\alpha$ contrary to how each value had the same impact with the previous method. This means that the most recent value is more important. 

***
### Up
### Down
- [[1762086887-explorationvsexploitation|exploration vs exploitation]]
- [[1762090583-stationaryvsnonstationaryrewarddistribution|stationary vs nonstationary reward distribution]]

***