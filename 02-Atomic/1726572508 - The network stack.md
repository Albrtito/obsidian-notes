---
aliases:
  - The network stack
  - Network layers
tags:
  - net
References: "[[Net_References_s1_2.pdf]]"
cssclasses: 
sr-due: 2025-02-06
sr-interval: 79
sr-ease: 250
---
# The network stack: 

> [!NOTE] Why layers? 
>  In order to organise the whole network. Split the network into smaller chunks of info. → **Modularization**
+ The layers are called an stack **because they are implemented as such:** Last in first out 

![[1726572508 - The network stack.png|center]]


From bottom to top, each layer offers a different services:
## Layers:
They are **numbered from bottom to top:**

1. **Physical:** The actual things we can touch 
   >Hardware

2. [[1732018095 - The network link layer|Link Layer]]: Data transfer between **neighboring network elements**
   > Next connection that needs to be made.

3. [[1728386212 - The network layer|Network layer]]: Joining all the linked devices in the link layer (the glue to actually create the network).
   > Where is the connection going? Whole topology of the web.

4. [[1728038869 - Transport network layer|Transport layer]]: Processes talking to each other to transfer data. 
   >How is the info going to be encoded and transported

5. [[1726574469 - Application layer|Application layer]]: Supports network applications. 
   >Decodes the info given by transport.

### Implementations:
As previously defined, layers work as an stack. So if a message wants to be sent from the application layer of one host to another. 
+ **Numbering goes with repect to the layer**
>5. The message is created in the app layer. 
>4. The transport layer sees it, breaks it into chunks (Headers added)
>3. The network layer states the destination (Header added)
>2. The link layer adds a header
>1. Message goes through the physical layer.

> [!example] Definitions
>+ Some definitions: 
>	+ **Segment:** Message + 1 header → Packet of transport layer
>	+ **Datagram:** Message + 2 headers → Packet of Network layer
>	+ **Frame:** Message + 3 headers → Packet of the link layer

At the other end it goes in reverse: 

> 1. Through physical layer
> 2. Link sees that info is correct (check header)
> 3. Network checks that he is the correct recipient (check header)
> 4. Transpor layer decodes (check header)
> 5. App layer delivers to respective service 

## The IP hourglass: 
An interesting point to make is the impact that the IP protocol has over the whole internet. All layers have several protocols that could be implemented while **the network layer only has the IP protocol**. ![[1726572508 - The network stackj.png|center|300]]