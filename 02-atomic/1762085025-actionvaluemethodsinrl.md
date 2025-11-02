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
 
>[!important] Properties:
> - **Convergence->** If we average over enough trials ourestimate will. be equal to the actual action-value (rewards):
>   $$\lim_{ N_{t}(a) \to \infty } Q_{t}(a) = q_{*}(a)$$
> - **Efficient averaging->** In order to not save all rewards to get the average we'll just use the last average and update that with the new found values. 
>   $$Q_{t+1}=\frac{1}{t}\sum_{i=1}^tR_{i}\rightarrow Q_{t+1} = Q_{t} + \frac{1}{t}[R_{t}-Q_{t}]$$
>   **where:**
>   - See that we add to the old average $Q_{t}$ the difference between the new reward and the old average. #duda Why is is that the reward is $R_t$ not $R_{t+1}$?
> - **Equally important values->** All values (times we have seen rewards) are equally important.
## the greedy choice
If the agent chooses the action that gives the highest expected reward **in the next step** we say that it chooses the greedy action. 
$$
A*_{t} = arg \max _{a} Q_{t}(a)
$$

We always have the choice to do so of course. If we do and we always take the better choice we'll be doing **explotation** while if we don't always choose it then the agent will **explore** more. 
We cannot do them at the same time but in order to **not exploit all the time** we can use the $\varepsilon-\text{greedy}$ method.

### $\varepsilon-\text{greedy}$
With this method the agent is **usually greedy** but will choose a **random action** with a probability of $\varepsilon$. Usually small. 
- One of the simplest ways to balance exporation and exploitation. 
- When exploring it should take at random from either all options but the best one or from all the options. Careful about taking from all the options cause it can still choose the best option, which is not the idea. 
In order to perform this method we'll also use a counter to keep track of how many times each action was chosen. 
***
### Up
### Down
- [[1762086887-explorationvsexploitation|exploration vs exploitation]]
***