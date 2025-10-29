---
aliases:
- permutation representation in genetic algorithms
tags:
- ms
---
# permutation representation in genetic algorithms
> [!NOTE] Intro: 
> When representing permutations in the genome we'll have the problem that no integer can be repeated twice. We have a list of integers that can change places but cannot be repeated within the list. 

## operations:

- **Recombination:**
	We'll find that **crossover operations** do not work as they do not take into account the repeating constraint. Therefore we'll have to alter this operator in the following way: 
	
	Given two parents and one cutoff point we'll: 
	1. Copy one of the  parts of the first parent into the child (at random)
	2. Starting in the cutoff point, copy the numbers that are not in the already copied part into the positions where the second parent has them. If there is no position for that number based on the second parent ordering then we put one of the missing numbers randomly. 
	By doing this in reverse we obtain the second child
	
	> i.e: We take the 3,4,5 th positions. Then create one child with those positions from the first parent, another one form the second one. 
	> The other positions are filled with the remainging numbers in the other parent order. 
	> ![[1760195591-permutationrepresentationingeneticalgorithmsj.png|center|200]]
	> 
- **Mutation:** 
  We'll find a problem like with recombination, we cannot change randomly. The solution is: 
	- **Insert allele**: Take an allele, move it to a new position, move the whole vector to accommodate. 
	- **Flip alleles:** Take two attributes and flip them
	- **Inverse**: Take a chunk of it all, inverse it 
	- **Random recombination**: Take some of them, change their places randomly. (same as flipping n times between some positions?)

***
### Up
- [[1760115822-geneticalgorithm|genetic algorithm]]
- [[20240515 - 010953 - Permutations|Permutations]]
### Down
***
