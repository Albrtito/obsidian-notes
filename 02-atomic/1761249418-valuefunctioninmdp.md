---
aliases:
- value function in MDP
tags:
- ms
---
# value function in MDP
> [!NOTE] Intro: 
> The value function in MDP provides us with the decision on which state should the agent visit next. For this it uses the [[1761239003-returnvsrewardinreinforcementlearning|reward and return]] values. 
> It will be used along the policy to determine the next state to transition to.

Now based on how return and rewards are calculated **we can use a value function to decide on which state is better by looking at the future rewards**. (This keeps on with the idea that ther there is no actual need to know how we got to the state we are at, only the future states)

>[!attention] Remarks:
> - Things depend on what is afterwards. Good actions and good states are so based on on what comes afterwards.
> - This two things are dependent. So how good an action is depends on the state the agent is at and vice versa

## the optimal value:
What if we dont care about the policy? Usually we'll have a policy that also decides on which decisions to take. This policy may be super bad or super good. So what if **we had the perfect policy**? This is called the optimal value function. 
The equation that gives this is called the **bellman optimality equation** and it is represented with $v_{*}$:

$$
\begin{aligned}
v_*(s) & =\max _{a \in \mathcal{A}(s)} q_{\pi_*}(s, a)=\underline{\frac{\max_a}} \sum_{{s^{\prime}, r}} p\left(s^{\prime}, r \mid s, a\right)\left[r+\gamma v_*\left(s^{\prime}\right)\right] \\
& \doteq \max _\pi v_\pi(s)
\end{aligned}
$$
**where:**
 - See that we are taking the max instead of 


***
### Up
- [[1761231645-markovdecisionprocess|MDP]]
### Down
- [[1761237890-mdppolicy|policy]]
- [[1761239003-returnvsrewardinreinforcementlearning|return vs reward in reinforcement learning]]
***