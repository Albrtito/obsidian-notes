---
aliases:
  - Protocol - Slotted ALOHA
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-16
sr-interval: 6
sr-ease: 210
---
# Protocol - Slotted ALOHA

> [!NOTE] Intro:
> The slotted ALOHA uses fixed slots of time to send data. This prevents collisions but  requires all hosts to be synchronised.  

### Requirements:

+ All frames  must have the same size
+ Time is divided into slots, each slot has the lenght equal to the time required to transmit 1 frame. 

  #duda: The propagation over one link could be different than other. And what if the transmission delay of one host is different from the others?

	+ Everyone can use the slots, however u need to transmit **at the beginning of the slot**

+ Nodes are somehow ==synchronized== 
  >f.e: Using a clock
+ The collision is detected by every node in the system. 
	+ Everyone can see that the link is busy. 
###  Managing collisions:
If there is a collision, **each node that collided retransmits with a probability p**. 
+ P is obtained randomly. The probability of collisions will change with a direct relation to P. The higher the P, the higher the probability of collisions. 

### PROS and CONS: 
+ Same as all random access protocols. 
**PROS:** 
+ With an **small load**, the channel can be used with **little to none problems.** 
+ **Decentralization**, only clocks are needed
+ Really **simple**. 

**CONS:**
+ Collisions = wasting slots
+ **Clock synchronisation is really hard** 

### Efficiency:
With a **huge number of hosts** we’ll have a value for p = 37%. This value will transform into: 
+ 37% of the channel will be used. 
+ 37% of the channel wil be empty. 
+ 26% of the time there will be collisions. 

For an small (or any arbitrary) number of host, the **best value for p will be:**
 $$
 p = 1/N
 $$
 + Where N is the number of hosts in the system. 
#duda: How would a host know how many host are there connected to the link?
***