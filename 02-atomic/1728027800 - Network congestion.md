---
aliases:
  - Network congestion
  - Congestion control
tags:
  - net
  - incomplete
References: 
cssclasses: 
sr-due: 2024-10-05
---
# Network congestion

## TCP Congestion control: AIMD
We can use the number of packets (n) sent in a window to control the flow sent into the network. **Change the flow of the packets to control congestions**

For this we need to pieces: 
1. **A congestion signal:** A way of telling the sender there has been a congestion
   We can know this by **looking at the RTT**, this is because the only delay that can change is the **queueing delay** → Congestion. 
   We can also use **packet loses**, it is easier altough most mechanisms are complex and use the RTT.
2. **A way of changing the flow:** Just change the size of the window

We’ll use packet losses and apply the AIMD method:

> [!attention] IDEA: 
> We aim to create congestion until we create the congestion, this way we can reach better average time. 
> AIMD: 
> + **A**ditive **I**ncrease
> + **M**ultiplicative **D**ecrease: 
> 	We dont only want to decrease the flow, we also **need to drain the buffer** 

+ **Base case:** Lets start with the basic cases: Once we sent a window of n we get n acks, the: 
1. We can send again the **same number of packets** 
2. We can send an **increased amount of packets** → We’ll do this so that if later we reach a congestion it is with a bigger amount of packets.
+ **Packets lost cases:** If we dont get the acks → **Packet loses**
1. Send a lot of less packets, not only to decrease the flow but enougth to **drain the buffers**. → Divide the window by 2. (Cut it in half)

**Remarks:**
+ Congestion will be detected once we experienced the **first loss**. We then save the value of where we congested. 
+ We keep on going until we congest over and over agan because we **need to explore the network and it’s capabilities.** It can change over time.
### Slow start: 

**What to do when starting a new flow?:** 
1. We can start really conservative, **start with a window of 1**.
   But one is to little, we’ll be incrementing for forever
2. Estimate an RTT based on the speed of the link we have. 
   But this is to much, se can disturb other users. 
**Solution:** We’ll perform an exponential incrementation. Start with 1 packet and double it each time. 1-2-4-8 -..-. We call this method **slow start**

In order to **optimize** this approach we’ll use the value of 
+ `cwnd` → Change window

1. Once we achieve congestion: 
	+ Set the value for `cwnd` to half it’s value. (Window cut in half)
	+ Set a new value: `ssthresh` as **half the value of**  `cwnd`(The value it had before cutting it in half)
	  
2. Next time we begin with an slow start, we’ll use an **exponential increase until ssthresh**, **then start growing linearly**

### Detection of the packet loss:

We an detect loss packets in two different ways, one of them is by **duplicate acks** and the other is **packet timeouts**. We’ll react differently in each case:

+ **Duplicated acks:** We’ll half the window, multiplicative decrease
+ **Pakcet timeouts:** We’ll **start again with an slow start**


### FSM:
![[Screenshot 2024-10-04 at 10.22.44 AM.png]]
### Challenging the window assumption | Fast recovery: 
Once we start recieving duplicate acknowledgments we **are no longer representing with our window the load that is being imposed to the network.** 

**Solution:** We’ll artifitialy increment the window size when recieving a duplicated ack. **But we’ll only do this once we have recieved 3 duplicated acks**. 

## TCP Tahoe:
+ Goest to window size 1 when 3 dup acks.
+ 
***
