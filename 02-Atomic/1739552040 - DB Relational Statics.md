---
aliases:
  - DB Relational Statics
tags:
  - filesAndDB
References: 
cssclasses:
---
# DB Relational Statics

> [!NOTE] Intro: 
> The static part of the Relational Model creates the tables, relations between them, what to do when something related changes and static constraints.
> + The set of all this info is called **Relational Schema/Model and is represented in a Relational Graph**

This note will define the concepts and rules needed to create a **theoretical model**.


> [!example] Naming convention: 
> + **attribute:** A set of the relation
> 	+ **key:** Same thing as an attribute
> + **domain:** All possible values that an attribute can take
> + **relation:** The cartesian product of n attributes 
> + **relation degree:** The number of attributes it has
> + **relation cardinality:** Number of unique tuples in the relation
> + **individual:** An specific tuple of the relation
>

## Relation:
The relations are based on [[Binary Relations]], with the following characteristics:

+ Each related element has a **domain**
+ A relation is the **cartesian product of n domains**
+ Each related element is called an **attribute**
+ Each set of related elements is called a **tuple**

> f.e: Given the DNIs and Names sets: 
> + DNIs: Have a domain given by the properties they must follow.
> + Names: Have a domain given by their type (CHAR)
> A relation between the two of them would be: 
> $$DNI x NAME$$
> And encloses all possible tuples with some valid DNI and name in the domain: 
> $$ (DNI_i, NAME_j) $$
> 

+ Relations can be swown implicitly(**intensive**), with a graph that defines the general form of it. Or explicitly(**extensive**) with all tuples that it contains. 

> [!NOTE] Relation degree: 
> Number of columns


> [!NOTE] Relation cardinality: 
> Number or rows / elements 

### Inherent restrictions:
These are restrictions that **come with the relational nature of this theoretical model.**
1. The order of attributes does not matter
2. The order of tuples does not matter
3. There are **no two identical tuples**
4. Individuals(tuples) are of the same nature.
	* They share the same attribute number (arity)
   + Attributes are single-value and atomic
	   + Single-value: One domain
	   + Atomic: Non-divisible for their aim. #duda: An example of this and why it is a defined property?
#### Referential integrity:
We can also define those **restrictions required for the integrity of the model**:
1. **Integrity of entity:** Each row is unique
	1. No attribute from primary key can take null value #duda: With a primary key defined by several attributes, null means all null or just only one of them null cannot be permitted?
2. **Referential Integrity:** Anything referenced allways exists. So all Foreign Keys mus reference something that exists. 
	1. If it’s null. The reference check is skipped. 
	2. For several attributes. The check can be done in one of the following ways.
	   + **COMPLETE:** All attributes work as one
	   + **PARTIAL:** No check for null part
	   + **WEAK:** If there is a null value, no check. #duda Does this also mean that if an attribute is not there it is seen as null?
	

### Special keys:
When we create a relation/table we have different types of attributes, these are:

+ **PRIMARY KEYS (PK)**: Identifying keys, must be unique and not null → <u>Underlined</u> 
+ **NULLABLE:** Attributes that **can take null** → Use *
+ **FOREIGN KEYS (FK)**: Identify associations → <u>Underlined</u> and with an arrow to the referenced key
	+ Same number of keys as the PK of the referenced relation, see referential integrity with [[#Referential integrity]] in order to see how this is checked.

## Protecting integrity 

### Protecting referential integrity:
> [!NOTE] Idea: 
> When deleting a reference to other relation the referential integrity rules state that no reference can be left orphan, or if so (is set to null) it must be said directly. 
> 
> Referential integrity **is in danger when delete or update operations are performed**. There are several options when this happens. 

+ **Restrict:** Any operation on fathers with children is prevented
+ **No Action:** Execution is prevented when it breaks the integrity
+ **Cascade:** The operation will be extended to the tuples containing old non-valid values.
	+ → Father dies, related  children die
+ **Set Null:** When the father dies, all childrens references point to null
+ **Set Default:** A default value is set if the father dies.

### Restrictions in the semantic:

> [!NOTE] Idea: 
> Restrict the actualization (operations on) data if some condition is not met.

+ There are two types: **Simple and Assertion**

#### Simple semantic restrictions:
Applied in the definition of **one element, their implementation si part of the element implementation.** 

#### Asertions or general restrictions:
Apply **on the whole DB** and **concerns several elements.**
+ Independendly implemented
+ Usually not implemented as it requires high computational costs

## Design documentation:
The whole design must be completed by adding documentation that details several aspects of the model and can be separated into:

+ **Explicit semantica assumption:** any requirement **provided by the client** 
+ **Non-observed explicit semantic assumption:** What is **not included in the proposed design**.
	+ A possible solution may be given 
+ **Implicit semantic assumptions:** Info **not provided by the client** but taken into account as it is needed for the design.