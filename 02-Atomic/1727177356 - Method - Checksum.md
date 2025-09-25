---
aliases:
  - Method - Checksum
  - Checksum
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-02-22
sr-interval: 95
sr-ease: 270
---
# Method - Checksum
 
> [!NOTE] Definition: 
> The checksum is an **error detection method** used to detect bit errors within a message. 
+ The probability of an error varies as the checksum can be created such as it has the reliability required.
## Implementation:
1. Take groups of 16 bits form the message
2. Do a binary sum of the two 16bit numbers
	1. If the result is **17 bits** add the extra bit (to the left) to the remaining 16 bits. **Repeat this process until the number is 16 bits**
	   ![[1727177356 - Method - Checksumj.png]]
	2. If the result is 16 bits, add the next 16 bits to that result. 
3. Perform the 1’s complement
***