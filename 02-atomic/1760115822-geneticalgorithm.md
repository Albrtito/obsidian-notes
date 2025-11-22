---
aliases:
  - genetic algorithm
  - GA
tags:
  - ml
---
# genetic algorithm
> [!NOTE] Intro: 
> Genetic algorithms are a type of [[1759827624-evolutionaryalgorithms|evolutionary algorithms]] that try to simulate the process of natural selection to obtain a solution to an optimization problem.


> [!example] Dictionary:
> - **chromosome** -> The set of attributes. If encoded then in genotype, if not encoded in phenotype
> - **allele** -> One value of the chromosome

#incomplete Need to finish the steps and attributes of each step. Also mejorar la definición básica en evol algorithms para tener un esquema básico desde el que organizar cosas. 
## parent selection
In order to select parents we'll do it based on:
$$
P_{FPS}^{(i)} = \frac{f_{i}}{\sum^{m}_{j=1}f_{j}}
$$
where:
- Each individual fitnes $f_{i}$ gets divided by the sum of all fitnesses to obtain a proportional probability. 

Then we can choose given their probabilities using either a **one-arm roulette wheel algorithm or a n-arm roulette wheel algorithm**

## population models: 
Used for survivor selection, there are several models based on how many children are generated and the number of parents that die. 
- **Generational model(GGA)**: All individuals die at the end of the cycle, their children survive 
- **Steady-State models(SSGA)**: Only one child per generation. One member of population is replaced
These are the two extreme cases. We talk about the quantity of  children generated as the **generation gap** (1 for GGA, 1/pop_size for SSGA). 
$$
\frac{\text{generated\_childs}}{\text{parents}}
$$

***
### Up
- [[1759827624-evolutionaryalgorithms|evolutionary algorithms]]
### Down
- [[1760115567-simplegeneticalgorithm|simple genetic algorithm]]
- [[1760193440-integerrepresentationingeneticalgorithms|integer representation in genetic algorithms]]
- [[1760194075-realvaluerepresentationingeneticalgorithms|real value representation in genetic algorithms]]
- [[1760195591-permutationrepresentationingeneticalgorithms|permutation representation in genetic algorithms]]
***
