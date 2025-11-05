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
Parameters: step size alpha in [0,1], small epsilon > 0. 
Init Q(s,a, theta) for all states and all actions A(s) arbitrarily except that the Q(terminal,*) = 0. 
Loop for each episode:
	Init S
	Loop for each step of episode:
		Chose A from S using policy derived from ANN q(s,a,theta)
		Take action A, observe R,S' 
		theta <- theta + alpha[R_(t+1)+gamma max_(a)q(S_(t+1),a',theta)-q(S_t,A_t,theta)] gradient(q(S_t,A_t,theta))
		S <- S';
	until S is terminal
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