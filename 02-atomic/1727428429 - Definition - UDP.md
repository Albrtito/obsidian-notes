---
aliases:
  - UDP
  - Definition - UDP
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-12
sr-interval: 40
sr-ease: 230
---
# UDP

> [!NOTE] Definition: 
> UDP is an **internet transport protocol service** that offers unreliable but faster data transfer. It’s a pseudo to **User Datagram Protocol**
> 

+ Requires c**onnectionless demultiplexing**
+ Really simple protocol
+ **Small header size**
+ **No congestion control**: Functions even with congestion
+ **No reliability:** Segments may be out of order
+ **Best effort service:** Send and hope for the best

**Remarks:**
 + UDP exist because it needs much less memory than TCP (**Smaller header**) and requires less time to send the packages. 
 + It does not provide anything else than the data transfer by itself. Everything must be **developed in the application layer**. 
+ It does contain a [[1727177356 - Method - Checksum|Checksum]] area to check for bit errors. 

![[Screenshot 2024-10-04 at 1.30.32 PM.png|center]]


***