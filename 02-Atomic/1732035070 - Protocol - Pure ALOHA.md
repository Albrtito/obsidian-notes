---
aliases:
  - Protocol - Pure ALOHA
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-06
sr-interval: 12
sr-ease: 250
---
# Protocol - Pure ALOHA

> [!NOTE] Def: 
> Pure ALOHA tries to solve the problem of clock synchronisation by deleting time slots. This **lowers the efficiency** but provides a better **decentralization** 

+ This means that collisions can also happen if someone is in the middle of the transmission. 

### Efficiency: 
The efficiency goes down by a lot to 18% for an infinite amount of nodes.
+ The efficiency for some value of p and N will be: 
  $$
  p()
  $$
+ Any frame that is send will collide with other frames that are send in the interval $(t_0 -1, t_0 + 1)$. There will be collision with any system that transmits in that interval. 
	+ This after all means that **the number of collisions rises.**


## Verbessern the protocol: 
What if we wanted to verbessern the protocol. Just by **checking if the channel is busy we’ll stop collisions.** This implementation is [[1732022695 - Protocol - CSMA|CSMA]]
***