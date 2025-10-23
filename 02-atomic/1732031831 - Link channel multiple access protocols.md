---
aliases:
  - Link channel multiple access protocols
  - Channel multiple access protocols
  - MAC Protocols
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-06
sr-interval: 12
sr-ease: 250
---
# Link channel multiple access protocols

The link layer must decide how each channel is accesed, not all channels provide bowth ways connecttion, not only that but most of the channels must provide an operating window for tons of hosts and must manage that. These protocols are used to figure out how 

## Where does the problem appear?
Links can have collisions: 

> [!NOTE] **Collision**: 
> Collisions happen when a node recieves two or more signals at the same time. 

 Collisions make it so no info is transmitted, these protocols try to solve this problem. 
## What must the protocol provide?
In order to solve this the **multiple access protocols are used,** these protocols must:

+ Figure out how nodes are going to transmit and coordinate
+ The protocols must **use the same channel that is being coordinated.** 

### Ideal framework: 

> [!NOTE] Info:
> We’ll use the following ideal properties of a multiple access protocol to compare the specific protocols defined. 

**Remark:**
 + R is defined as the rate at which a host can transmit info through an specific link. 

1. When **only one node** wants to transmit it can send at **rate R** 
2. When **M nodes want to transmit**, each can send at **average rate R/M.** Distribution of the link over all nodes. 
3. ==There **wont be a centralized entity** that synchronises. There is a decentralized network of links.== 
4. We would like for the protocol to be **simple**. 

## Types: 
Based on the solution provided we ddefine several types of these protocols: 
### Channel partitioning:
We divide the channel into smaller pieces. Each node has a piece.
+ There are no collisions in this method
+ **Good for high channel loads, **bad for low channel loads**

  > A piece could be a t ime slot, a frequency or something similar. 

+ Among these types of protocols are:
	 + [[1732020527 - Protocol - TDMA|TDMA]] : Channel divided by time slots
	 + [[1732020800 - Protocol - FDMA|FDMA]]: Channel divided by frequency slots.
### Random access:
Channel does not divide or partition. Whenever a host wants to acces it does. 

+ We need a way to **detect/recover from collisions.**
+ Opposite from the channel partition: **Good for low** channel load, **bad for high** channel load. 
+ Among these types of protocols are: + 
	+ [[1732021285 - Protocol - ALOHA|ALOHA]]
	+ [[1732022695 - Protocol - CSMA|CSMA]]
		+ [[1732023041 - Protocol - Ethernet|Ethernet]] → Based on CSMA

+ **Taking turns:** Nodes take turns. The nodes with more data take longer turns.
***