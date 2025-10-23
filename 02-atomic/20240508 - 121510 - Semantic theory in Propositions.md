---
aliases:
  - Semantic theory in propositions
tags:
  - logic
"References:": 
cssclasses: 
sr-due: 2024-06-19
sr-interval: 21
sr-ease: 250
---
# Semantic theory in propositional calculus.

This note presents information about how the semantic theory can be applied specifically to [20240523 - 122919 - Propositional logic](20240523%20-%20122919%20-%20Propositional%20logic.md). There is not really much to say besides what was explained in semantic theory. Here there is a more step by step solving guide.

## Solving: 
In propositional calculus we’ll apply semantic theory to obtain whether a formula or a deduction is valid. 

### Formulas: 
For formulas we know: 
1. A formula is valid if it is a tautology
2. Finding a tautology means there is no possible counterexample
	1. A counterexample is a false interpretation (a 0 in the truth table or a possible counterexample)
3. We can use booth truth tables and counterexamples, we should obtain the same result and coherent in both cases. 
### Deductions: 
Deductions can be evaluated as deductions or as formulas (personal recommendation, do it as formulas and then is just the same always). 

**As deduction:** Find there is no counterexample. Premises positive conclusion negative
**As formula:** Either apply deduction theorem and use the formula steps or transform the formula to: 
$$
p_1 \land p_2\land ...\land p_n \land \lnot q
$$
+ The deduction is correct if this formula is **unsatisfiable**