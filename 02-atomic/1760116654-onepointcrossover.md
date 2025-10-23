---
aliases:
- one point crossover
tags:
- ms
---
# one point crossover
> [!NOTE] Intro: 
> Specific case of the [[1760191052-npointcrossover|n point crossover]]
> The one point crossover is a technique used in evolutionary algorithms to recombine the properties of two parents in order to create a new child. It works by choosing one point (random) for one of the parents. The new child has properties of parent 1 until that point, then properties of parent 2. 

This type of crossover is usually done with a high probability (0.6,0.9) as parents usually are high fitness. 
#duda If we are not doing the crossover then the child is getting all the attributes from one of the parents?

> i.e:
> parent 1 -> 000000
> parent 2 -> 111111
> 
> crossover at 2
> child 1 -> 001111
> child 2 -> 110000


> [!bug] Problems
> There are hoewever some problems with this operator: 
> 1. There is a positional bias, the attributes that are together will usually stay together. 
> 2. The first and last properties cannot ever be heredadas at the same time.

A solution would be to apply an [[1760191052-npointcrossover|n point crossover]] or [[1760191333-uniformcrossover|uniform crossover]]. 

***
### Up
- [[1760191052-npointcrossover|n point crossover]]
### Down
- [[1760191333-uniformcrossover|uniform crossover]]
***
