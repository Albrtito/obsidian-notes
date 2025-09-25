---
Date: 2024-03-19
tags:
  - calc
"References:": 
sr-due: 2024-07-07
sr-interval: 75
sr-ease: 270
---
### Definition
Convergence is the answer for the question: **What value does $a_n$ have when n = ...(any value you want to think of)?** Sometimes answering this question is really easy. However in most cases this value you where thinking of won't be an easy real number but infinite or minus infinite. There's your problem

We say(informal) that a sequence **converges to** (or tends to) a real number a for a given value of n. When if approaching that number n the series gets closer and closer to a. 

Before explaining how to actually compute and understand the convergence, lets state **what is it that we want to find when being asked if a sequence is convergent?** 
+ If we find convergence in a sequence we'll give as a solution that **the sequence converges to a when approaching n**
+ However if we can **prove that the sequence does not converge when approaching n** we'll say that **the sequence diverges when approaching n**
+ With infinite, we'll usually leave out the "when approaching n" part and just say: **The sequence converges** or **The sequence diverges**

### Representation and computation with limits
Convergence can be represented in several ways. 
+ Usually we represent it and compute it with [Definition - Limits](Definition%20-%20Limits.md). 
	$$
	a = lim_{n\rightarrow \inf} a_n
	$$
	This means that when computing the term such as n = infinite in  the sequence $a_n$ , that term is going to be a. 

+ Can also be represented with the following notation
	$$
	a_n \rightarrow_{n\rightarrow \inf} a
	$$
	The same meaning as the previous one is applied. 

**Remark and example:**
	In most cases we'll be interested in what happens when n tends to infinite. However this idea of convergence can be applied to any value of n. If we take for example a sequence: 
	$$
	s_1 = ({1\over n}_{n\in N}) = \{1, 1/2, 1/3, 1/4...\}
	$$
	Ask: What happens if n = 100? 
	This is easy, we could use the limit notation but the answer is straightforward: 
	$$
	\begin{align}
	a_{100} = {1\over 100} \\lim_{n\rightarrow 100} {1\over n} = 1/100
	\end{align}
	$$
	However we won't usually do that, we would like to know what happens if n tends to infinite. For this we'l use limit notation
	$$
	
	 lim_{n\rightarrow inf} {1\over n} = a
	
		
	$$
	Then based on the properties of limits we'll be able to say: $a = 0$

**In order to compute wether a sequence converges or diverges we'll use limits**  
#### Properly defining limits: 
![Definition - Limits](Definition%20-%20Limits.md)