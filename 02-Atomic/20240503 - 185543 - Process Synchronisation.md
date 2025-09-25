---
aliases:
  - Process Synchronisation
tags:
  - os
"References:": 
cssclasses: 
sr-due: 2024-09-08
sr-interval: 114
sr-ease: 283
---

# Process synchronisation:
## Communication mechanisms: 
How can we transfer information between two processes, there exists several mechanisms to do so: 
+ Files 
+ Pipes(pipes, FIFOs)
+ Shared memory variables
+ Message passing 

During the OS course we’ll work with **shared memory variables**
## Synchronisation mechanisms: 
Synchronisation between processes is the concept of managing how the processes share information between one another so there are no conflicts and the information is not changed in non-intended ways.

Synchronisation mechanisms **allow to enforce that a process stops its execution until an event happens in some other process**

In order to synchronise processes we use services provided by the OS such as: 
+ [Semaphores](20240503%20-%20190310%20-Semaphores%20Dijkstra%20method.md) 
+ [Mutex and conditional variables](20240504%20-%20162315%20-%20Mutex%20and%20conditional%20variables.md)
During the OS course we’ll focus on those two with an entasis on mutex and condition variables as semaphores can be to fixed to models. 
Other services could be

+ **Monitors**

These methods are based on the concept of how synchronization operations must be **atomic**. 