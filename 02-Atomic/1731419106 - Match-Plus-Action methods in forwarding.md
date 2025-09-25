---
aliases:
  - Match-Plus-Action
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-07
sr-interval: 13
sr-ease: 270
---
# Match-Plus-Action 
The match plus action process is performed inside the routers, it is an esential function of the data plane **in charge of finding where each datagram should be redirected by looking at the table**. 


## Optimizing searching: 
> [!BUG] Problem: 
> The main problem when looking at a table is how long is it going to take. Input ports need to work blazingly fast and looking at a 4 million entry table is not feasable.
> 

> [!check] Solution: 
> The solution is to use **prefix-matching** to simplify all the probabilities into a few prefixes and output into link-interfaces based on this prefixes.
> 
+ If two prefixes math use **longgest-prefix matching**
+ This still needs to be done super fast. Spetial SRAM,DRAM,TCAM memory is used along with the latest search algorithms to return rows in **constant time.**

## OpenFlow generalised forwarding:

> [!example] Remember: 
> Match plus action is not creating the tables, just using their defined structure 

We’ll look at the match-plus-action method for **generalised forwarding**. This method is ruled by the **OpenFlow** standard. 
### Flow tables:
The forwarding or flow tables contain the following fields for each entry:
+ **Set of header field values (Used for Match)**: Prefix to match
+ **Set of counters:** Updated as packets are matched by the table entry. 
+ **Set of actions(Used foor Action):** What to do when recieving this type of packages.

### Match: 
The OpenFLow standard can look at fields from link,network annd transport layers to assign the package to a flow table entry.
Therefore, the match part of the forwarding table will have aa value for the port, IP source and IP destination. 

| Ingress port | IP Src | IP Dest |
| ------------ | ------ | ------- |
|              |        |         |
+ Of course, a table could have no value for some of this fields at it may not be pertinent or affect the decision. 

### Action: 
There are three types of actions that the flow table can perform:
+ **Forwarding**
+ **Dropping**
+ **Modify-field**

### Example: 
A complete forwarding table following this match-plus-action implementation would have the form:

| MATCH                          | ACTION                |
| ------------------------------ | --------------------- |
| PORT: X, IP SRC: X, IP DEST: X | FORWARD\|DROP\|MODIFY |


***