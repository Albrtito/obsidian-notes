---
aliases:
  - evolutionary algorithms
  - EAs
tags:
  - ml
---
# evolutionary algorithms
> [!NOTE] Intro: 
> These algorithms are based on the same idea as evolution. 
> > "The fittest may survive"

This natural selection model uses the best individuals as seeds for the next generations, **recombining and mutating the descendants.** 
In order to know which individuals are the best we'll make them **compete for survival. **


> [!example] Dictionary:
> - **enviroment** -> Problem
> - **individual** -> Candidate solution, a single solution
> - **fitness** -> Quality of the solution. Determines the chance for seeding new solutions

## prop: 
- **Stochastic** -> Population-based algorithm, they create some number of individuals and play with them
- **fitness-based selection** -> They select based on the fitness of the individual
  We can visualize this for individuals with n traits inside an space of n+1 dimensions (where this +1 dimension is the fitness).
  Inside this space we would like to see that over time individuals change(mutate) their traits going towards the high fitness areas. 

## general scheme

1. **Initialise**
2. **Evaluate for termination**: Is the population good enough
   - Do we terminate -> HALT
   - Do we not terminate -> Keep going
1. **Select parents**: Select the parents for the next iteration
2. **Mutation**:  Create new agents for the next iteration
3. **Back to 2**

### initialization:
Usually random, importance on getting enough initial traits so that they can evolve from there.
Can include existing solutions or use problem-specifi heuristics to seed the population. Which means that we can start from an alrready good point by using other methods pre applying the evolutionary algorithm. 

### fitness evaluation: 
What are the requirements for the population? We create an objective function or quality function to represent this so that we can compare based on one single real value (fitness). 
We'll usually look for the fittest (max fitness)

Generally this algorithms will have three phases related with fitnes: 
1. Initial phase: All random
2. Mid phase: Poulation starts to move towards good fitness points
3. Late phase: Population concentrated on high hills
Because we can stop this fitness improvement at any time we'll call this an anytime algorithm. If we stop it we'll have a solution, even if it is a subobtimal one. 

Another thing about the fitness improvement is that it'll improve very little if we wait twice as much. (a great improvement followed by a very slow improvement)
### parent selection:
The selection is usually probabilistic. So this means that we'll probably take as parents those with higher fitness. However we can also take some that are not that fit (based on that probability). Creating variation within the child. 

### variation operators:
How do we create this new candidates (the children). We have two operators: 
1. Recombination/Crossover
2. Mutation: 

> [!attention] Remark:
> Nowadays most EAs use both operators. Although one or the other can be exclusive. 

#### recombination:
Merges information from the parents creating new offspring based on it. The choice of info is stochastic. 
This does not mean that all offspring will be better just by having good parents, most of them wont be actually better. (but some will, so yay)

#### mutation
Create new traits that the parents did not have. It introduces diversity which is really important so that there is still randomness. 
We say it is **unary** when it only alters one trait. 

### Survivor selection: 
Which individuals will survive the next round? We can decide this based on different parameters such as a max number of individuals or what is the minimum fitness that one individual must have to survive.
If an individual does not cut it, then it does not go into the next round. 

### termination: 
Different ways, but generally basically asking, are we good enough?

- **fitness** : Reach target fitness
- **max generation**: Stop at some number of iterations
- **min level of diversity**: All agents are similar, lets stop
- **generations without fitness improvement**: Individuals are not getting better
***
### Up
### Down
- [[1759829263-encodingattributesinevolutionaryalgorithms|encoding attributes in evolutionary algorithms]]
***
