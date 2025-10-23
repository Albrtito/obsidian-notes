---
aliases:
  - Semaphores, Dijkstra method
  - Semaphores
Date: 2024-03-18
tags:
  - os
"References:": 
sr-due: 2024-06-10
sr-interval: 41
sr-ease: 210
---
# Semaphores
## Intro:
Dijkstra's method for managing synchronisation between processes is based on a **signalling mechanism** within **the same machine**.  

A semaphore is a really basic concept, it’s **just a counter.** We start by initialising it with any value we want (f.e: semaphoreName = 0) and from that point onwards we’ll subtract to the counter 1 when a process wants to be executed (semWait(semaphoreName)) and adds one when a process has finished to execute (semSignal(semaphoreName)).
Both operations, signal and wait are **atomic**

A process can get the resource if **there is no process running and the count is negative.**

**Remarks:**
+ #duda : Semaphores are implemented in hardware so that their operations can be atomic? In the test of the OS course two opposite answers are given. 

>f.e: If there are 4 processes, all require the same resource. 
	1. Semaphore is created → **semaphoreName = 0** 
	2. P1 get’s the resource → **semaphoreName = -1**
	3. P2 want’s to get it but it can’t as there is another process using it, so it waits → **semaphoreName = -2**
	4. P1 finishes→ **semaphoreName = -1**
	5. P2 gets the resource 
	6. P3 enters → **semaphoreName = -2**
	7. P4 enters → **semaphoreName = -3**
	8. P2 finishes → **semaphoreName = -2**
	9. P4 gets the resource 
	10. P4 finishes → **semaphoreName = -1**
	11. P3 gets the resource
	12. P3 finishes → **semaphoreName = 0**
	
+ **Remark:** See that there is no order specified, P4 can get the resource first even though P3 arrived first.

## Things to have in mind when implementing semaphores:

+ Always follow a known pattern/algorithm that works before doing it yourself: Such as [Algorithm - Problem -Producer-Consumer problem](Algorithm%20-%20Problem%20-Producer-Consumer%20problem.md) or [Algorithm - Readers-Writers problem](Algorithm%20-%20Readers-Writers%20problem.md)

+ Semaphores are known for causing problems, if you deviate from the basic algorithms be reaaaly careful.
	+ Is an example of somethings simple that should work but doesn't.There are usually problems ur not seeing

+ Most of the problems can be done with the two models described below: [Algorithm - Problem -Producer-Consumer problem](Algorithm%20-%20Problem%20-Producer-Consumer%20problem.md) and [Algorithm - Readers-Writers problem](Algorithm%20-%20Readers-Writers%20problem.md)

## Basic usage and implementation:
### Initialisation: 
As we have already seen, semaphores are signalling mechanisms. To use them we’ll include the library `semaphore.h`:

```c
include <semaphore.h>
```

Any semaphore is initialise in the following way:
**Remark:** A semaphore is initialised **for each of the critical resources**

```c
sem_t semaphoreName; //semaphore "semaphoreName"
```

Then to add and subtract from the semaphore we’ll use the following methods: 

### Methods: 
#### semWait(semaphoreName)
semWait subtracts one from the semaphore, then makes the process wait until **the semaphore is negative and no process is running**
+ Why wait until then? Because if the count is negative → Processes are waiting. And if no process is running, this process can start running 
**Remark:** It is important to notice that semaphores by themselves won’t impose an order of execution between processes. So all processes waiting will be executed on any order once a process releases the resource.
#### semSignal(semaphoreName)
semSignal adds one to the count. It let’s the other processes know that the resource is now free to use. 
### Basic model:
1. Initialise the semaphore to 1
2. Indicate the entry point for a critical section with a semWait(s) 
3. Indicate the  exit code from a a critical section with a semSignal(s)

```c

include <semaphore.h>
sem_t semaphoreName; //semaphore "semaphoreName"

// Non-critical code
...
//Start of critical code sectio
semWait(semaphoreName) //Wait until it is possible to run
<CriticalCode>
semSignal(semaphoreName) // Once the critical section is over, signal exit
...
// Non-critical code

```


### Idea of the semaphore / Implement a semaphore: 
We’ll use the semaphore library of c. However how would it look if we wanted to actually implement semaphores as something new:
	The easiest way is to create a queue. When a process is blocked it gets added into the queue. If there is no process running and the count is negative get one process out of the queue. 


## POSIX: 
![POSIX - Semaphores](20240504%20-%20164653%20-%20POSIX%20-%20Semaphores.md)