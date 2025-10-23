---
aliases:
  - Equiv. test classes
tags:
  - softwareDev
"References:":
  - "[SoftwareDev_Resources_GE2_Presentation_Hands-onLab](../00.References/SoftwareDev_Resources_GE2_Presentation_Hands-onLab.pdf)"
DateCreated: 2024-03-31
sr-due: 2024-07-09
sr-interval: 69
sr-ease: 290
---

The TDD test creation method focuses on the creation of test prior to the development of the source code. This means that the source code is created in order to meet the test requirements. **The focus is given to the requirements and completion of them**

Then the process must be the following: 
1. Create a test corresponding to a test case
2. Build the code to pass the test (**only that piece of code**)

**Repeat this two steps for each case**
# Creating the test: 
## Equivalent classes: 
**STEP 1** : Before creating any test we must define all the possible equivalence classes and limit values. 

The following **notation** is proposed during the softwareDev course, although other notations may be used. 
+ **CEVn** : An identifying valid class(acronym: **c**lass **e**equivalence **v**alid. n represents the index)
+ **CENVn**:  An identifying **non** valid class(acronym: **c**lass **e**equivalence **n**on v**alid**. n represents the index)
+ The limit values involved in both types of classes obtain the names: **VLVn** and **VLNVn**
A table with all valid and non valid equivalence classes must be created
## Building the associated tests: 
Two main rules: 
+ **A test can group several valid classes**
+ **A test CANNOT GROUP several invalid classes, only covers ONE invalid class**
For each test created a table is done with the parameters for the test, the expected result and the test it is covering


