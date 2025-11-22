---
aliases:
- episodic vs continuing tasks
tags:
- ml
---
# episodic vs continuing tasks
> [!info] Intro: 
> When talking about returns and rewards in ms we'll find that each task has some reward and we need to sum them all up to find the return. When doing so we need to separate between two types of tasks.
> - **episodic tasks ->** Those that happen and stop happening, finite. A final state is reached. Easy to get return as we can just sum it all up. 
>   Here **events are independent from each other**
> - **continuing tasks ->** Tasks go on and on and on, never ending. If we just sum all the rewards the problem is that the first rewards do not have importance anymore (probably). So we use a variable to "forget" with the pass of time.
>   $$
> G_{t}=R_{t+1} + \gamma R_{t+2} + \gamma^2R_{t+3} + \dots = \sum_{k=0}^\infty \gamma^k R_{t+k+1}
> $$
> **where:**
> - The $\gamma$ is the discounting coefficient. 
> - The first rewards have more impact than the latter ones [[1761239003-returnvsrewardinreinforcementlearning|return vs reward in reinforcement learning]]
***
### Up
### Down
***

## ipact of discounting:
The discounting coefficient can be any value between 0 (shortsighted) and 1 (farsighted). We usually use farsighted values as the rewards in the future still hold some value and we still need to show that. 
A really high value in the future is still really worth it. 

## choosing and the effect on rewards:
To choose between one of this two types of task we'll have to look into the type of event that we are processing. Also some events can be seen as both episodic and continuoius. 
Also for episodic tasks we can use discounting by looping with 0 reward forever in the end state. **So it is ok to use discounting for episodic tasks**
***
### Up
- [[1761231645-markovdecisionprocess|markov decision process]]
### Down
- [[1761239003-returnvsrewardinreinforcementlearning|return vs reward in reinforcement learning]]

***
