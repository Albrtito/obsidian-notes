---
aliases:
  - Input port processing in routers
  - Input port processing
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-11-30
sr-interval: 8
sr-ease: 251
---
# Input port processing:
Input ports must do the following actions, we’ll discuss each one of them below:

1. Lookup into the forwarding tables and send the packet into the switching fabric to the output port. This lookup is usually denoted as the abstraction **match plus action**
2. Physical and link layer processing.
3. Rewrite the packets header information
4. Update counters for network management.

## Lookup:
+ Iput port processing solves the centralised processing botleneck in lookup by **copying the forwarding tables into each one of the input ports.** We call this process the [[1731419106 - Match-Plus-Action methods in forwarding|Match-Plus-Action ]]


![[1730624725 - Routerj.png|center|500]]



***