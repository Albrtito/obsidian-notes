---
aliases:
  - E.R
tags:
  - discrete
"References:":
  - "[[20240510 - 090701 - Exercises - Equivalence relations]]"
cssclasses: 
sr-due: 2024-06-22
sr-interval: 41
sr-ease: 232
---
# Intro and definition
> [!NOTE] Definition 135
> An relation R is an **equivalence relation**: 
> IF: It is reflexive, symmetric and transitive
> This means that it complies with the properties of: 
> + [Transitivity](20240415%20-%20123134%20-%20Transitivity%20property.md)
> + [Symmetry](20240415%20-%20123138%20-%20Symmetry%20property.md)
> + [Reflexivity](20240415%20-%20123128%20-%20Reflexivity%20property.md)

**Remarks:**
+ If R is an equivalence relation such as aRb. This can be denoted.  
$$
  a \equiv b (mod R)
$$
This is further studied in [[Modular arithmetic]]

## Theorem function - relation: 

> [!NOTE] Theorem
> If R is defined by a function, then R is an equivalent relation. 

# Equivalence classes: 

> [!NOTE] Definition 136: Equivalence classes.
> For an equivalence relation on set V. All members of the set related to a certain element v $\in$ V belong to the equivalence lass **determined by v**. (they are related to v in some form defined). This is formally defined as: 
> $$
> [v]_R \text{ or simply } [v]
> $$
> with:
> $$
> [v]_R = \{w \in V: vRw\}
> $$
> Any element $w\in [v]_R$ is a representative of the equivalence class $[v]_R$. This means that if v and w both belong to the same equivalence class, it is the same to write $[v]_R$ than $[w]_R$ as both define the same class. 

**Remarks:** Let R be an equivalence relation on V, then:
+ $[a]_R$ is non-empty for all $a\in V$
+ For any two elements in the domain (a and b). Then: 
	**Either** they are related: Same equivalence set: $[a]_R = [b]_R$ and $aRb$ 
	**Or**: They are not related, the intersection between their equiv. sets is empty. $[a]_R \cap [b]_R = \emptyset$ 
## Quotient set: 

> [!note] Definition: Quotient set
> The quotient set of an equivalent relation contains **all the equivalence classes** of the relation. 
> $$
> {A\over R} = \{[v]_R\}, \forall v\in V 
> $$
> This sets **forms a partition on the domain V**

**Remarks:**
In the same way, given a partition of V $\{V_1,V_2,V_3,…\}$ an equivalent relation can be found such as it’s equivalent classes are $V_1,V_2,…$


