Date: 2024-02-06
Class: #softwareDev 
References: [SoftwareDev_Resource_PairProgrammingGuide ](../00.References/SoftwareDev_Resource_PairProgrammingGuide%20.pdf)[StrengheningTheCaseForPairProgramming](https://doi.org/10.1109/52.854064)

---
# Pair programming: 

## What is it?
It's an agile technique that can be compared to rally racing as a pair of programmers (drivers) are coding together in the same machine. 
The way this works is by differencing a **driver** and an **observer**. 
**Driver:** Writes code
**Observer:** Checks for how to improve the code he's looking at.
+ Driver and observer switch role periodically
+ Pairing is dynamic: The pairs change
+ Experience of the driver and observer must be similar
+ If not working at the same time : 
	+ Part the work into the separate part, then **review** together


## Advantages & Disadvantages

**Advantages:**
+ No information is lost in case of one programmer leaving 
	+ For a changing pairs group, programmers leaving are less of a thread
+ **Fewer defects and FEWER ERRORS**, **QUALITY**, 
+ Detect easy all defects
+ if the communication work, great
+ Code is tested and reviewed more
+ Collective ownership of the code
+ Increases confidence and satisfaction of the programmer : Based on what?¿

**Dis:**
+ Code creation can be slower
+ Communication between members can really fuck up things
	+ Create some**test cases first**
+ The design must be simple
## Case study: 
+ [StrengheningTheCaseForPairProgramming](https://doi.org/10.1109/52.854064)
# Collective code ownership 
Means that the code belongs to several developers and all of them can make changes and share responsibilities.
## What is needed?
+ Work environment must be similar or equal
### Using a coding Standard
Guidelines for creating code
Rules 
+ Some must be met some are a must
**Correct, understandable, maintainable software**

+ [Python Standar: PEP-8](https://www.python.org/dev/peps/pep-0008/)
+ 


### Using a VCS
+ Use a version management system to share it all. -> Enter an initial explanation to GitHub
	+ Test are essential for pushing anything into the shared environment. 
**On push:**
+ **Coding standar**
+ **All test**
+ **Upload functional source code**
	+ New test cases, new code
+ Notify

### Summary
Highlight ==what’s important!==