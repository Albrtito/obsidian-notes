---
aliases:
  - Congruent relation
tags:
  - discrete
"References:": 
cssclasses: 
sr-due: 2024-06-13
sr-interval: 32
sr-ease: 268
---
# Def:

The congruent relation is defined as an [Equivalence relations](Equivalence%20relations.md).Where two elements are related if they are congruent: 

> [!NOTE] Congruent relation
> Two elements a and b are **congruent modulo m** if m | (a-b). This relation is denoted as: 
>$$
 a \equiv b\mod m
>$$

+ This means that **under the division by m**, a and b have the same remainder.
$$
\begin{gather}
m | a \Rightarrow m = qa + r_1 \\
m | b \Rightarrow m = kb + r_2\\\\
\boxed{r_1 = r_2}
\end{gather}
$$
+ This can also be defined as: 
$$
a \equiv b \mod m \Leftrightarrow m | (a-b)
$$
+ And the same definition can be given in a less formal way such as: 
$$
\begin{gather}
a \equiv b \mod m\\ \Leftrightarrow\\
a \mod m = b \mod m
\end{gather}
$$
**Remarks:**
+ a is related to b: $a \equiv b (\mod m)$ **if and only if**: $a (\mod m) = b (\mod m)$. **This means** exactly the same as what is said above. Both have the same remainder under the division by m
+ **If** $a \equiv b (\mod m)$ **then**: a = b + km $k \in Z$
# Equivalent relation: 

## Proving the equivalent relation:
In order to prove that the relation is equivalent the three properties of equivalent relations mus be proved: 

1. **Reflexivity:** We can prove reflexivity by proving that any element a is related with itself. 
   Because we know that m | 0. Then by using the definition:
	$$
	a \equiv a \mod m \Leftrightarrow  m | (a-a)  = m|0
	$$
	
	This is true for any a. Then reflexivity is proved. 

2. **Symmetry:** To prove symmetry we need to prove that for any a and b. 
   $$a \equiv b \mod m \Leftrightarrow b \equiv a \mod m$$
   By definition this holds (they share remainder). However lets expand the definition. 
   **IF:**
   $$a \equiv b \mod m \Leftrightarrow m | (a-b)$$
   **Then**
   $$ m | (a-b) = m | -(b-a) \Rightarrow m | (b-a)$$
   m divides b -a meaning that the definition holds for aRb and bRa
   
3.  **Transitivity**

## Equiv. classes and quotient set: 
The equivalence classes (or **congruent classes**) modulo m for an equivalent congruent relation of mod m are: 
$$
[a]_m = \{b\in Z: a \equiv (\mod m)\}k = \{a + mk : k \in Z\}
$$
Because this means nothing to anyone trying to understand this let’s explain it in a friendly way: 

Every time we create a relation mod m means dividing any element in the domain of the relation (Z) by m and looking at what the remainder of that division is. For some value of m we’ll have several possible remainders based on the number we divide by m.
	f.e: The relation based on the mod 4 means dividing by 4 and looking at what the remainder is, all the possible remainders we can get when dividing by 4 are 0,1,2,3. Then we can create the equivalent classes, one for each value that the remainder can take. 

**Remarks:** There are only m equivalent classes for the congruent relation mod m defined by the **quotient set of the relation**: 
This is the notation usually used: 
$$
Z_m = \{[0]_m,[1]_m,...,[m-1]_m\}
$$
More formally: 
$$
Z_m ) \{[a]_m: 0 \leq a \leq m-1 \}
$$

# Practice cases: 
## Clock: 
With clocks the congruent relation is defined over mod m when m = 12 as there are 12 possible hours in a clock. 
Based on this modulus, we can obtain that any hour has a remainder mod 12. If the remainder is equal to 0 then the hour is either 12 or 24. 
We do not actually care about numbers bigger than 12, that is why we use the congruent relation. 


