---
aliases:
  - Protocol - CSMA-CD
  - CSMA/CD Protocol
  - CSMA/CD
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-11-28
sr-interval: 4
sr-ease: 210
---
# Protocol - CSMA-CD

> [!NOTE] Intro: 
> Build on top of the [[1732022695 - Protocol - CSMA|CSMA]] protocol. Provides **collision detection** reducint the time once a collision happens. 

+ If a node detects a collision while it is transmitting, it’ll stop. 

### ==Efficiency:== 
$$
efficiency = \frac{1}{1 + \frac{5t_{prop}}{t_{trans}}}
$$
+ **Prop time:** Max prop delay between 2 nodes 
+ **Transmission time:** Max time to transmit a **max-size** frame 
+ **Efficiency goes to 1:** 
	+ With propagation time going to 0 
	+ With transmission time going to infinity
***