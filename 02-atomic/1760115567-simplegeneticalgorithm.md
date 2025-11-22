---
aliases:
  - simple genetic algorithm
  - SGA
tags:
  - ml
---
# simple genetic algorithm
> [!NOTE] Intro: 
> Simple genetic algorithms are a type of genetic algorithm where: 
> - Representation: Binary strings
> - Recombinations: N-point or uniform
> - Mutation: Bitwise bit-fplipping with fixed probability
> - Parent selection: Fitnes-Proportionate
> - Survivor selection: All children replace parents
> - Speciality: Emphasis on crossover


> [!attention] Remarks:
> - Used in many **early** studies, nowadays only used for **benchmarking** new GAs or models. 
> - If encoding digits use [[1760192042-graycode|gray code]] as the one bit change for each integer keep it so small changes in the genotype cause small changes in the phenotype. It is not recomended to encode integers as bit but in this type of algorithm there is not really any other choice. 

> [!example] Dictionary:
> - **chromosome** -> The set of all attributes of an individual, here a binary string
>   > chromosome for some individual: 1001001010

## Reproduction cycle:
Each reproduction cycle follows the steps:
1. Select best (fittest) parents and make random pairs with them
   In order to select by fitness we'll use the following probabilty function:
   $$
P_{FPS}^{(i)} = \frac{f_{i}}{\sum^{m}_{j=1}f_{j}}
$$
	where:
	- Each individual fitnes $f_{i}$ gets divided by the sum of all fitnesses to obtain a proportional probability. 

2. For each pair:
	1. Apply crossover with proability $p_{c}$, otherwise copy parents. 
	2. For each offspring apply mutation (bit-flip) with probabilty $p_{m}$ (indepenent probablity for each attribute)
	   - The flipping range will vary between $\frac{1}{\text{population\_size}}$ and $\frac{1}{\text{chromosome\_lenght}}$ . In general in relation with the crossover must be lower. 
	The proabilities of both depend on what we want to do, look into [[1760191416-crossovervsmutation|crossover vs mutation]]
3. Replace the whole population with the resulting offspring. 


***
### Up
- [[1760115822-geneticalgorithm|genetic algorithm]]
### Down
- [[1759829263-encodingattributesinevolutionaryalgorithms|phenotype vs genotype]]
- [[1760116654-onepointcrossover|one point crossover]]
- [[1760191052-npointcrossover|n point crossover]]
- [[1760191333-uniformcrossover|uniform crossover]]
- [[1760192042-graycode|gray code]]
- [[1760191416-crossovervsmutation|crossover vs mutation]]
***
