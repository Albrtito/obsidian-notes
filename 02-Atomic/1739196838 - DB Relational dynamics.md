---
aliases:
  - DB Relational dynamics
tags:
  - filesAndDB
References: 
cssclasses:
---
# DB Relational dynamics

> [!NOTE] Intro: 
>  The relational dynamics of a model are responsible of **changing the state of the set of relations that create the database.**
>  + Changes are done in some time
>  + In order to perform the changes a language in required
>  + Operators can either inspect or change.

## Relational languages: 
Relational languages are: 
+ Domain spacific
+ Declarative
+ Of specification type

Two types of languages are described based on their approach to obtain results. 
1. **Relational algebra:** Describes the changes to be done.
2. **Relational calculus:** Describes the goal to achieve.
### Relational Algebra:

Operators are classified into unary and binary. 
+ **Unary operators**: Only applied to one relation 
+ **Binary operators:** Applied to two relation 
+ **Bin. Compatible:** Applied to two relations but:
	+ Must have the same degree
	+ Must have the same data nature (two by two). We call this being compatible.

This operators can also be divided between primitive/primary or derived:
+ **Primitive:** Cannot be obtained from others
+ **Derived:** Can be obtained from others:
	+ Intersecction
	+ join
	+ Natural Join
	+ division
	+ Semi-join
	+ Anti-join
	+ Outer-join

Unary operators of relational Algebra: 
1. **Selection:**
$$
\sigma_{\text{predicate}}  \text{(Relation)}
$$
Selects all values of the selected relation where the given attribute complies with some conditions. 

 2. **Projection:** 
$$
\pi_{atrib1,atrib2...} (Relation)
$$
Creates a subRelation that contains only the selected attributes from the original relation. 


This algebra lets any chain of operators (expresions) be assigned into a symbol, this is called **renaming**.
$$
\rho_\text{symbol} (Expression)
$$
$$
S \equiv Expression
$$

Bin. compatible operatores of relational Algebra: Set operators.
1. **Union:** Obtain all non-repeated tuples from both tables. 
   + Both tables must be compatible
$$
	   RelationA \space \cup \space RelationB
$$
2. **Intersection:** Obtain all repeated tuples (both relations have them) from both tables.
	+ Both tables must be compatible
$$
	   RelationA \space \cap \space RelationB
$$

3. **Difference:** Obtain that appear on the first relation but are not present on the second one.
$$
	   RelationA \space - \space RelationB
$$

Binary operators or Join operators. Require two tables but those tables must not be compatible or meet any criteria. 

1. **Cartesian product:** Obtain every combination of tuples of both relations. 
	$$
	   RelationA \space X \space RelationB
	$$
2. **Join:** Subset of the cartesian product where a condition is met. 
$$
   RelationA \space \Theta \space attrib1 \space \leq | \geq | = \space attrib2 \space RelationB
$$
	1. **Natural join:** A particular case of the join operator, where the applied condition is the equality. 
	   $$
	  RelationA \text { * }_{\text{attribute}} \text{ RelationB}
	   $$
	   
	   This can be used in three ways:
	   + Without the attribute name: Then it is assumed that the only common attribute is used
	   + With an hourglass symbol instead. Meaning that a foreign key is taken. 
	   + With a conditional expression

