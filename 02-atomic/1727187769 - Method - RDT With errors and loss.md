---
aliases:
  - RDT With errors and loss
  - Method - RDT With errors and loss
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-15
sr-interval: 42
sr-ease: 210
---
# Method - RDT With errors and loss

> [!BUG] PROBLEM: 
> We already described the [[1727187698 - Method - RDT With bit errors|Method - RDT With bit errors]], this method has one **main problem**:
> If an acknowledgement package is **lost**, then **the system will forever keep on waiting for the package to arrive.**

**Solution:**
Once the package is send a timer starts, when the timer ends, the sender asumes that the package has been lost **and retransmits it**. 
+ Duplicate packages can be generated → We already have sequence numbers to deal with this. 
+ ==The timer waits for **exactly 1 RTT** (Round Trip Time)==
	+ To compute the RTT we can check the history of packages sent and how long they took. **However the only variable that will change the RTT is the queueing delay**. This means that the last package wont be a good prediction of the next one. → See [[1728377926 - Timeout estimations TCP|Timeout Estimations TCP]] for the real world example
	+ Because it is an estimation. The RTT will be wrong some times. 
	+ For the first package: Either be very agressive and start sending with small RTT untill there is a response, or be loose and set a long RTT. THe thing is we need that first response to estimate a better RTT.
+ We say that packages are retransmitted, however ack packages are **never retransmitted** but send again for a retransmitted package.
### Complete FSMs:
**Sender:**
	![[1727176650 - Principles of reliable data transfer.png]]
+ This sender **does not retransmit over negative acknowledgment**. It only retransmits over timeouts.

**Receiver:**
+ Is unchanged with respect to the last model 


> [!bug] ==PROBLEM:==
>  ==If any acknowledgment can appear at any arbitrary time, then the packages would need to be differently numbered, this cannot be implemented. In order to solve this we **asume that packages have a time to live** in the network. (TTL)==

### ==Performance problems:== 
This system has performance problems due to the waiting time RTT that the sender needs in order to **wait for the ACK.**

We can solve this by allowing **multiple packets in flight**. Start sending packages even though we havent recieved the ack for the previous ones. 

To solve this problems we’ll use:  [[1727187791 - Method - RDT Sliding window|Method - RDT Sliding window]]

***