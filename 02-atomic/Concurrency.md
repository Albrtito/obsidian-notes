---
Date: 2024-03-18
tags:
  - os
"References:":
  - https://aulaglobal.uc3m.es/pluginfile.php/6794419/mod_resource/content/1/T3.L1-Concurrency-Intro-Concepts.pdf
sr-due: 2024-07-30
sr-interval: 72
sr-ease: 224
---

# Advantages of concurrent execution: 
**Sometimes** (not in most cases) is easier to program in parallel. An example is web servers as they can be seen as a parallel system where each client works in parallel. However if the problem being solved is not initially  parallel then it is not that of an advantage.

Since the late 2000 the clocks inside the CPU cores cannot go faster. This means that we cannot make clocks that go faster without overheating. 
We have however developed better transistors, this means that we can now input more into the CPU. This resolves into concurrent execution as **making programs parallel** is the key for **program speed** 

But there where also big advantages of concurrency before there where even multicore CPUs. Why was it better? The main difference is based in the user experience. The advantage of having multiple users using the same core with concurrent execution make it so both users have a better experience. w

The last main advantage is on the usage of IO. Concurrency lets the CPU work on another process while the IO work is being done in another process.

# Kinds of concurrent processes
## Independent: 
Processes run without interaction between them. **The easy way of doing concurrency**
+ No communication 
+ No synchronisation

> [!Attention] Remakr:
> + Comparten recuros de hardware
> + Siguen compitiendo por los recursos al tenerlos compartidos

## Cooperating: 
Process that run concurrently with some interaction.Something about one of the process is needed for the other one. 
This is **way harder** than independent concurrency as managing the interaction gets really complicated. 
+ Possible communication
+ Possible synchronisation (they have to finish together at one time)

### Interactions between processes: 
+ **Shared resource**
	Both processes use the same data or compete for that data. Competing for the data happens in a [Race condition](Race%20condition.md)
+ **Communication** 
	Shared global variables or some messaging between processes
+ **Synchronisation:** 
	A process having to wait for events in other processes. This is using resources until the other process ends. In order to ensure synchronisation methods such as [[20240503 - 190310 -Semaphores Dijkstra method|Semaphores]] or [[20240504 - 162315 - Mutex and conditional variables|Mutex and conditional variables]] are used.
	+ Other methods such as an [[20240408 - 164250 -Atomic Execution|atomic code snippet]] can be used. 

# Algorithms to solve problems. 
Based on all explained for this chapter two possible algorithms appear in order to solve process concurrence. This algorithms are explained from the point of view of the problem they are created to solve. 
+ [Algorithm - Problem -Producer-Consumer problem](Algorithm%20-%20Problem%20-Producer-Consumer%20problem.md)
+ [Algorithm - Readers-Writers problem](Algorithm%20-%20Readers-Writers%20problem.md)