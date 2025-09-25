---
aliases:
  - Exercises - Logic - PRENEX AND SKOLEM
  - Logic - Submission - 7.1
tags:
  - logic
"References:": 
cssclasses:
---
# Submission 7: PRENEX

## 3.  Transform each formula of the following deduction into a PRENEX normal form:

**first formula:**
$$
\begin{gather}
\forall x \exists y (P(x,y)\lor \lnot Q(x,y)\rightarrow R(x,y))\\\\
\forall x \exists y (\lnot[P(x,y)\lor \lnot Q(x,y)]\lor R(x,y))\\\\
\boxed{\forall x \exists y ([\lnot P(x,y)\land  Q(x,y)]\lor R(x,y))}\\\\
\end{gather}

$$
**second formula:**
$$
\exists x\forall y(\exists yQ(x,y)\rightarrow R(x,y))
$$
$$
\exists x\forall y(\lnot \exists yQ(x,y)\lor R(x,y))
$$
Change y for u in the Q predicate so there is no problems between variables.
$$
\exists x\forall y(\forall u \lnot Q(x,u)\lor R(x,y))
$$
$$
\boxed{\exists x\forall y\forall u( \lnot Q(x,u)\lor R(x,y))}
$$

**third formula:**(already in PRENEX)
$$
\exists x \exists y R(x,y)
$$

## 5. Transform each formula of the following deduction into a PRENEX normal form:

**first formula:**
$$
\forall x \exists y(\lnot Es(x)\land Eu(x) \rightarrow \lnot S(y,x))
$$
Get rid of the conditional:
$$
\forall x\exists y (\lnot(\lnot Es(x)\land Eu(x))\lor \lnot S(y,x))
$$
Solve the negations: PRENEX 
$$
\boxed{\forall x\exists y (( Es(x)\lor \lnot Eu(x))\lor \lnot S(y,x))}
$$

**second formula:**
$$
\forall x ((\forall y S(y,x) \land \lnot \exists yEs(y))\rightarrow \lnot Eu(x))
$$
Get rid of the conditional:
$$
\forall x (\lnot(\forall y S(y,x) \land \lnot \exists yEs(y))\lor \lnot Eu(x))
$$
Solve the negations:
$$
\forall x ((\lnot\forall y S(y,x) \lor  \exists yEs(y))\lor \lnot Eu(x))
$$
Out with the quantifiers: **Remark:** One of the two existential quantifiers must be transformed into the variable u #duda(Where to do so)
$$
\boxed{\forall x \exists y \exists u ((\lnot  S(y,x) \lor  Es(u))\lor \lnot Eu(x))}
$$

 
## 8. Obtain the skolem normal form equivalent to the following formula.
 
$$
\forall x \exists y \exists z [(\lnot P(x,y)\land Q(x,z))\lor R(x,y,w)]
$$
Already in PRENEX

Transform to SKOLEM:

Bind free variables
$$
\exists w\forall x \exists y \exists z [(\lnot P(x,y)\land Q(x,z))\lor R(x,y,w)]
$$


Transform to the required formula type **clause (and) clause (and)..(and)..**
$$
\exists w\forall x \exists y \exists z [((R(x,y,w)\lor \lnot P(x,y)) \land ((R(x,y,w)\lor Q(x,z))]
$$
Remove existential quantifiers: SKOLEM
$$
\boxed{\forall x [((R(x,f(x),a)\lor \lnot P(x,f(x))) \land ((R(x,f(x),a)\lor Q(x,g(x)))]}
$$

## 9. Obtain the skolem normal form equivalent to the following formula: 

$$
\forall x \{\lnot P(x,a)\rightarrow \exists[ yP(y,g(x))\land \forall z (P(z,g(x)) \rightarrow P(y,z))]\}
$$
**PRENEX**
Delete all conditionals: 
$$
\forall x \{ P(x,a)\lor \exists y[ P(y,g(x))\land \forall z (\lnot P(z,g(x)) \lor P(y,z))]\}
$$
No negations to composite formulas 

Extract quantifiers to the beginning of the formula:
$$
\forall x \exists y \forall z\{ P(x,a)\lor [P(y,g(x))\land  (\lnot P(z,g(x)) \lor P(y,z))]\}
$$
Obtain the clause form:
$$
\forall x \exists y \forall z\{[P(x,a)\lor P(y,g(x))] \land [P(x,a)\lor ( \lnot P(z,g(x))\lor P(y,z) )]\}
$$

**SKOLEM**
Remove all existential quantifiers:
$$
\boxed{\forall x \forall z\{[P(x,a)\lor P(f(x),g(x))] \land [P(x,a)\lor ( \lnot P(z,g(x))\lor P(f(x),z) )]\}}
$$

## 10. Obtain the skolem normal form equivalent to the following formula:
$$
\forall x [(P(x)\rightarrow \lnot \forall y (Q(x,y)\rightarrow \exists zP(z))) \land \forall t(Q(x,y)\rightarrow R(t))]
$$
Remove conditionals → Free variables → Get required “clause” form → Remove existential quantifiers.
$$
\forall x\forall z \forall t[((\lnot P(x)\lor Q(x,f(x))\land (\lnot P(x) \lor \lnot P(z)) \land (\lnot Q(x,a)\land R(t))]
$$