---
Date: 2024-03-18
tags:
  - os
"References:": 
sr-due: 2024-07-04
sr-interval: 72
sr-ease: 263
---
# Intro: 
A race condition is when two concurrent processes edit the same variable at the same time. Without a proper execution structure the order is not defined and the result could change to unexpected results. The example given in class is really straightforward: 
f.e: 
	Both processes do the same (suma is mistyped, it's sum). A possible execution is for one to execute after the other, then total =200. However other possible executions could output 100. If instead of two processes we had 6 or more, solutions would be completely unexpected.
	![Screenshot 2024-03-18 at 17.33.31](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-03-18%20at%2017.33.31.png)


The only way to **solve the race condition** is to enforce a path. Enforce an order such as only one order is the right one. 

**Remarks:**
+ When thinking about instructions as atomic be careful. The only way to be sure than an instruction is atomic and no race condition will apear is to look at the assembly, and even then, be careful. An instruction in C can hide several instructions in assembly. 
# Solving the race condition: 
The main principle to follow in order not to have race condition problems is: 
+ **The functionality of a process needs to be INDEPENDENT from the speed of execution of the process wrt other processes**

The most common solution in order to follow this principles is [Mutual exclusion](Mutual%20exclusion.md) or ensuring than a set of instructions can be executed atomically. This means that the set of instructions will execute all together with no other process instructions in between. 

**What is mutual exclusion?**
	![Mutual exclusion](Mutual%20exclusion.md)

