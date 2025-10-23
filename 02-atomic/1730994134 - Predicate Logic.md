---
Date: 2024-03-12
tags:
  - logic
"References:": 
sr-due: 2024-06-02
sr-interval: 61
sr-ease: 292
aliases:
  - Predicate Calculus
  - Predicate logic
---

# Predicate logic: 
[[1730994133 - Propositional logic|Propositional logic]] is really useful if there are only minimal unit (atomic) propositions. However reality does not work that way. In order to detail reality in a more accurate way we use predicate logic. 

Predicate logic divides between **what is said: PREDICATE** and **about whom is said: SUBJECT OR TERM** . This way a predicate can be associated to one or more subjects.

As with any other logical system we shall define the **Alphabet**, **Axioms** and **Valid formulas(SCF)** of the system. 
## Alphabet and SCF: 
+ For **terms and subjects:** Small letters are used. If the subject is a constant(an specific being(denoted f.e. as a personal name)) the letters **a,b,c...** are used. If the subject is a variable inside a domain it is represented by **x,y,z...**
+ For **predicates**: Caps are used, starting with the P. **P, Q,R...**
### Predicates:
Predicates are assigned over some subjects or terms. Then a predicate P can be assigned to a series of terms $x_i$ .  
$$
 P(x_1, x_2,x_3,x_4...)
$$
A predicate can have any number n of arguments. The number n is called **arity**. The arity of any argument P can be from 0 to n $\in R$

Based on their arity predicates can be classified as: 
+ **Constant predicates:** Arity = 0. Represent atomic proposition
+ **Monadic predicates:** Arity = 1. Represent properties of an object
+ **Poliadic predicates:** Arity > 1. Represent relationships between objects.
### Quantifiers:
Quantifiers are used to assign a set of terms in the domain of a variable to the predicate. 
	f.e. Maybe all of the domain of variable x is affected by the predicate P, but it could be that only part of the domain was affected. 
In order to symbolise that we use the universal and the existential quantifier. 
**Universal quantifier:** All of the elements of the domain x 
$$
\forall x
$$
**Existential quantifier:** At least one element of the domain x
$$
\exists x
$$
A variable affected by a quantifier is bounded.
	f.e. **Example with some predicate Sit(x,y,z) where x is sitting between y and z:** If all the students are sitting between Manuela and José: 
$$
	\forall x P(x,b,c)
$$
	if at least one student is sitting between Manuela and José
$$
	\exists x P(x,b,c)
$$
### Syntactically correct formulas: 
![[Screenshot 2024-04-09 at 12.58.02.png]]
### Connectives
Same connectives as in [[1730994133 - Propositional logic|Propositional logic]] are defined. Their hierarchy is also maintained.

## Axioms: 
![[Screenshot 2024-04-09 at 12.56.05.png]]

---

# Solving:
+ [Construction of formulas](Construction%20of%20formulas.md)
+ [Negation with existential vs universal](Negation%20with%20existential%20vs%20universal.md)
## Proof theory in predicarte calculus:
As in propositional calculus, there is a way of using the axioms and rules in order to solve and validate logic expressions. This “way” is defined by **proof theory** and it’s application to predicate calculus. 

See the following note for the whole theory explanation: [ Proof theory in predicate calculus](20240409%20-%20121336%20-Proof%20Theory%20in%20Predicate%20Calculus.md)

## Semantic theory:
Semantic theory defines another method for deducing whether a formula is valid or not by the usage of truth tables and counterexamples. 
See the following for the whole theory explanation: 
[Semantic theory in Predicates](20240411%20-%20110836%20-Semantic%20theory%20in%20Predicates.md)


