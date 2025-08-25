---
aliases:
- lexical analysis
tags:
- review
References:
cssclasses:
---
# lexical analysis
> [!NOTE] Intro: 
> The lexical analysis is the process performed over an string to transform it into tokens. This tokens save a lexical identifier, the literal word and the position of the string.

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
