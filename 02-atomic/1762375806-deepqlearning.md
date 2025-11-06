---
aliases:
- deep q-learning
tags:
- ms
---
# deep q-learning
> [!info] Intro: 
> Deep q learning is a evolution of q-learning that uses a Deep Neural Network (DNN) to replace the Q table. This note contains its implementation. See that it is the same as in [[1762271227-qlearning|Q-Learning]] but with the update changed.

>[!example]- Dictionary:
> - **deep q network (DQN)->** The DNN used to approximate the q values.

```pseudocode
(1) Take some action a and observe (s,a,s',r)
(2) set U_t
```

See that the update is now changing the parameters as that is what really changes the Q values. 

>[!important] Properties:
> - **Bootsraping:** Only care about the next reached state
> - **Off-Policy learning:** Learn greedy
> - **Function approximation:** Use a DNN to get the Q values. 

This three properties altogether are called [[1762376174-thedeadlytriad|the deadly triad]]. 

***
### Up
### Down
***