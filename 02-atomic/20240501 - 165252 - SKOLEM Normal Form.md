---
aliases:
  - SKOLEM Normal form
  - SNF
tags:
  - logic
"References:": 
cssclasses: 
sr-due: 2024-06-17
sr-interval: 36
sr-ease: 270
---
# SKOLEM Normal Form (SKN)
SKOLEM normal form is a formula structure key for several automatic proof procedures (whatever that is)

> [!NOTE] Definition
> Features: If a formula is in SKN then:
> + Quantifiers must be at the head of the formula
> + Only universal quantifiers are allowed
> + The matrix of the formula is a conjunction of clauses 
> 	
> 	**Namely**: 
> 	The matrix formula is composed by clauses that only contain the $\land$ connective cunjucted between them: $\forall ... \forall ... [(C_1)\land(C_2)\land…\land (C_n)]$
> 	**Remark:**
> 	$C_n$: Is a clause this means that is composed by literals that are connected though the or connective.
> 	$$
> 	 C_n = L_1 \lor L_2 \lor L_3 ...\lor L_n
> 	 $$
> 	**Where:** Each literal **is atomic**
> 	


## Procedure to obtain SKOLEM NORMAL FORM (SNF)
Given any formula A, it is possible to derive the SNF using:
1. Get the [PRENEX Normal form](20240501%20-%20161016%20-%20PRENEX%20Normal%20form.md) of A

for example: The PRENEX form: 
$$
\forall x \exists y \exists z [(\lnot P(x,y)\land Q(x,z))\lor R(x,y,w)]
$$
2. Bind free variables, adding existencial quantifiers to **the head** (the first of all the quantifiers) of the PNF(existencial closure). 

Keeping with the example:
Here we bind w as it was the only free variable. We create an existential quantifier and place it **at the head**
$$
\exists w\forall x \exists y \exists z [(\lnot P(x,y)\land Q(x,z))\lor R(x,y,w)]
$$

3. Transform the matrix of the resulting formula using the equivalences: 
	+ **Remember** that because we have already transformed into the PNF there are no $\rightarrow$ or composite $\lnot$ connectives.
	+ **Remark:** These two equivalences are placed under Replacement Theorems/conjunction/2.3. The first one is the main one used. The idea is: **IF A or (B and C) THEN: (A or B) and (A or C)**
$$
	\vdash A\lor(B\land C)\leftrightarrow(A\lor B)\land (A\lor C)
$$
$$
\vdash(A\land B)\lor(A\land C)\leftrightarrow A\land(B\lor C)
$$
For our example: We use the formula as it is: 
$$
\exists w\forall x \exists y \exists z [((R(x,y,w)\lor \lnot P(x,y)) \land ((R(x,y,w)\lor Q(x,z))]
$$

4. Remove all existential quantifiers, to do so: 
	1. Start processing existential quantifiers from left to right
	2. If $\exists$ as no $\forall$ on the left. Replace the variables with constants:
	
	Example of how to do so, the variable x is replaced with a:
	$$
	\exists x \forall y \forall x(P(x,y)\lor Q(x,z)) \Rightarrow \forall y \forall z(a,y) \lor Q(a,z))
	$$
	3. If $\exists$ has any $\forall$ on the left, replace the variable with a function depending on as many arguments as $\forall$’s on the left, using those very same variables as arguments.

	The variable x is replaced with f(y,z) as the existential has the generalisation of y and z before itself.

$$
\forall y\forall z\exists x(P(x,y)) \lor Q(x,z)) \Rightarrow \forall y \forall z (P(f(y,z), y ) \lor Q(f(y,z),z))
$$
+ See that the variable x has been substituted by the function f(y,z)
+ If there where more existential quantifiers, **use different functions.** 
   
  
	In the example: Our final solution for our example would be: 
	$$
	 \boxed{\forall x [((R(x,f(x),a)\lor \lnot P(x,f(x))) \land ((R(x,f(x),a)\lor Q(x,g(x)))]}
	 $$
	
