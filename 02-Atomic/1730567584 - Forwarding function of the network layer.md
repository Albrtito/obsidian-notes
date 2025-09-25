---
aliases:
  - Forwarding function of the network layer
  - Forwarding
  - switching
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-01-17
sr-interval: 40
sr-ease: 270
---
# The forwarding function the netwok layer:
> [!NOTE] Forwarding: 
>  Router local action of transferring a packet from input link intergace to the appropiate output link interface.

 + Takes place in **very short timespaces**. Needs to be done quickly as a lot of packets go through one router. 
 

> [!example] Dictionary: 
> + **switching** → Can be used interchangeably with forwarding 


## Forwarding tables:
Every network router has one forwarding table. These tables are use by the router to **know where each packet needs to be forwarded**. 
+ Data from the packet header is taken and used to index the table. 
+ **IMPORTANT:** These tables are **created by the [[1730567097 - The network layer control plane|Control plane]]**
+ Forwarding tables reference IPs in their [[1730832772 - CIDR Notation|CIDR Notation]], sending all IPs with some prefix to the same place. 

## Types of forwarding algorithms:
###  [[1731418961 - Generalized forwarding|Generalized forwarding]]

> [!attention] MAIN IDEA: 
> A lot of factors matter, not only the destination

### Destination-based forwarding:

> [!attention] MAIN IDEA: 
> Only the destination matters 


> [!NOTE] Intro(Analogy): 
> Each node sees the final destination of a packet and decides **towards where to send it only based on how to arrive to that destination**. 
> 
> If we used cars going though roundabouts with each roundabout having an entry booth the cars would tell the attendand where to go(final destination) and the attendand would just decide wich exit to take at that roundabout.

***