---
aliases:
- policy selection
tags:
- ms
---
# policy selection
> [!info] Intro: 
> What actions to take and with what probability to take them. We can use different strategies for this.
> Defined as:
> $$
> \pi_{t}(a|s)
> $$
> **where:**
> This means probability of taking action a given that the agent is in state s. And $S_{t} = s$
> For deterministic policies:
> $$
> \pi_{t}(s) = action
> $$

1. **Greedy action selection ->** Always take the greedy action (the best one, greater rewards)
2. $\varepsilon$**-greedy ->** Select the greedy action with probability 1-$\varepsilon$ and explore with probability $\varepsilon$. 
3. **Preference based** -> Select action on rewards obtained. Develop preferences affecting the probability to take each action.

Now based on how return and rewards are calculated **we can use a value function to decide on which state is better by looking at the future rewards**. (This keeps on with the idea that ther there is no actual need to know how we got to the state we are at, only the future states)

>[!attention] Remarks:
> - Things depend on what is afterwards. Good actions and good states are so based on on what comes afterwards.
> - This two things are dependent. So how good an action is depends on the state the agent is at and vice versa

How we choose this value function and this policy can actually a

***
### Up
- [[1761231645-markovdecisionprocess|markov decision process]]
### Down
- [[1761239003-returnvsrewardinreinforcementlearning|return vs reward in reinforcement learning]]
***
