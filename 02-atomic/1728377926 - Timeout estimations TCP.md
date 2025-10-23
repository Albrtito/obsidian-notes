---
aliases:
  - Timeout Estimations TCP
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-01-01
sr-interval: 25
sr-ease: 190
---
# Timeout Estimations TCP
The TCP protocol asociates a timer  to the **oldest package being sent** (without a recieved ack), the value of this timer is what we call **TimeoutInterval** and it’s computed using the **RTT** or round time trip.

We’ll see in this note **how the value to the timer is set and computed**.

**Remarks:**
+ It is better to set a **longer RTT** because then we’ll only be waiting longer for packets that get lost or corrupted. This is why we **wont try to get an exact value for the RTT but we’ll try to make an overestimate**

### Estimation of the RTT:
Estimating based on the last sent package is a really bad idea because the **variabilty between packages is huge.** A best estimation will be: 

$$
\boxed{EstimatedRTT = (1-\alpha) \cdot EstimatedRTT + \alpha \cdot SampleRTT}
$$
+ $\alpha$ : A constant value
+ $EstimatedRTT$ : The previous estimated RTT 
+ $SampleRTT$ :The computed RTT of the last packet.

**Remarks:**
+ This formula makes it so the weight of one particular sample **decreases exponentialy over time**. 
+ We compute the average of the last n samples with a decreasing weight for each previous sample. 
+ The changes in alpha give out how much weight we give to previous samples. $\alpha = 0.125$ → Typical value

> [!BUG] Problem: 
>  However the estimation of the RTT is a bad value to use as actual RTT **because we are not overshooting**. 

> [!check] Solution: 
> Create the overshoot with a security margin using the **variance(deviation)** of the estimated value. 

$$
\boxed{DevRTT = (1-\beta)\cdot DevRTT + \beta|SampleRTT - EstimatedRTT|}
$$
+ **Remark:** The $EstimatedRTT$ here is the one **from the last Estimation (Not the one computed in this iteration)**
### Timeout interval: 
Using what we have just explained about RTT, we use that data to compute the timout intervals for timers sending the oldest package:

Finally, the gloval timeout interval will be: 
$$
\boxed{TimeoutInterval = EstimatedRTT + 4\cdot DevRTT}
$$
 
## ==Fast retransmit:== 

> [!BUG] Problem:
> Right now the protocol reacts with a large waiting time (4 times the deviation). If we send 4 packages and the second one is lost, then the reaction to send again the second package wont arrive until we have recieved the acks for all 4 packages (or not). 

We would like to ackt in one RTT time. In order to do so we’ll **only** **tolerate up to three duplicate acks**

> [!CHECK] Solution: 
>  
>Once we have recieved **more than three duplicated ack** we’ll assume that it is a loss package and retransmit right away. 



***
