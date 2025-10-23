---
aliases:
  - Router packet scheduling methods
  - Packet scheduling
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-01
sr-interval: 9
sr-ease: 268
---
# Router packet scheduling methods
There are several packet scheduling methods that routers can use. Nowadays they all mus adere to the **net neutrality convention**, which forces ISP to follow three rules: 
1. **No Blocking** 
2. **No Throggling:** No content must be degraded
3. **No paid prioritazion**

## Types of methods:
The main used methods are: 
+ **FIFO** (First in First Out)
+ **Round robin** (Wighted queing)
+ **Priority queue:** This can caouse a conflict with the net neutrality
***