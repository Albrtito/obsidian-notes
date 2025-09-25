---
aliases: 
tags:
  - logic
"References:": 
cssclasses: 
sr-due: 2024-06-03
sr-interval: 14
sr-ease: 241
---
# Proof Theory in Predicate Calculus:
## Intro: 
Once understood the concept of [Logic proof theory](20240409%20-%20122243%20-Proof%20theory.md) we can say the following: 

In order to define a formal proof in Predicate theory we’ll need to identify: 
1. **A: Alphabet** 
	What symbols can we use?
2. **F: SCF (Syntactically correct formulas)**
	What is a valid formula
3. **X: Axioms**
	We’ll build the system on top of these rules
4. **R: Inference rules**
	What is legal to do with the SCF?
	
Most of these have already been defined in [1730994134 - Predicate Logic](1730994134%20-%20Predicate%20Logic.md), however the Inference rules haven’t been previously defined: 

## Inference rules in predicate logic (R):

There are three main inference rules: 
### Modus Ponens:
Same as with propositional logic:

**If** A then B and A is proved, **then** B is proved.
$$
\begin{gather}
\vdash \mathrm{A} \rightarrow \mathrm{B}, \vdash \mathrm{A} \\
\hline \vdash \mathrm{B}
\end{gather}
$$
With atomic propositions (or constant predicates) this one is the one to use.
### Conditional Universal Generalisation:


$$
\begin{gather}
\vdash \mathrm{A} \rightarrow \mathrm{B}(\mathrm{y}) \\
\hline \vdash \mathrm{A} \rightarrow \forall x \mathrm{B}(\mathrm{x})
\end{gather}
$$
#### IMPORTANT CONSTRAIT:
<font color="#ff0000">“y” cannot be a free variable in A</font>
**Remarks:** 
+ A free variable is a variable with no specific value (humans → Free variable, Juan → Not free)
+ $B(y)$ : Represents a s.c.f in which “y” **is a free variable**
	+ f.e: The following formula has y as free variable: $\forall x (P(x,y)\rightarrow \exists z Q(w,z))$ 


### Conditional Existential Generalisation:

$$
\begin{gather}
\vdash \mathrm{A}(\mathrm{y}) \rightarrow \mathrm{B} \\
\hline \vdash \exists \mathrm{x}A(\mathrm{x}) \rightarrow \mathrm{B}
\end{gather}
$$
#### IMPORTANT CONSTRAINT: 
<font color="#ff0000">“y” cannot be a free variable in B</font>
**Remarks:** 
+ A free variable is a variable with no specific value (humans → Free variable, Juan → Not free, $\forall humans$ → Not free?, $\exists humans$ → Not free? #duda )
+ $A(y)$ : Represents a s.c.f in which “y” **is a free variable**
	+ f.e: The following formula has y as free variable: $\forall x (P(x,y)\rightarrow \exists z Q(w,z))$ 



### Generalisation:
For transforming predicates with free variables into predicates with a universal or existential quantifiers.
#### Universal generalisation(UG) - LIMITED:

**IDEA:** From a free variable to all the domain of x
$$
\begin{gather}
\vdash \mathrm{A}(\mathrm{y})  \\

\hline \vdash \forall \mathrm{x}A(x)

\end{gather}
$$
##### LIMITS: 
+ It **cannot be applied on variables that have been introduced by means of existential specification**
+ It cannot be used within an assumption, only in the case that, within the same assumption, we had obtained the free variable by means of Universal Specification. 

**NAMELY (en la práctica):**
+ Only outside assumptions
+ Only if the variable comes from U.S
#### Existential generalisation(EG):

**IDEA:** From a free variable to at least one of the domain of x.

If A is valid for some free variable y. Then there exist a value of x such as A is true. This has no limitation as y is a free variable inside the domain of x. Then there will always exist (at least y) on variable on the domain of x such as A(x) is true.
$$
\begin{gather}
\vdash \mathrm{A}(\mathrm{y})  \\

\hline \vdash \exists \mathrm{x}A(x)

\end{gather}
$$
**f.e:**
	$$ \begin{aligned}& A(y) \\\vdash & A(y) \rightarrow \exists x A(x) \\& \exists x A(x)\end{aligned}$$
### Specification: 
For transforming predicates with universal or existential Quantifiers to predicates with free variables. 
#### Universal specification (US):

**IDEA:** From all the domain of x to one free variable

If A(x) is true for all values of x, then A(y) must be true as y is a free variable inside the domain of x. 
$$
\begin{gather}
\vdash \forall \mathrm{x}A(x)  \\

\hline \vdash \mathrm{A}(\mathrm{y})

\end{gather}
$$
**f.e:**
	$$\begin{aligned}\forall x A(x) & \text { Premise } \\\vdash\forall x A(x) \rightarrow A(y) & \text { Axiom 9 }\\A(y) & \text { M.P. } 1,2\end{aligned}$$
#### Existential specification(ES) - LIMITED: 

**IDEA:** From at least one of the element of the domain of x to a free variable.

If A(x) is valid for all x. And A(y) implies B. Then B can be obtained as a s.c.f

$$
\frac{\vdash \exists x A(\mathrm{x}),, A(y) \rightarrow B}{\vdash B}
$$
##### LIMITS: 
This rule is usually used by introducing assumptions (as in propositional calculus)

![Screenshot 2024-04-09 at 14.08.46](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-09%20at%2014.08.46.png)
+ The variable introduced cannot be used again in another E.S
+ To cancel the assumption B cannot have y as free variable. (Use E.G on it: Then get out some x)
+ To carry out step $A(y) \rightarrow B$, **y cannot be previously subject of U.G, don’t use U.G inside the assumption**
	+ This means that we cannot do anything such as $A(y) \Rightarrow \forall x A(x)$ previously to the conditional statement. 
+ Different variables must be used in different assumptions. 



#### COMMON PITFALLS WITH E.S / U.G  :

1. Assumption of E.S inside another E.S assumptions, variables to generalise to.
   ![Screenshot 2024-04-09 at 14.17.06](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-09%20at%2014.17.06.png)
	1. IF creating an E.S inside another E.S, it cannot be on the same variable as that variable might not be the same that satisfies both
	2. Going out of the assumption, we cannot generalise y with an universal generalisation as it comes from E.S
2. With universal specification, <u>the quantifier must affect the whole formula</u>: 
	+ <font color="#ff0000">Incorrect use:</font> $\forall x P(x) \rightarrow A \Rightarrow P(y) \rightarrow A$
	+ Correct use: $\forall x (P(x) \rightarrow A)\Rightarrow P(y) \rightarrow A$ : The quantifier affects also the A.


#duda: I keep saying that y is a free variable inside the domain of x: Is that true?

## Method to apply: 

1. Extract the quantifiers at the beginning in the complete formulas (Use E.S (This one is the difficult one), U.S)
2. Propositional calculus rules are applied until we get an unquantified version of the conclusion
3. The quantified conclusion is obtained applying U.G(This one is the difficult one) and/or E.G

**GET QUANT OUT** → **GET PROP SOLUTION** → **GET QUANT IN**

