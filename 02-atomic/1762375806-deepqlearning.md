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
(2) set U_t = r + gamma max_a q(s',a',theta)
	or U_t = r if s' is terminal
(3) theta <- theta + alpha[U_t - q(s,a,teta)] grad(q(s,a,theta))
(4) Repeat
```

See that the update is now changing the parameters as that is what really changes the Q values. 

>[!important] Properties:
> - **Bootsraping:** Only care about the next reached state
> - **Off-Policy learning:** Learn greedy
> - **Function approximation:** Use a DNN to get the Q values. 
> 
> This three properties altogether are called [[1762376174-thedeadlytriad|the deadly triad]]. 

However now, because we are changing the estimate based on an already changing value (the DNN approximation) the following problems appear:

>[!bug] Problems:
> 1. The subsequent observations are correlated
> 2. The target value $U_{t}$ keeps changing

In order to solve this problems: 
1. **Use experience replay:** Add a buffer that stores the past observations, then update based on that so that those observations do not keep changing. This adds an step:

```pseudocode
(1) Take some action a and observe (s,a,s',r), add it to B
(2) sample mini-batch {s_j, a_j, s'_j,r_j} from B uniformly
(3) set U_j = r_j + gamma max_a q(s'_j,a',theta) for all j
	or U_j = r_j if s'_j is terminal
(4) theta <- theta + alpha sum_j([U_j - q(s_j,a_j,teta)] grad(q(s_j,a_j,theta)))
(5) Repeat
```

2. **Use target network:** The target also changes all the time. Then we'll fix it. Creating a copy of the weights for the neural network and using those for some time while updating the real weights. Passed some episodes we'll update the copy with the current weights. The new algorithm then takes the form:

```pseudocode
(1) Take some action a and observe (s,a,s',r), add it to B
(2) sample mini-batch {s_j, a_j, s'_j,r_j} from B uniformly -- added from the experienced replay
(3) set U_j = r_j + gamma max_a q(s'_j,a',theta) for all j
	or U_j = r_j if s'_j is terminal
(4) theta <- theta + alpha sum_j([U_j - q(s_j,a_j,teta)] grad(q(s_j,a_j,theta)))
(5) Repeat
```
***
### Up
### Down
***