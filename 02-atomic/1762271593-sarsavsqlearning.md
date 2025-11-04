---
aliases:
- SARSA vs Q-Learning
tags:
- ms
---
# SARSA vs Q-Learning
> [!info] Intro: 
> SARSA and Q-learning are two different implementations of temporal difference learning. This note discusses their differences. 

Both implementations take the next action accourding to the policy. However the action-value update differs.
**On-policy** uses a plicy to find the next action to take while **off-policy** just takes the best action. 
- For on policy this means assuming actions according to policy which may not be greedy. 
- For off policy means just updating the always with the greedy action. THe policy actually used and the policy for updates is different. #duda Not really understanding this

This makes it so **sarsa(on policy)** goes for safer paths wile **q-learning(off-policy)** chooses optimal but riskier paths. This means worse scores for q-learning than sarsa during training. 

However there is a big change when going onto applying the obtained state values after training. Because q-learning  
The compromise can be bridged by using an smaller epsilon with SARSA $\varepsilon-$greedy policy. 
***
### Up
- [[1762270792-sarsa|SARSA]]
- [[1762271227-qlearning|Q-Learning]]
### Down
***