---
aliases:
- real value representation in genetic algorithms
tags:
- ms
---
# real value representation in genetic algorithms
> [!NOTE] Intro: 
> How can we transform real values in the phenotype to the genotype of the genetic algorithm. 

First we'll need to think about **when to use real values in genetic algorithms.** 
If we have an analytical problem $\hat{y}=\theta_{1}x_{1}+\dots+\theta_{n}x_{n}$ then we dont usually want to use a genetic algorithm. 
#duda When is that we use them then?

## operators:
Which operators work with real values?
- **recombination**: Both **n-point and uniform crossover** can be used. We can also perform **arithmetic recombination**
- **mutation:** We can perform **uniform mutation** between an upper and lower bound, selecting with equal probability any value in the range. If we perform **non-uniform mutation** then there is no equal probability for all values in the range but some probability distribution. 

***
### Up
### Down
- [[1760191052-npointcrossover|n point crossover]]
- [[1760191333-uniformcrossover|uniform crossover]]
- [[1760194325-arithmeticrecombination|arithmetic recombination]]
***
