---
aliases:
  - chomsky hierarchy
tags:
  - review
  - comp
References:
cssclasses:
---
# chomsky hierarchy
> [!NOTE] Intro: 
> The Chomsky hierarchy separates grammars into different classes based on the **types of languages thay can produce**

Types contain each other and are numbered from the biggest to the smallest: 3 → 0 

- Type 3: Regular grammars
	**Right linear:**
$$P = \{(A::=aB) \cup (A::=a) ; A, B \in \sum _N \land a\in \sum _T\}$$
	**Left linear:**
$$
P = \{(A::=aB) \cup (A::=a) ; A, B \in \sum _N \land a\in \sum _T\}
$$
- Type 2: Context-free grammars
	- No terminals on the left
	  $$P = \{A::= v : A\in \sum_n \land v\in\sum^+\} $$
- Type 1: context-sensitive grammars
	- The context is important so rules cannot change it.
	  $$xAy \rightarrow xvy$$
- Type 0: Recursively enumerable grammars
  $$ u ::= v : u \not = \lambda : \text{at least one non-terminal in u}$$
	- How to know if is type 0? → Check if it is not one of the other three. 


**Remarks:**
- For programming the most relevant grammars are regular and context free (types 3 and 2)

***
### Up
- [[1755855042-grammar|grammar]]
### Down
***
