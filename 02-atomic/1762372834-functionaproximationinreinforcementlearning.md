---
aliases:
  - function approximation in reinforcement learning
tags:
  - ms
---
# function aproximation in Reinforcement Learning
> [!info] Intro: 
> What if the number of states and actions is huge? (e.g. chess). Then we find that temporal difference models such as [[1762271227-qlearning|Q-Learning]] or [[1762270792-sarsa|SARSA]] require high memory to save all the state-actoin pairs in to the [[1762372623-qmatrix|q-matrix]] as well as a really long time to populate the table. Function approximation is a new type of reinforcement learning that **uses a deep neural network (DNN)** to approximate the Q values. 

But if using a deep neural network it needs to learn the parameters, therefore function approximation is used **when the number of learned parameters is smaller than the number of entries in the Q-table**

>[!important] Properties:
> - **Generalization:** This new approach can create a Q value for every state pair. It may not be the best of them all.

***
### Up
- [[1762025473-reinforcementlearning|reinforcement learning]]
### Down
***