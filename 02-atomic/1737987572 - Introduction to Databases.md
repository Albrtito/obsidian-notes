---
aliases:
  - Introduction to Databases
tags:
  - incomplete
  - filesAndDB
References: 
cssclasses:
---
# Introduction to Databases

> [!NOTE] Why databases: 
>  Information is usefull

## Characteristics of storage:
1. **Perdurability:** How **long** the info will last
2. **Capacity:** How **much** info it’ll contain
3. **Speed:** How **long it’ll take** to access
4. **Range:** From where and how many people will acces the info
5. **Access type:** 

## Types of storage:
We can classify storage and therfore databases by purpose, type of data they store, data semantics, data syntax…

Based on **purpose** information can be saved in order to precess it or in order to store it (among others). 
+ **Inmediate storage:** Aimed for **processing**
+ **Long term storage:** Aimed for **storage**

Defining the database with some **syntax and semantics** will create a **data model**. Based on these models we identify several types of databases.
+ **Serial organisation:** Elements that are similar, doesn’t matter if we take one or another
  > bread in a bakery
  
+ **Sequential organization:** For sorted elements. 
	+ Search through a binary search

+ **Hasshing:** Know where everything exactly goes 
+ **Indexed organization:** Point to where elements are 
	+ **We like this for databases**

Based on whether there is an actual data model or not we can say that the storage is:
+ **Structured:** Has a design, several types of data
+ **Non-Structured:** No design, only one type of data
+ **Semi-Structured:** Combination between the two → Metadata

## Data operations: 
What are we actually doing with the data once we get it into the database? The same basic operations repeat on all storing systems.
+ **Add**
+ **Edit**
+ **Erase/Delete** 
+ **Retrieve/Queries:** Look at the data, check what there is stored

## Static vs Dynamic:
The data and its organisation can change in time. We define the **data that varies in time as dynamic** while the **invariant data or fixed data is called static**:


## Design: 

> [!NOTE] What is design?
> Designing a database is, after all, creating the data model, with the semantics and syntax it conlleva.
> + **Given some needs → Create the solution**

Architecture of databases, three levels: 
+ **Internal level:**  What the admins see, **what is coded.**
+ **Conceptual level:** → Conceptual Schema (Semantics), what the designers see. **What is designed on paper.**  → The conceptual level is represented in the [[1739551767 - Relational DB Model|Relational DB Model]]
+ **External level:** Whatever the **users** see

## Managing the databases: (DBMS)
DMBS or Data Base Managing System are the systems that provide description, manipulation and utilization.  
+ **Description:** Creation of the model, the design. 
+ **Manipulation:** Edits on the model and operation of itself
+ **Utilization:** Support, Queries, API 

***
