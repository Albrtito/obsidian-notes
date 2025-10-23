---
aliases:
  - Method - Partial Fractions
  - Partial Fractions
tags:
  - calc
  - diffcalc
---
# Partial fractions:
The partial fraction method is used to **decompose**fractions into **sums of simpler** rational functions. The objective is to rewrite expressions such as: 
$$
\frac{3x}{x^2 -x -2}
$$
by partitioning them into smaller fractions based on the decomposition of the denominator by it’s rots. For the previous example we would obtain something such as: 
$$
\frac{1}{x +1} + \frac{2}{x -2}
$$
## Method:

**CONDITION:**
This method is used for fractions such as: 
$$
\frac{P(x)}{Q(x)}
$$
There are two variations of the method:

There’ll be two different possibilities whether: 
1.  $\deg(P(x)) < \deg(Q(x))$ 
2. $\deg(P(x)) > \deg(Q(x))$ 

### For deg(P(x)) < deg(Q(x))
Perform [[20240620 - 172412 - Method - Polynomial long division|Polynomial long division]] in order to restructure the polynomic fraction.

### For deg(P(x)) > deg(Q(x))

1. Rationalise Q(x) into it’s factors. 
2. Write an equality such as: 
$$
\frac{P(x)}{Q(x)} = \frac{A_0}{F_1(x)} +\frac{A_1}{F_2(x)} + ... + \frac{A_n}{F_n(x)} 
$$
Where $F_i(x)$ are the factors of Q(x) after rationalisation

**Remarks:**

+ If a factor is repeated n times then the partial fractions need to be: 
$$
\frac{P(x)}{Q(x)} = \frac{A_0}{F_1(x)} +\frac{A_1}{F_1(x)^2} + ... + \frac{A_n}{F_1(x)^n} + \frac{A_{n+1}}{F_2(x)}
$$
See that the factor $F_1(x)$ is repeated n times and therefore there are n fractions representing it, with increasing values for it’s degree.

+ If a factor is not simple but has degree 2 or more: 
This example is for a degree 2: For greater degrees just follow the pattern.
$$
\frac{P(x)}{Q(x)} = \frac{A_0x + A_1}{F_1(x)} +\frac{A_2}{F_2(x)} + ... + \frac{A_n}{F_n(x)} 
$$
### Down
- [[calc_resource_partialFractions.pdf|Explicación del método con ejemplos y ejercicios de práctica con soluciones, se entiende guay]]
### Up