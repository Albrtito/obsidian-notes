---
aliases:
  - Resolution proof method
tags:
  - logic
"References:": 
cssclasses: 
sr-due: 2024-05-02
sr-interval: 1
sr-ease: 230
---
# Proof method: Resolution

Resolution is an automated proof method used to **test whether a deductive structure is correct studying the validity of a formula**. The algorithm may not finish, then it is said that it is undecidable.
+ Used in formal program verification

## Procedure
Test whether a deduction: 
$$
p_1,p_2,...,p_n \Rightarrow q
$$
is correct by analysing if the formula: 
$$
F = p_1 \land p_2\land ...\land p_n\land \lnot q
$$
is unsatisfiable. 

(finding a contradiction)
**Formula unsatisfiable $\rightarrow$ Correct deduction**

+ We can choose a set of Skolem functions f so that the SNF is satisfiable or unsatisfiable in the same circumstances as the original formula. 
+ If contradictions can be derived from F, then the formula is unsatisfiable. 

**Then:** In order to use the method we must: 
1. Derive the corresponding SNF for the formula (F)
2. Try to get an empty clause by repeated use of the resolution rule: $(L\lor A, \lnot L\lor B \Rightarrow A\lor B)$ to obtain new clauses called resolvents. 
	1. In order to obtain resolvents it might be necessary to substitute variables with: 
		**Constants:**
		**Variables:** This is the way to go
		**Functions:**
		+ Variables cannot be replaced with functions that have those same variables as arguments
		+ If the same variable comes up in different clauses, despite of having the same name, they are different and they can be replaced with different terms
		+ Every clause can be used as many times as necessary, using as many different replacements as necessary
		+ Replacements affect the complete clause. Not specific predicates within a clause.

3. Getting an empty clause implies the existence of a contradiction. This means an unsatisfiable formula and therefore **correct deduction**
4. If after exploring all the potential combinations we cannot get a contradiction. then we can conclude that F is satisfiable (the deduction is not correct)
5. If the algorithm does not finish we cannot be sure that we have checked all possibilities, cannot conclude anything

1. Join together all the premises and conclusion negated.
2. Obtain the PRENEX equivalent: [PRENEX Normal form](20240501%20-%20161016%20-%20PRENEX%20Normal%20form.md)
3. Obtain SKOLEM equivalent: [SKOLEM Normal form](20240501%20-%20165252%20-%20SKOLEM%20Normal%20Form.md)
4. Try to get an empty clause with variable substitution.
