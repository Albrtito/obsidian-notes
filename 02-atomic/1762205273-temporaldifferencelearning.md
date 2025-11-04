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
 - The target value $R_{t+1}+\gamma V(S_{t+1})$ is obtained by summing the obtained reward when going to the state $S_{t+1}$ and the value of that state (this way the agent jnow )
***
### Up
- [[1762025473-reinforcementlearning|reinforcement learning]]
### Down
- [[1761231645-markovdecisionprocess|markov decision process]]
***