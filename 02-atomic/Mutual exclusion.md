---
Date: 2024-03-18
tags:
  - os
"References:": 
sr-due: 2024-06-19
sr-interval: 42
sr-ease: 186
---
# Intro: 
Mutual exclusion is **a method used in order to solve the [Race condition](Race%20condition.md)**. 
	The race condition is when two processes want to alter the same resource at the same time. In order to avoid this from happening mutual exclusion is used. 

Mutual exclusion is the blocking of a resource when a process is using it, defining [Critical sections](Critical%20sections.md) for each of the processes. 
**Namely:** If a process uses a resource no one else can use it till it finishes. **Avoid two processes in need of the same resource from executing at the same time**




# Problems with mutual exclusion: 
In the following sections we’ll see implementation of mutual sections. This methods for implementation sometime make it hard to create this problems, however they can almost always appear if not being careful about them.
## Deadlocks
Deadlocks appear when doing mutual exclusion with multiple resources. 

The best way to understand it is through an example: 
Imagine that we had two processes P1 and P2 and two resources A and B. This resources can be whatever, lets say they are global variables for this example.

1. Process P1 blocks resource A because it needs to be used and no one can change it
2. Process P2 blocks resource B because it  needs to be used an no change 
(Everything ok till here)
3. Process P1 wants to block B to use B and A at the same time (A is not free), so starts waiting for P2 to free B
4. Process P2 wants to block A to use B and A at the same time (B is not free), so starts waiting for P2 to free A
**And they can keep waiting forever** (Here is the problem)

### Solution:
The **general solution to solve deadlocks**: Everyone uses the resources in the same order

## Starvation: 
A process is indefinitely blocked waiting to enter a critical section. A resource is used all the time between two processes, they take turns for the resource and do not let other processes to access it. 

### Solution: 
To **solve starvation problem** we need to ensure that no process is blocked forever, schedule use of resources another way. 

# Conditions for mutual exclusion
1. Only one process is allowed to be at the same time into the critical section of a resource.
	1. The critical section of a resource is defined as any section that needs that resource. 
	2. No two processes can be at the same resource, duh.
2. A process that request enter into a section **cannot be postponed indefinitely**
3. If no one is in a critical section, anyone can enter immediately 
4. **No assumptions about relative speed of processes or about the number of processors must be made;** When developing the code, it should not matter the number of cores there are or how fast everything is done. This changes for each machine and can vary the code execution. 
5. **A process must stay in its critical section for a finite amount of time**: This means that it cannot hold a resource forever. 
6. Any mechanism for implementation of mutual exclusion must provide synchronisation between processes, meaning: 
	1. **Each process must request access to the section**
	2. **Each process must signal when exiting the critical section**

fe: 
```
\Non-critical code

...
<Entry to critical section> (request acces)

Critical section code

<Exit from critical section> (signal the exit)
...

\Non-critical code
```
# Implementation: 
## Alternatives to mutual exclusion: 
There are several ways of implementing mutual exclusion, we’ll se a few of them during the OS course, but before that, some **alternatives to mutual exclusion** could be: 

+ **Disabling interruptions** : This way the process cannot be interrupted and the section is executed as a whole. However this only works for **mono-processor systems**

+ **Machine instructions** : test and (set or swap). Problems such as starvation and deadlock are still possible (see below)

Any other alternatives rely solely on the OS. 

## Semaphores:
As said in:[[#Conditions for mutual exclusion]], any process must signal when entering the section and when exiting it. This is on what semaphores rely on:

![20240503 - 190310 -Semaphores Dijkstra method](20240503%20-%20190310%20-Semaphores%20Dijkstra%20method.md)

## Mutex and Conditional variables: 
![Mutex and conditional variables](20240504%20-%20162315%20-%20Mutex%20and%20conditional%20variables.md)