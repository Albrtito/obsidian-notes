---
aliases:
- solving n queens with evolution
tags:
- ms
---
# solving n queens with evolution
> [!NOTE] Intro: 
> Given the basic [[1759830817-nqueensproblem|n queens problem]], how can we solve it using evolutionary algorihtms?

First of all we need to transform the genotype (chess board) into a phenotype. 
A good way of doing so appears after realizing that queens cannot be in the same column|row by definition. Then we can just represent each column as elements of a vector with value going from 0 to m.

The next thing is to decide on some fit function. What is a good 

Once we have chosen good parents, how can we do recombination? 
The first problem that appears is with the restrictions on positions. We cannot have two positions with the same value as they would be on the same row and that cannot be. 
- **mutation:** We'll change values inside the vector, swapping them. 
- **recombination:** We'll cut and crossfit. So cut one of the parents and crossfit each value with both parents values. 

#incomplete 
***
### Up
- [[1759827624-evolutionaryalgorithms|evolutionary algorithms]]
### Down
***
