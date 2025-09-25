---
aliases:
  - Types of switching fabrics
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-03
sr-interval: 11
sr-ease: 288
---
# Types of switching fabrics
![[Screenshot 2024-11-03 at 5.17.05 PM.png|center]]
In order for the input ports to send data into the output ports a conection between both of them is needed. 
This connection is called a switching fabric as it **switches (forwards) packets from input to output**. There are several ways of creating switching fabrics based on the hardware used. 

+ **Memory switching:** As in any common computer, the CPU (router’s processor) copies the packages into the memory and then back to the output buffer.
	+ Treats input/output ports as I-O  devices
+ **Bus switching:** Packets are sent over a bus. 
	+ Only one packet at a time, others wait
	+ Control headers added to distinguuish which port keeps each packet.
+ **Interconnection network:** A network inside the router. NxM (N: input ports, M: Output). 
	+ Still have the problem of two inputs into the same output!
***