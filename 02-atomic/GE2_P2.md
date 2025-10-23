---
aliases: 
tags:
  - softwareDev
"References:": 
DateCreated: 2024-03-29
---
For this second part the following will be developed: 
+ Include PyBuilder
+ Create function 1: Request hotel reservation
+ Create function 2: Arrival at the hotel
+ Create function 3: CheckOut

# Objectives of the practice: 
+ Practice collective code ownership
+ Practice driven development
+ Learn required tools of test driven development
+ Practice functional and structural testing techniques
## Goals: 
**Define, automate and execute tests** In order to check if the components developed work correctly
+ Automate the testing with [PyBuilder](PyBuilder.md)
+ Follow TDD (CREATE FIRST THE TEST, THEN THE CODE)

# Function 2: Arrival at the hotel
## Inputs: 
**JSON:** 
Json format: 
```Json
{ 
"Localizer":"<String having 32 hexadecimal characters>",
"IdCard": “<valid idCard>” 
 }
```
## Process: 
## HotelStay class: 
```python
 "alg" (String). Identify the algorithm used to sign the stay code. Its value should be 
 "SHA-256" for now, but in future releases, the component will allow other values. ○ 
 "typ" (String). Type of room. ○
"Localizer" (String). This value is the value of the locator described in HM-FR-01. ○ 
"idcard" (String): Valid ID of the person who made the reservation. ○ 
"arrival". Date and time of arrival at the hotel (UTC in timestamp format). The date (day, month, and year) must match the arrival date provided in the reservation. ○ 
"departure". Departure date (UTC in timestamp format). It will be calculated by adding the number of days of the reservation to the arrival date. ○ 
"room_key" (String). It will be the code that will identify the stay at the hotel and will be engraved on a card to, for example, associate restaurant expenses or open the room door. This code is calculated by encoding the above fields using "SHA-256". The text to be encoded has the following
```
## Outputs: 
+ SHA-String
+ File with processed stays
+ HotelManagementExceptions
## Interface: 
Given an input: **guest_arrival(input_file):** with the path of the file 
Output the string of the room key or an exception

## Help and tips for this exercise: 
+ Stored in [SoftwareDev_Resources_GE2_Presentation_Hands-onLab](../00.References/SoftwareDev_Resources_GE2_Presentation_Hands-onLab.pdf)

# Requirements: 
Requirements are explained and detailed in the [Kanban_GE2](Kanban_GE2.md) page. For each funcitonal requirement some inputs are defined. 
# To- Do: 
1. Always use the github repo
2. Configure the project with pybuilder
	1. requirements.txt
	2. Update .gitignore
3. TDD process: 
	1. First function test cases
	2. **Second function**  Test cases + Syntax Analysis. Complement with equivalence classes and boundary values. **Document in an excel file**
	3. Third function test cases
4. PDF document with all test cases for each funciton. 
	1. F1: Equivalence classes
	2. F1: Boundary values
	3. F2: Grammar
	4. F2: Derivation Tree
	5. F3: ControlFlowGraph
	6. Basic paths
	7. Good look for the document
5. Generation of a log report for all the test. 


---