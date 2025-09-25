---
aliases:
  - White box testing
  - Structural testing
tags:
  - softwareDev
"References:": 
cssclasses: 
sr-due: 2024-08-08
sr-interval: 73
sr-ease: 297
---
# White box testing: 
## Intro:
Structural or white box testing focuses on the **internal structure of methods.** 
+ Test **all paths**

We care about whatever is in the box.
![Pasted image 20240501124251](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240501124251.png)

There are different techniques: 
+ **Control flow** : Look at the execution paths and create test for each of them. 
+ **Data flow**: Focus on the definition, usage and deletion of variables
All these techniques are **applied during unit-testing**
---

## Advantages: 
+ All code paths can be verified as tested or not. There is a countable number of them
## Disadvantages: 
+ Number of paths can be to large for testing
+ Difficult to detect **data sensitivity errors** (p = q/r) #duda  Why so difficult?
+ **Assumes control flow is correct** (the implementation (it works), now we test if it works well or not) 
+ Need of programming skills 
 

## Types of white box testing: 
+ [Control flow testing](20240501%20-%20143420%20-%20Control%20flow%20testing.md)