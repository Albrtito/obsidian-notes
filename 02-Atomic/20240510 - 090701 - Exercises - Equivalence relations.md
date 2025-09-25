---
aliases:
  - Exercises - Equivalence relations
tags:
  - discrete
"References:":
  - "[[Discreta_Exercises_All_Solved.pdf]]"
cssclasses:
  - page-manila
sr-due: 2024-05-22
sr-interval: 2
sr-ease: 188
---
# Exercises - Equivalence relations


## 11.4:
Let R be a relation defined on N × N, such that $(a, b)R(c, d)$ if and only if a + b = c + d. 
Show that R is an equivalence relation on N × N, and that there exists a bijection between the quotient set (N × N)/R and N.

The relation can be defined as a function f, then: 
$$
f(a,b) = a + b = c+ d = f(c,d)
$$
If a function f exists then it is an equivalence relation.

## 11.6: (not-done)
We define the relation R on R2 = R × (R \\ {0}) such that
$$
(a, b) \mathcal{R}(c, d) \quad \Leftrightarrow \quad a d=b c 
$$
Show that this is an equivalence relation, and obtain the quotient set $R_2/\mathbb{R}$

## 11.7: Circular relation
A relation R defined on a set A is a circular relation if it verifies the following property: 
$$
aRb \text{ and } bRc \Rightarrow cRa $$
Prove that a relation is an equivalence relation if and only if it is circular and reflexive.

+ **All equivalence relations are circular**
$$
\text{Equivalence} \Leftrightarrow \text{Circular and Reflexive}
$$
**Proof:**
1. **If** it is equivalence and aRb and bRc => (transitivity) aRc => (Symmetry) cRa **=>** **circular**
2. **If** R is circular and reflexive =>? Symmetric and transitive 
	+ Proof of symmetry: In particular, if the c in the original definition was a b, there would be symmetry:  aRb and bRb => bRa 
	+ Proof of transitivity: aRb and bRc => cRa => (by the just proved symmetry) aRc

## 11.8: Weakly transitive
A relation R on a set A is weakly transitive if, for all elements a, b, c, d ∈ A, the relations aRb, bRc, and cRd imply that aRd. Determine which one of the following two statements is true and which one is false (by proving the former, and giving a counter- example of the latter): 
1. Every symmetric and weakly transitive relation is transitive. 
2. Every reflexive, symmetric, and weakly transitive relation is an equivalence relation.

We have a definition of R such as: 
$$
aRb, bRc, cRd \Rightarrow aRd
$$
**Proof:**
1. We need to prove transitivity for every w.t relation, then for that relation: 
$$
aRb \land bRc \Rightarrow aRc
$$
	We can find a counterexample as, given the relation we know that the following “links” are defined (the relation has defined) based on the initial statement and symmetry: 
	$$ \begin{gather}\text{Initial relations: }aRb, bRc, cRd, aRd \\\text{ By symmetry: } bRa, cRb, dRc, dRa\end{gather}\ $$
+ The symmetry defined relations also cover the ones defined by Weak Transitivity.

	Looking at this definition we see that the transitivity property defined above does not comply(We have aRb and bRc but no aRc). 
	Then we have found a **counterexample** and this statement is **false**

2. Again, we need to prove transitivity as it is the only property of equivalence relations left. 
	Checking for all the relations defined we have: 
	$$ 
	\begin{gather}
	\text{Initial relations: }aRb, bRc, cRd, aRd \\
	\text{ By symmetry: } bRa, cRb, dRc, dRa\\
	\text{By reflexivity: } aRa, bRb, cRc, dRd\\
	\end{gather} 
	$$
	We now see that for all the elements in the relation the transitivity property is met. Then this statement is **true.**

## 11.9: 
The adjacency matrix of a binary relation R is given by:
$$
A_R = 
\begin{pmatrix}
1 &0&1\\
0&1&b\\
1&a&c
\end{pmatrix}
$$
+ Where a,b,c = 0,1
Which conditions should a,b and c satisfy so that R becomes an equivalence relation?

