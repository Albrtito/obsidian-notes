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
> - **t->** When we use t in math and definitions we refer to the time. The times we have done someting. There will be a finite number of t (repetitions) that will be performed.

>[!important] Properties:
> - **Realistic learning:** This type of learning is more realistic than others as the actions and consecuences are similar to the real world. The agent learns by **trial and error**.
> - **Unknown enviroment:** The agent can learn by itself from an unknown enviroment based on its own experience.
> - **Deterministic|Non-deterministic rewards:** There are two types of rewards
> 	- **Deterministic**, meaning that they are always the same for some given action
> 	- **Non-Deterministic:** This means that they are not always the same. Usually following a distribution. 

## reinforced vs other learning

Like in supervised learning there are rewards and feedback. However there is no dataset of known cases or labels for each case telling the agent twhat the right answer is. 

With unsupervised learning there is not as much similarity. However it does share the idea of there not being some perfect behaviour or correct actions.
Unsupervised learning still does not have any feedback loop (rewards), there is no enviroment and again, reinforced learning does not use a data set. 

## choosing an action:

### rewards and estimates:
We can obtain the **real expected** reward for some specific action as: 
$$
q_{*}(a) = \mathbb{E} [R_{t}|A_{t}=a]
$$
**where:**
 - $q_{*}(a)$ -> Represents the expected reward for an action a
 - The expected value is the sum of the probabilties of obtaining one reward times the reward. (P1*R1 + P2*R2+...). 
 - $R_T$ -> Is the fixed reward value.

However the agent does not know this expected reward, this is what we are trying to teach it. It still need to maximize the total reward. To do so it goes into a trial and error cycle. Try actions, estimate their rewards/values and prefer those that appear best, giving each action and state some **estimate** on how good it is: $Q_{*}(a)$. 
The agents uses: 
- [[1762085025-actionvaluemethodsinrl|action-value methods in RL]]

### [[1762091784-policy|policy]]: 
Once we have some trial and error values on what the best actions are based on the experience of the model we still can choose between which action to take.
***
### Up
### Down
- [[1762085025-actionvaluemethodsinrl|action-value methods in RL]]
- [[1761237890-mdppolicy|policy]]
- [[1761231645-markovdecisionprocess|markov decision process]]
- [[1762205273-temporaldifferencelearning|temporal difference learning]]
***