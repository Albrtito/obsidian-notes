---
aliases:
  - GE3
tags:
  - softwareDev
"References:":
  - "[SoftwareDev_Resources_GE3_Statement](../00.References/SoftwareDev_Resources_GE3_Statement.pdf)"
cssclasses:
---
# Intro: 
This exercise’s objective is to apply what has been learned about refactoring during the SoftwareDev classes. 

# Step 2: 

## 2.1 Refactoring cases: 
**Remark:** After every single refactoring a build must be made. No push must be made without a correct build. DO NOT START REFACTORING BEFORE UR SURE THAT THE SOURCE BUILDS. 

There are some refactoring cases that have been intentionally included in the code: 

+ **Mysterious names:** Solve it with **changeFunctionDeclaration** (to rename a function), **rename variable** to rename a variable and **renameField**. Usually this last two can be used directly with the rename
+ **Duplicated code**: 
	+ If there is the same code structure in more than one place → Unify those two structures
	+ Look carefully for differences (be careful)
	+ To change the duplicated code find and capture all duplicates
	+ If the same expression is repeated in two methods of the same class: Solve it by **extracting the function**
	+ If the expression is similar but not identical: Solve it with **slide statements**. Organising the similar parts. 
	+ If the **duplicates are in subclasses** of a base class: Solve it by using **pull up method** . 
+ **Long functions:** Short = better. Long = hard to understand. 99% of the time, to shorten just extract a part. (divide the function into two parts)
+ **Divergent changes:** Solve it with: **Split phase and movement function** (to better understand divergent changes see the statement.) … 
+ **Large classes:** Try to **extract class**, if the inheritance makes sense **extract superclass** or **replace type code with subclasses(extract a subclass)**
+ **Comments:** There can be to many comments because the function is not well done. If a comment is needed to explain a function, in most cases the function will be to long: Use **change function declaration** to change the name. 
## 2.2 Code regulations: 
Make it so the code follows the established code regulation → This code regulation is the one given by Pylint (PEP8) (Already asked to the teacher)

## 2.3 - 2.4 Execution of the defined test cases and registration in GitHub: 
Test cases must be run, **at the end they must be satisfactory.** 
**Remark:** At the end of the project, get the xml output of the pyb into github. This output is inside the target/reports folder. (excluded for everyone so the last one to do a build puts it in)

## Usage of git: 
The best usage for this project is to **only have one main brach**. This is as such because all the files are interconnected between them and we cannot create separate workflow branches.


# Step 3: Simple design

# Step 4: Publications related to refactoring
Search in [google scholar](https://scholar.google.com) for an article related to refactoring (research on how refactoring has an impact on …). In a **word document**, include the reference for two articles that have been published in the last two years and a brief summary of the articles(one paragraph per article) with an **explanation to why the article is relevant.**: 
**reference format:**
+ Title, name of the journal or conference where it has been published, web address where to find it, authors and date of publication



# Step 5: Task to do
- [x] Create a git repo. Name it GXX.2024.TYY.EG3
- [x] Clone the project and include the code and folders structure in AulaGlobal
- [ ](#2.1%20Refactoring%20cases) . Detect where to apply and apply. 
- [ ] Make the code comply with PEP8 using pylint tool.
- [ ] Include the word document with the selected Publications
- [ ] Upload the refactored and redesigned code. Along with the test and reports generated before the last commit (xml format)

# Rules and procedures
At the delivery deadline the following must be in the github repo: 
+ Source code (refactored)
+ Code with the test (any adjustment made)
+ Report with the result of test execution. (in a folder named docs/test_reports)
# Class notes: 
During the lab we’ll see that some validations should not be moved, however a  lot of them will.We can define an specific class to validate the values of the attributes and create the corresponding methods inside of that class. To create this class we’ll use extract class. 

Really important to execute the tests after each change. 

next week we’ll have the fourth theory test, related to structural test.


2024-04-11 - 18:20
For checking attributes, the best thing is to create a class attribute, this class attribute has a method to check the attribute. Then we can create subclasses that check each of the possible attributes. 

Remember, when creating a subcclass _validate, first thing, do the super()._validate(attr_value).

  

For storage we can also create a new class: JsonStore(). This class has all the save_reservation, save_checkin and save_checkout  functions. This where involve with hotel manager and now need to be moved here. 

  

The code is in the slides, everything is in the slides. Applying refactoring techniques is just moving some code from place to place. It should not be needed to add new code.


**Remarks:**
+ For some unittest we’ll have to change the calls to the classes: First update the test, then after it fails, change the classes.
+ 

+ [Refactoring Presentation](20240411%20-%20173829%20-%20Refactoring%20Presentation)
+ 
