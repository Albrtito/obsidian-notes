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
 - $q_{*}(a)$ -> Represents the reward for action a
 - 
***
### Up
### Down
***