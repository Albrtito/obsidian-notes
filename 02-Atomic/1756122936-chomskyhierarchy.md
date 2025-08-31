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
	- Left-right linear
- Type 2: Context-free grammars
	- No terminals on the right
- Type 1: context-sensitive grammars
	- The context is important so rules cannot change it.
	  $$$$
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
