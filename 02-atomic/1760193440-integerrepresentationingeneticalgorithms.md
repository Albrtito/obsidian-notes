---
aliases:
- integer representation in genetic algorithms
tags:
- ms
---
# integer representation in genetic algorithms
> [!NOTE] Intro: 
> When using integers in genetic algorithms we need to transform them from phenotype (an integer) to genotype (whatever the genome is). There are several methods to do so. 

## Bit representation
For algorithms such as [[1760115567-simplegeneticalgorithm|SGA]] the genotype is a bit string, this is **highly unrecommended** when working with integers (encoding into bit) but if we have to do so we'll use [[1760192042-graycode|gray code]] so that an small change in phenotype does not highly alter the genotype. 

## Encoding categorical values: 
It is easy to encode categories into integers but we'll always need to keep in mind the significance of them in the fitness function. 
## operators:
Which operators work with integers when encoded as integers?
- For **crossover(redistribution)**: [[1760191052-npointcrossover|n point crossover]] and [[1760191333-uniformcrossover|uniform crossover]] work
- **For mutation**: Bit flipping mutations work. It can either be done by giving it a more likely probability to move to similar values or by choosing a random choice. 

***
### Up
- [[1760115822-geneticalgorithm|genetic algorithm]]
### Down
***
