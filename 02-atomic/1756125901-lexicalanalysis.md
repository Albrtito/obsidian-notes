---
aliases:
  - lexical analysis
tags:
  - review
  - comp
References:
cssclasses:
---
# lexical analysis
> [!NOTE] Intro: 
> The lexical analysis is the process performed over an string to transform it into tokens. This tokens save a lexical identifier, the literal word and the position of the string.


> [!example] notation:
> 	
> - **lexeme:** The literal string text that is being refered
> - **token:** We usually refer to the id of the triad as token but it can also be used to define the whole triad
> - **annotated token:** A more specific way of refering the whole triad (id, lexeme, position)



> Example of the tokenization of a package definition statement. 
```go
package main;
```
```
(kwPackage, " ", (1,1))
(identif, "main", (1, 9))
(semicoma, " ", (1,14))
```

**Remarks:**

- Literal strings are only saved when they are needed, for example an identifier.

***
### Up
### Down
***
