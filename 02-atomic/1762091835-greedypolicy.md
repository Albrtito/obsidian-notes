---
aliases:
- greedy policy
tags:
- ms
---
# greedy policy
> [!info] Intro: 
> Choosing greedy means choosing the best possible thing without looking at anything else.

## the greedy choice
If the agent chooses the action that gives the highest expected reward **in the next step** we say that it chooses the greedy action. 
$$
A*_{t} = arg \max _{a} Q_{t}(a)
$$

We always have the choice to do so of course. If we do and we always take the better choice we'll be doing **explotation** while if we don't always choose it then the agent will **explore** more. 
We cannot do them at the same time but in order to **not exploit all the time** we can use the $\varepsilon-\text{greedy}$ method.

### $\varepsilon-\text{greedy}$
With this method the agent is **usually greedy** but will choose a **random action** with a probability of $\varepsilon$. Usually small. 
- One of the simplest ways to balance exporation and exploitation. 
- When exploring it should take at random from either all options but the best one or from all the options. Careful about taking from all the options cause it can still choose the best option, which is not the idea. 
In order to perform this method we'll also use a counter to keep track of how many times each action was chosen.
#### choosing $\varepsilon$
When choosing a value for epsilon it usually happens that: 
- With epsilon = 0. The algorithm is completely greedy. There is no improvement with time. The algorithm finds the best option and does not explore with others. 
- With epsilon = 0.1. The algorithm finds a better solution, however still takes some of the worse approaches with time. It learns really fast in the beginning but does not get better after that. 
- With epsilon = 0.01. It takes more time to learn the best one but one learned it keeps improving with time as it chooses the greedy (best one) more often once learned. 
The best idea of course would be to have a **decaying epsilon**, so that there is more exploration at the beginning but then once a better solution is found it starts just being greedy with that solution. 
***
### Up
### Down
***