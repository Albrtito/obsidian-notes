---
aliases:
  - PRENEX Normal form
  - PNF
tags:
  - logic
"References:": 
cssclasses: 
sr-due: 2024-06-02
sr-interval: 25
sr-ease: 270
---
# PRENEX Normal Form (PNF)
PRENEX normal form is a formula structure. For the logic course it is mainly used to obtain the SKOLEM Normal Form.
The PRENEX formula can **always** be obtained.

> [!NOTE] Definition
> A PRENEX normal form must: 
> + Only have connectives of type $\lnot, \land$
> + All negations must be atomic (no compound negations)
> 	This is an atomic negation: 
> 	$$
> 	\lnot A
> 	$$
> 	This is a compound negation:
> 	$$
> 	\lnot (A \land B)
> 	$$
> + All quantifiers must be at the beginning of the formula
> 

## Method to obtain PRENEX NORMAL FORM (PNF):
Given a formula A, we derive the PNF with the following steps:
1. Eliminate connectives different to $\land, \lnot, \lor$
	+ This is done using the formula 9. Implication with respect to disjunction of the [Theorems and rules](../00.References/Logic_Resource_Theorems%20and%20Derived%20Rules%20Combined.pdf). 
	The theorem is:
	
	Considering:
	$$
	\begin{aligned}
	& H(\mathrm{~A} \rightarrow \mathrm{B}) \leftrightarrow(\sim \mathrm{A} \vee \mathrm{B}) \\
	& -(\mathrm{A} \rightarrow \mathrm{B}) \leftrightarrow \sim(\mathrm{A} \sim \sim \mathrm{B})
	\end{aligned}
	$$
	
	If the formula A contains ...R $\rightarrow S$...
	$$
	\begin{aligned}
	& \vdash \ldots(\mathrm{R} \rightarrow \mathrm{S}) \ldots \leftrightarrow \ldots \sim(\mathrm{R} \wedge \sim \mathrm{S}) \ldots \\
	&
	\end{aligned}
	$$
2. Eliminate negation when its compound: Use Morgan and Equivalence theorem.
	+ For predicate logic: **Remember:** 
$$
	\lnot \forall A \Rightarrow \exists \lnot A
$$
$$
\lnot \exists A \Rightarrow \forall \lnot A
$$
3. Move all quantifiers to the beginning.
	+ **Problem:** There is two different quantifiers for the same variable such as: 
$$
	\vdash ... A(x)\lor \forall xP(x) 
$$
The solution is to give a new name to the variable x. 

$$
	\vdash ... A(x)\lor \forall yP(y) 
$$
**Remark:** This is important to do for the SKOLEM Normal form. 

Once we have solve this problem just take all quantifiers out (**Remark:** A quantifier cannot be negated if we want to take it out.)