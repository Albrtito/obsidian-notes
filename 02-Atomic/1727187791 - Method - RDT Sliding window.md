---
aliases:
  - Method - RDT Sliding window
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-05
sr-interval: 33
sr-ease: 205
---
# Method - RDT Sliding window

## Sliding window mechanism:
![[1727176650 - Principles of reliable data transfer-1.png]]
#duda: Entonces esperamos a que los que están en la porción amarilla se ack para volver a mandar? Ese tiempo de espera es así?

+ The packets in flight are those inside the window. 
+ The packets inside the window are **remembered**. 
	+ Once a package is acknowledged a new package enters the window and the acknowledged package is forgotten. 

There are two implementations that **end the whole chain of thought that has been explained in** [[1727176650 - Principles of reliable data transfer|Principles of reliable data transfer]].
### Selective repeat:
+ The receiver needs a buffer, as big as the one in the sender that can store packages in order to reorder them. 

> [!BUG] Problem: 
> + Managing so many timers for each of your connections is challenging. 
> + Storing that many packages in the receiver side is not ideal?

### Go-Back-N: (The good one)
==Only one timer. This timer is associated to **the oldest package in the window.*Contents*== 

The receiver only wants the next package, if this package is not received, then it s**ends an acknowledgment for the package it is waiting for.**
+ Once the receiver drops one package of the window, then the whole window is retransmitted starting from the package that was lost.



***