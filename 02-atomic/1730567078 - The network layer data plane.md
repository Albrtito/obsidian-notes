---
aliases:
  - The network layer data plane
  - Data plane
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-07-20
sr-interval: 225
sr-ease: 309
---
# The network layer data plane
The data plane implements the [[1730567584 - Forwarding function of the network layer|Forwarding function of the network layer]]. 

The systems that implement this layer are the [[1730624725 - Router|Routers]],specifically, the input-output and switching fabric components. The data plane also consist in the functions used for **moving packages inside the routers** and avoiding queuing. 

> [!attention] : MAIN IDEA:
> The main idea of the data plane is that it is the part of the network layer that **already has forwarding tables so it KNOWS WHERE TO SEND THE INFO, it then needs to perform the actual MOVEMENT OF DATA INSIE THE ROUTER** 


***