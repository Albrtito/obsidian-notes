---
aliases:
  - reinforcement learning
  - RL
tags:
  - ms
---
# reinforcement learning
> [!info] Intro: 
> Reinforcement learning is agent oriented learning. This means that there is an agent that can interact with an enviroment in order to achieve a goal. 


This creates three basic relations. 
- The Agent performs **actions** to interact with the enviroment
- The enviroment **changes** and with it its **state** based on the agents actions
- The enviroment **rewards** the agent based on their actions and how good they where. 
  - Reward design is important as the agent will get better on what gets the greatest reward.
  - It is also important for the agent to look for the best way to get a greater **cummulative reward**. Not only the inmediate reward with time. 

>[!example]- Dictionary:
> - **agent ->** The person or object doing the learning
> - **action ->** What the agent can do to interact with the enviroment. Something that the agent does
> - **enviroment ->** The setting the agent learns in
> - **state ->** A collection of properties that the enviroment has at some given moment
> - **reward ->** Positive or negative (**penalty**) based on the actions of the agent. Marking if they where good or not. Rewards are **inmediate**

>[!important] Properties:
> - **Realistic learning:** This type of learning is more realistic than others as the actions and consecuences are similar to the real world. The agent learns by **trial and error**.
> - **Unknown enviroment:** The agent can learn by itself from an unknown enviroment based on its own experience.

## reinforced vs other learning

Like in supervised learning there are rewards and feedback. However there is no dataset of known cases or labels for each case telling the agent twhat the right answer is. 

With unsupervised learning there is not as much similarity. However it does share the idea of there not being some perfect behaviour or correct actions.
Unsupervised learning still does not have any feedback loop (rewards), there is no enviroment and again, reinforced learning does not use a data set. 

## calculating rewards:

We can obtain the expected reward for some specific action as: 
$$
q_{*}(a) = \mathbb{E} [R_{t}|A_{t}=a]
$$
**where:**
 - $q_{*}(a)$ -> Represents the expected reward for an action a
 - The expected value is the sum of the probabilties of obtaining one reward times the reward. (P1*R1 + P2*R2+...). 
 - $R_T$ -> Is the fixed reward value.

However the agent does not know this expected reward. It still need to maximize the total reward. To do so it goes into a trial and error cycle. Try actions, estimate their rewards/values and prefer those that appear best. While doing so an **estimate** is created for some action a $Q_{*}(a)$. 
The agent will try the action a and see what the reward is. Then update the estiamte with that reward (all estimates start at 0).Of course all actions must be tried, if not some good rewards at the begining  would obscure some better rewards waiting further along. The agent tries multiple times and averages the estimate. 
$$
Q_{t}(a) = \frac{\text{sum of rewards when a taken prior to t}}{\text{number of times a taken prior to t}} = \frac{\sum^{t-1}_{i=1}R_{i} \cdot 1_{A_{i=a}}}{\sum_{i=1}^{t-1}1_{A_{i=a}}}
$$
**where:**
 - When using $1_{A_{i=a}}$ we mean: 1 if 
***
### Up
### Down
***