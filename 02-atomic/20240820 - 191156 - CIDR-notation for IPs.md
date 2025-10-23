---
aliases:
  - CIDR notation
tags:
  - cyber
"References:": 
cssclasses:
---
# CIDR notation:
Notation used to define ranges or groups of ip addresses. 
+ See the following [medium article](https://medium.com/gitconnected/the-24-in-192-168-0-0-24-explained-in-30-seconds-b0ed6cb635c7) for a quick but throughout explanation
## Basics: 
The notation goes in the following way: 
``` Shell
192.168.0.0/<0-32>
```

This means: Take a number of ip addresses, starting with `192.168.0.`, equal to 32-<number> being <number> the number specified after the bar. 

**Let’s say we have `192.168.0.1/28`:**
Number of ip address = 2 ^ (32–28), which is 2 ^ 4 = 16
**The ip addresses are thus 192.168.0.0, 192.168.0.1, 192.168.0.2 … 192.168.0.15**

