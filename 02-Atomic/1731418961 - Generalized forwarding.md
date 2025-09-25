---
aliases:
  - Generalized forwarding
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-02-03
sr-interval: 57
sr-ease: 270
---
# Generalized forwarding

> [!NOTE] Intro: 
>  Each node sees the final destination of the packet **along with a lot of other info** and decides where to send it based on an algorithm programmed into the router. 
>  
>  **Analogy:**
>  The cars that enter a roundabout not only tell the booth assistant where to go but also have some properties that allow them to use some exits or not (maybe older cars cannot use the fast highway). It can also happen that some cars are not allowed to used any of the exits.

+ In general, generalized forwarding is implemented along a **Software Defined Networking** controler, in charge of creating the Forwarding tables. 
+ Inside the routers the  [[1731419106 - Match-Plus-Action methods in forwarding#OpenFlow generalised forwarding|OpenFlow standard is used for the match-plus-action implementation]]



***