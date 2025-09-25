---
aliases:
  - Protocol - Ethernet
  - Ethernet
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-01-01
sr-interval: 23
sr-ease: 225
---
# Protocol - Ethernet

> [!NOTE] Intro: 
>  The Ethernet protocol is a link layer protocol that uses a random access implementation based on [[1732037327 - Protocol - CSMA-CD|CSMA/CD]].

**Remarks:**
+ The ethernet link card that a host card is called NIC
## Steps: 
**Sending data:**
1. NIC recieves tha datagram, creates the frame
2. NIC **senses channel:**
   + **Empty channel:** Start frame transmission 
   + **Busy channel:** Wait for empty channel 
3. Wait untill the transmission is finalized (the whole frame is send): 
	+ **There is no collision while sending:** Nice, the frame was sent
	+ **There is a collision:** Abort and send a jam signal (saying, I stopped because a collision was sensed)
		+ ==Enter an **binary exponential backoff** → Based on the probability that retransmission will happen → Based on the number of hosts connected to the link.== 
***