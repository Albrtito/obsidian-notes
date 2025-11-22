---
aliases:
- implementation of a temporal difference learning agent
tags:
- ml
---
# implementation of a temporal difference learning agent
> [!info] Intro: 
> Given the most basic temporal different learning agent TD(0). We could implement this in the following way (pseudocode)

```pseudocode
Input: the policy (pi) to be evlauated
Initialize V(s) arbitrarily (with all equal to 0, usually)
Repeat(for each episode):
	Initialize S
	Repeat (for each step of episode):
		A <- action given by pi for S
		Take action A, observe R, S' 
		V(S) -> V(S) + alpha[R+gammaV(S')-V(S)]
		S <- S`
	until S is terminal 
```

**where:**
- S' represents the next state

***
### Up
- [[1762205273-temporaldifferencelearning|temporal difference learning]]
### Down
***