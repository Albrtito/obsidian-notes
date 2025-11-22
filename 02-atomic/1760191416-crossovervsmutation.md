---
aliases:
  - crossover vs mutation
  - recombination vs mutation
tags:
  - ml
---
# crossover vs mutation
> [!NOTE] Intro: 
> What is more important, crossover (recombination of parents properties) or mutation (random changes) in the child creation process of EAs? 

In general we'll say that it depends on the problem..but

> [!attention] Remark
> An **only mutation EA is possible**, however a **crossover-only EA does NOT WORK**. 
> This is because we cannot get new characteristics in future generations, we limit the characteristics to those that appear randomly in the first generation. 

We'll say that each of them (usually) perform a different purpose: 

**Exploration:**
**Crossover** is explorative, it makes big changes, going towards the center point between both parents, looking for the best areas in the search space. 

**Explotative:**
**Mutation** is exploitative as it creates small random changes, optimizing the solution (looking for the best of the best)

This means that we could adapt an algorithm so that it gives more importance to exploration at the beginning and once we find nice fitness solutions start giving more importance to mutation to optimize the problem. 


***
### Up
### Down
***
