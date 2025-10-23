---
aliases:
  - grammar production rules
tags:
  - review
  - comp
References:
cssclasses:
---
# grammar production rules
> [!NOTE] Intro: 
> Production rules specify how to rewrite one string to another. → **DERIVATION**

Given a general production rule: 
$$
\alpha \rightarrow \beta
$$

- We say that an string w **derives (to)** z when we can go from one to another using production rules
	- $w \Rightarrow z$ : One step derivation
	- $w \Rightarrow* z$ : Multi step derivation

> [!example] properties
> 1. **Derivation:**
>Given a general production rule: $$\alpha \rightarrow \beta$$ 
>We say that an string w **derives (to)** z when we can go from one to another using production rules
>$w \Rightarrow z$ : One step derivation
>$w \Rightarrow* z$ : Multi step derivation
>
>2. **Applicability:**
>   A rule is applicable when it can be used over a substring of w
>3. **Sentential form:** #duda Isn’t it all a sentential form?
>   A sentential form are all strings derivable from the start symbol: $$S \Rightarrow* w$$
>4. **Sentence:** 
>   A word | sentence | valid string, only consists of terminals (terminals are the alphabet of the language, non terminals are just for grammar-use)



***
### Up
- [[1755855042-grammar|grammar]]
### Down
***
