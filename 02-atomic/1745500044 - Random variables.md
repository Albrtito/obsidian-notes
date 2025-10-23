---
aliases:
  - Random variables
tags:
  - ai
References: 
cssclasses:
---
# Random variables

> [!NOTE] Intro: 
> In oposed to [[20240523 - 122919 - Propositional logic|Propositional logic]] where a variable can have either T or F values and a **truth assignment** is the assignment of values to those variables, [[1745499861 - Probabilities|Probabilities]] use an aproach where **one variable can have several values, contained inside the domain of that variable** ($\Omega$)
> Instead of having some associated value to the variable there is a **probability associated to each value that the variable can have**.

> f.e: $X \in \{1,2,3,4,\}$, with probabilities $\{0.2,0.3,0.1,0.4\}$

+ These probabilies define a **probability distribution**

> [!exercise] Dictionary: 
> +  **sample space: ($\Omega$)** The domain of a random variable
> + **atomic event: (e)** A possible situation of the variable: X = 3
> + **probability distribution:** Function $P(e)$ that assigns a number to each $e\in \omega$
> 	+ Usually represented as a vector
> + 

## Probabilty distribution:
The probability distribution is given by some function $P(3): \forall e \in \Omega$. 
+ If this function is not defined and the variables are three, independent, then the probability of the event that combines all three variables will be obtained by knowing all the possible combinations of these three variables, or in other words, a [[20240515 - 010953 - Permutations|Permutations]]
+ Another important thing is to know whether the variables are [[1745504803 - Probabilistic variable independence|Probabilistic independence]] or not. If they are the **size of the probabilistic distribution can be drastically reduced**

## Conditional distribution:

***