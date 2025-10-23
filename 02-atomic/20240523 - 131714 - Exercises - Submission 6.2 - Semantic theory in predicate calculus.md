---
aliases:
  - Exercises - Submission 6.2 - Semantic theory in predicate calculus
  - Exercises - Semantic theory in predicate calculus
tags:
  - logic
"References:": 
cssclasses:
---
# Exercises - Semantic theory in predicate calculus: 

## 2: Evaluation of a formula given **a domain and definition of the predicates**: With truth table

## 3: Given a domain D = {a,b}: With truth table
![[Screenshot 2024-05-23 at 13.53.07.png]]
The formula is true for every interpretation. **THEN:**
+ It is semantically valid in the domain. However it is only valid in **this domain**

## 4: Given a domain D = {a} with truth table
Verify the formula: 
$$
\forall x (P(x) \lor \forall x Q(x)) \rightarrow \forall x(P(x) \lor Q(x))
$$
![[Screenshot 2024-05-23 at 14.04.05.png]]
The formula is true for all interpretations. Then it is valid in domain D.

## 5. Verify formula with counterexample
$$
\forall x(P(x) \lor Q(x)) \rightarrow (\forall x P(x) \lor \forall x Q(x))
$$
In order to find a counter example (False interpretation) we look for: 
+ $\forall x(P(x) \lor Q(x))$ : true
	+ 
+ $(\forall x P(x) \lor \forall x Q(x))$ : false
	+ $\forall x P(x)$: FALSE
	+ $\forall x Q(x)$ : FALSE

We can try to find a counterexample in domain D = {a} however this counterexample is not possible: 
![[Screenshot 2024-05-23 at 14.22.58.png]]
+ See that we cannot fix P(x) ∨ Q(x)

However in a domain with two elements  D = {a,b} we can get a counterexample: 
![[Screenshot 2024-05-23 at 14.23.57.png]]

## 6: Verify the formula with counterexample: 
$$
\exists x (P(x) \land Q(x)) \rightarrow (P(y)\lor Q(y))
$$
The conditional needs to be false, then: 
$(P(y)\lor Q(y))$ is False while $\exists x (P(x) \land Q(x))$ is true meaning:  
+ P(y) is false
+ Q(y) is false

If we look in a domain D= {a} with free variable y = a we need for Q(y) to equal 0 while Q(a) equals 1. This is impossible. 
![[Screenshot 2024-05-23 at 17.36.37.png]]

However in a domain of two elements we can surely find a counterexample: 
![[Screenshot 2024-05-23 at 17.36.49.png]]

## 7: Verify the formula with counterexample
$$
\lnot \forall x A(x) \land \lnot (\exists x \lnot A (x))
$$
In order for the formula to be false we need one terms to be false. To simplify the quantifiers we do the following: 
$$
\exists x \lnot A(x) \land (\forall x  A (x))
$$
In a one element domain we get: 
D = {a}
![[Screenshot 2024-05-24 at 02.06.58.png]]
Proving a counterexample for D

## 8: Verify the formula with counterexample: 
$$
(\exists x A(x) \rightarrow \exists x B(x)) \rightarrow \forall x (A(x)\rightarrow B(x))
$$
For this formula, we prove a counterexample by proving that the conditional is false, then: 
+ $(\exists x A(x) \rightarrow \exists x B(x))$ : **TRUE**
+ $\forall x (A(x)\rightarrow B(x))$ : **FALSE**
There are no free variables, for a domain for D = {a} we have:
![[Screenshot 2024-05-24 at 02.15.19.png]]
Which means that for a one element domain there is no possible counterexample: 
For a domain D = {a,b}
![[Screenshot 2024-05-24 at 02.18.58.png]]
We find one counterexample hence the formula is not valid

## 9: Verify the formula with counterexample: 
$$
(\exists xA(x)\land \exists x B(x)) \rightarrow \exists x (A(x)\land B(x))
$$
For the formula to be false, then find a counterexample, the conditional must be false. 
+ $\exists x (A(x)\land B(x))$ : **FALSE**
+ $(\exists xA(x)\land \exists x B(x))$: **TRUE**

There are no free variables. 
For a domain D = {a} we find that: There is no counterexample: ![[Screenshot 2024-05-24 at 02.27.37.png]]

However for D = {a,b} we can find a counterexample and therefor the formula is not valid
![[Screenshot 2024-05-24 at 02.27.14.png]]
## 10. Verify the formula with counterexample: 
$$
\forall x\exists y P(x,y) \rightarrow \exists y \forall x P(x,y)
$$
It is a conditional, then for it o be false we need: 
+ $\exists y \forall x P(x,y)$ : **FALSE**
+ $\forall x\exists y P(x,y)$ : **TRUE**

For a domain of D = {a} we cannot find a counterexample: 
![[Screenshot 2024-05-24 at 02.39.55.png]]
However for domain D ={a,b} we find the following counterexample: 
![[Screenshot 2024-05-24 at 02.40.28.png]]
Then the formula is not valid.

## 11. Verify the formula with refutation: 

**Remember:** Refutation is obtained by uniting the premises and the conclusion with an and operator and negating the conclusion. 
$$
\exists x (P(x) \land Q(x)) \Rightarrow \exists x \lnot Q(x) \lor \forall x \lnot P(x)
$$
We obtain the following formula: 
$$
\exists x (P(x) \land Q(x)) \land \lnot[\exists x \lnot Q(x) \lor \forall x \lnot P(x)]
$$
We know that for this formula to be false, either of both tenses have to be false (and operator), we look for a counterexample in D = {a} and find one counterexample: 
![[Screenshot 2024-05-24 at 02.52.12.png]]
Then the formula is not valid. 

## 12. Verify the formula with counterexample: 

## 13. Verify the formula with counterexample: 

## 14. Verify the formula with counterexample: 

## 15. Verify the deduction using counterexample. 
