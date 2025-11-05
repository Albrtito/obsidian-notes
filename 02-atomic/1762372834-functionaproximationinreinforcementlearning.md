---
aliases:
  - function approximation in reinforcement learning
tags:
  - ms
---
# function aproximation in Reinforcement Learning
> [!info] Intro: 
> What if the number of states and actions is huge? (e.g. chess). Then we find that temporal difference models such as [[1762271227-qlearning|Q-Learning]] or [[1762270792-sarsa|SARSA]] require high memory to save all the state-actoin pairs in to the [[1762372623-qmatrix|q-matrix]] as well as a really long time to populate the table. Function approximation is a new way of obtaining Q values that **uses a deep neural network (DNN)** to approximate the Q values. 

But if using a deep neural network it needs to learn the parameters, therefore function approximation is used **when the number of learned parameters is smaller than the number of entries in the Q-table**

>[!important] Properties:
> - **Generalization:** This new approach can create a Q value for every state pair. It may not be the best of them all but it is not zero. However with temporal difference learning if a q value is not there it cannot be created.

Because the parameters need to be learned, the new Q values are obtained given an state, action and parameters. This Q values try to estimate the q value that would be obtained given a policy (like in TDL).
$$
Q(s,a,\theta) \approx q_{\pi}(s,a)
$$
**where:**
 - s,a,$\theta$ -> State,action, parameters
 - **The parameters is what needs now to be updated every episode**
The policy then acts **nearly greedy**, almost taking the max value proposed by the DNN.
$$
\pi(s) \approx arg\max_{a} Q(s,a,\theta)
$$

## Applying it to SARSA and Q-Learning. 
Now using this new Q value function we obtain into Sarsa and Q-Learning: 

**SARSA**
$$
U_{t} = R_{t+1} + \gamma Q(S_{t+1},A_{t+1},\theta)
$$
**Q-Learning:**
$$
U_{t} = R_{t+1} + \gamma\max_{a}Q(S_{t+1},a',\theta)
$$
**where:**
 - The new updated value is named U instead of Q as the Q function does not change based on the next value it takes. 
 - This new version of Q-Learrning is called [[1762375806-deepqlearning|deep q-learning]]
***
### Up
### Down
***