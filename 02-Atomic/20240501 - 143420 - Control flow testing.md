---
aliases:
  - Control flow testing
tags:
  - softwareDev
"References:": 
cssclasses: 
sr-due: 2024-09-25
sr-interval: 131
sr-ease: 290
---
## Control flow testing
Create a test for each execution path
### Control flow graphs
These graphs are the foundation of flow testing. A graph shows the control structure of the code. 
+ Each function has a graph 
+ Each module has a graph
+ Each method has a graph
Analysis of the graphs define the test cases.
#### Drawing the graphs: 
Easy: Everything is a circle, specify conditions inside of them. If some node represents an if write if inside of the circle. Two or more paths will branch from the node. 
**Example:**
	![Control Flow Graph Example](../99%20-%20Meta/0.%20Attachments/Control%20Flow%20Graph%20Example.png)
### Coverage levels
Coverage is defined as the percentage of the code that has been tested. Following levels are defined from less coverage (level 0) to max coverage( level 3)
1. **Level 0:**  Below 100% coverage. Test something, but not all of it
2. **Level 1:** Execute each of the nodes at least once
3. **Level 2:** Decision/Branch coverage. Check the true and false statement for each of the decisions
4. **Level 3:** Condition coverage. Check all possible combinations of conditions for all decision-making.

### Cyclomatic complexity: 
Used to measure number of possible linearly independent paths: 
+ [[20240619 - 141717 - Definition - Cyclomatic complexity|Cyclomatic complexity]]
+ 