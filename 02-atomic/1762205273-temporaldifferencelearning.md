---
aliases:
  - temporal difference learning
  - TDL
tags:
  - ms
---
# temporal difference learning
> [!info] Intro: 
> Temporal difference learning is a form of [[1762025473-reinforcementlearning|reinforcement learning]]. For this type of models the agent does not know everything but rather the opposite. Knows nothing. (opposite to [[1761231645-markovdecisionprocess|markov decision process]]). 
> All state values are initialized to zero and then updated. But how to updated them?

>[!important] Properties:
> - **no model of the enviroment:** They work by experience
> - **fully incremental**
> - **update befor knowing it all:** The update is only made based on the next stage. Then the full chain does not matter
> - **less memory and computation**
> - **convergent:** Under certain assumptions
## Intuition: 
Intuition is how the agents in TDL update the state's value. It'll first initialize all states with a value of 0. Then do a run and update the sate with the reward obtained after performing some action from that state. After that the update is done using: 
$$
V(S_{t}) \leftarrow V(S_{t}) + \alpha [R_{t+1}+ \gamma V(S_{t+1}) - V(S_{t})]
$$
**where:**
 - The <- means an update on the state value 
 - This update is perform using the previous value + some new update. 
 - This new update is applied based on some $\alpha$ that is the **learning rate**
 - The update is the difference between the the target value and the current value. So how much it increases.
 - The target value $R_{t+1}+\gamma V(S_{t+1})$ is obtained by summing the obtained reward when going to the state $S_{t+1}$ and the value of that state (this way the agent goes to states that also have better states with following actions). 
 - $\gamma$ -> The **discounting coefficient**

This method is the **simplest temporal-difference method TD(0)**
>[!important] Properties:
> This way of updating state-values has the following properties. 
> - **bootstrapping:** The update of the estimates of state-values is done using the estimates of the successor state-values.
> - **sampling:** The updates are only based on **ONE subsequente action or state**. #duda Is it because of this that the method has a 0? TD(0)


***
### Up
- [[1762025473-reinforcementlearning|reinforcement learning]]
### Down
- [[1762270199-implementationofatemporaldifferencelearningagent|implementation of a temporal difference learning agent]]
- [[1762270792-sarsa|SARSA]]
- [[1762271227-qlearning|Q-Learning]]
***