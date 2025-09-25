---
Date: 2024-03-12
tags:
  - softwareDev
"References:": 
sr-due: 2024-10-18
sr-interval: 170
sr-ease: 250
---
# Intro:
Syntax analysis is used for compilers and parsers that need to understand a language defined formally. These parsers divide the input into tokens that can later be analysed with a parse tree.  **The main goal is to create this parse tree. Abstract syntax tree (AST)**
# Applications and limitations
+ Used for **grammar like input data**
+ Reduces number of test cases
+ Identification of grammar done using system requirements
+ Useful with [Unit testing](20240501%20-%20123051%20-%20Unit%20testing.md) 
+ Not so useful with system testing
+ Not useful for acceptance testing

# Procedure: 
### **Definition** of grammar
Grammar must be type 2 or 3 (regular or context free)	
At most one non terminal at the left
Lambda is not allowed
Avoid recursive grammars: Infinite test cases
### **Draw** derivation tree
Draw the grammar defined as a derivation tree
One symbol one node
Number the nodes: **From top to bottom, from left to right**
Distinguish all levels

### **Identify** test cases
To create all **valid test** cases two steps are required: 
1. Create test cases covering all non-terminal nodes. (Make test that use those non-terminal)
2. Create test cases covering all terminal nodes
For **invalid inputs**: There is to many of them to find them all. A sample is considered by computing what happens if: 
1. Non-terminal nodes are deleted or duplicated
2. If terminal nodes are deleted or duplicated
#duda Estos inputs inválidos son aquellos que tienen el duplicado o el deletion? Como afecta eso a la prueba. Estamos probando que si duplicamos o quitamos nodos me da un input inválido?
### **Automate** test cases


---
### Summary
Highlight ==what’s important!==
