---
aliases:
  - Exercises - Logic - Resolution
  - Logic - Submission - 7.2
tags: []
"References:": 
cssclasses:
---
# Exercises - Logic - Resolution: 

## 1. Verify correct deduction by resolution: 

$$
\forall x  \exists y P(x,y) \Rightarrow  \exists y \forall x P(x,y)
$$
1. Turn the formula into resolution form:
$$
\forall x  \exists y P(x,y) \land \lnot[  \exists y \forall x P(x,y)]
$$
2. Get the PRENEX equiv: 

**DELETE COMPOUND NEGATIONS:**
$$
\forall x \exists y P(x,y) \land \forall y \exists x \lnot P(x,y)
$$

**TAKE OUT THE QUANTIFIERS:**
$$
\forall x \exists y \forall v\exists u(  P(x,y) \land  \lnot P(u,v))
$$

3. Get the SKOLEM equiv: 

**ONLY UNIVERSAL QUANTIFIERS:**
+ y → f(x)
+ u → g(v, x)

$$
\forall x  \forall v(  P(x,f(x)) \land  \lnot P(g(v,x),v))
$$
**OBTAIN A CLAUSE FORM:**
Or connectives together, divided by and connectives. 

Already in a clause form: 

C1: $P(x,f(x))$
C2: $\lnot P(g(v,x),v)$

No substitutions would lead to an empty clause. The **deduction is not correct.**

## 2. Verify correct deduction using resolution:
The premises are given one after the other, remember that the resolution method says: 
$$
p_1 \land p_2 \land ...\land p_n \land \lnot q
$$
**Then**: 

Premises:
$$
\begin{gather}
& \exists x \forall y(A(x, y) \rightarrow B(y, x) \vee C(y)) \\
& \forall x \forall y(D(x, y) \rightarrow \sim C(x)) \\
& D(a, b) \wedge \forall x \forall y A(x, y)
\end{gather}\\ 
$$
Conclusion:
$$
\exists x B(a, x)
$$
1. Formula into resolution form: 
$$
\begin{gather}
\exists x \forall y(A(x, y) \rightarrow B(y, x) \vee C(y)) \\
 \land \\
 \forall x \forall y(D(x, y) \rightarrow \sim C(x))
 \\ \land \\
 D(a, b) \wedge \forall x \forall y A(x, y)
 \\ \land \\
 \lnot [\exists x B(a, x)]
\end{gather}
$$
2. Transform into PRENEX: 

**DELETE COMPOUND NEGATIONS AND CONDITIONALS**
+ Use interdefinitions for the first two premises.
+ Same for conclusion 
$$
\begin{gather}
\exists x \forall y( \lnot A(x, y) \lor (B(y, x) \lor C(y))) \\
 \land \\
 \forall x \forall y(\lnot D(x, y) \lor \sim C(x))
 \\ \land \\
 D(a, b) \wedge \forall x \forall y A(x, y)
 \\ \land \\
 [\forall x  \lnot B(a, x)]
\end{gather}
$$
**TAKE OUT ALL QUANTIFIERS:**
+ Every duplicated quantifier is given a new variable. 
$$
\begin{gather}
\exists x \forall y( \lnot A(x, y) \lor (B(y, x) \lor C(y))) \\
 \land \\
 \forall u \forall v(\lnot D(u, v) \lor \sim C(u))
 \\ \land \\
 D(a, b) \wedge \forall r \forall s A(r, s)
 \\ \land \\
 [\forall t  \lnot B(a, t)]
\end{gather}
$$
+ Take out all of them: 
**Remember:** a and b are constants not free variables. 

$$
\begin{gather}
\exists x \forall y \forall u \forall v \forall r \forall s \forall t
\begin{cases}
(\lnot A(x, y) \lor (B(y, x) \lor C(y))) \\
 \land \\
 (\lnot D(u, v) \lor \sim C(u))
 \\ \land \\
 D(a, b) \wedge  A(r, s)
 \\ \land \\
 [ \lnot B(a, t)]
 \end{cases}
\end{gather} 
$$


3. Transform into SKOLEM:
+ No free variables to bind 

**DELETE EXISTENTIAL QUANTIFIERS:**
$$
\begin{gather}
 \forall y \forall u \forall v \forall r \forall s \forall t
\begin{cases}
(\lnot A(c, y) \lor (B(y, c) \lor C(y))) \\
 \land \\
 (\lnot D(u, v) \lor \sim C(u))
 \\ \land \\
 D(a, b) \wedge  A(r, s)
 \\ \land \\
 [ \lnot B(a, t)]
 \end{cases}
\end{gather} 
$$

**TRANSFORM TO CLAUSES:**
+ Everything is in clause form 
$$
\begin{gather}
 \forall y \forall u \forall v \forall r \forall s \forall t
\begin{cases}
(\lnot A(c, y) \lor (B(y, c) \lor C(y))) \\
 \land \\
 (\lnot D(u, v) \lor \sim C(u))
 \\ \land \\
  D(a, b) \land   A(r, s)
 \\ \land \\
 [ \lnot B(a, t)]
 \end{cases}
\end{gather} 
$$

4. Obtain and analyse the clauses:
Clauses are: 

C1: $(\lnot A(c, y) \lor (B(y, c) \lor C(y)))$
C2: $(\lnot D(u, v) \lor \sim C(u))$
C3: D(a,b)
C4: A(r,s)
C5: $[ \lnot B(a, t)]$

**TRY TO ARRIVE INTO AN EMPTY CLAUSE:**
C6 =>  C1 - C4 : $(B(y, c) \lor C(y))$
C7 => C6 - C5 : C(y)
C8 => C2 - C7 : $\lnot D(u, v)$
C9 => C3 - C8 : $\emptyset$

Reached an empty clause, then unsatisfiable formula, then **correct deduction**



