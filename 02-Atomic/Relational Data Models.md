---
tags:
  - filesAndDB
---
Based on the mathematical notion of relation: 
A possible described relation would be:
$$
R: N xN R\{(x,y)/ y = x^2\} \Rightarrow R\{(1,1), (2,3), (3,9),...\}
$$
## Main definitions and ideas: 
**Domain:** Set of values of the same nature. What type of values can be stored. (this is given by some kind of restriction or rules: f.e: a name must be a char with no more than 50 characters)

**Attribute:** An attribute is an aspect shared by the elements of a 
relation. (f.eThis means that the attribute Name1 is defined inside the Name domain and can be a )
### [Relation](Relation):
+ Subset of the cartesian product of n domains. All possible combinations of two domains. It is given a name as the generalisation of all those combinations( it is seen as the title in most cases(table design))
+ Similar to the table title idea: A relation is the set of occurrences defining a collection individuals. (the table with all the individuals)
**A relation can be defined intensively or extensively.** The intensive definition defines the invariable static structure of the relation while the extensive definition describes a set of tuples of the relation in a certain moment(time is involved with it, it's like making an screenshot)


#### Characteristics: 
+ **Degree of a relation:** Number of attributes in the relation
+ **Cardinality:** Number of elements in the relation. 
**Example:**
	![Pasted image 20240225180934](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240225180934.png)
+ A tuples in the relation is one specific row of pairs of attribute + the values for the attribute for an specific entries. (f.e For the second row of the picture above the tuples are: ((Name, Carlos)(DNI,XXXXXXX)(Telephone,XXXXX))) 
#### RESTRICTIONS:
 + This makes it so that the order of the tuple does not matter
+ There cannot be two identical set of tuples, at leas something between the rows has to be different to create identification.
+ Because there has to be some identification, this means that there must be an attribute that identifies each row. This is the [Primary Key](Primary%20Key.md)
+ An attribute with a possible null value(optional attributes) are denoted with an asterisk *
#### [Foreign Key](Foreign%20Key.md)
An attribute can reference to the attribute of another relation, this is called an **association**. This is done through the foreign key. This reference can be to another attribute or to a set of attributes. 

## Restrictions and notation
+ [Primary Key](Primary%20Key.md) must be noted: **PRIMARY KEY (PK) **  
+ Alternative keys to the primary are called **Candidate keys**, they are marked as unique: **UNIQUE (CK)**
+ All values that are **not mandatory** must be noted as **NOT NULL**
+ Associations are noted: **FOREIGN KEY (FK)**
+ **What happens when referential integrity is endangered?** : [Integrity rules](Integrity%20rules.md)
+ **What happens when the semantics are rejected?**: [Semantic restrictions](Semantic%20restrictions.md)
## Relational design: 
The creation of the schema that defines relations and associations inside a relational database is called relational design. This relational design contains: 
+ The relational integrity rule for each relation
+ Set of all relations, their constrains and definitions
This is all gathered in the [Relational Model](Relational%20Model.md)
