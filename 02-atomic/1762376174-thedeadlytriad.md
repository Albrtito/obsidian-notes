---
aliases:
- the deadly triad
tags:
- ms
---
# the deadly triad
> [!info] Intro: 
> The deadly triad referes to a RL algorithm that uses three elements at the same time: **Bootstrapping**, **off-policy** learning and **function approximation**. The following property appears:
> If any of these is removed the Q-values will converge (**good**) (for sufficiently small alpha) however with all three the values might diverge (for any alpha and reasonable gamma)

There are two possible solutions:
1. Skip one of the three
2. Work around to address the instability that may lead to the divergence
Lets go more deeply into this:

**What do we get rid of?**
- Function approximation if the q-table is small, if not no way
- Bootstraping is what we want for computational efficiency, saving all the sequence is just mad 

Maybe give off-policy? 
We can sometimes and use then [[1762270792-sarsa|SARSA]]. But not always a good choice.


***
### Up
### Down
***