---
Date: 2024-02-27
tags:
  - softwareDev
"References:": 
aliases:
  - TDD
---
# Intro:
Test driven development or TDD is a programming framework for creating code based on test specified from requirements.The main idea of TDD is: 

1. First create test from requirements.
2. Write code to fulfil one test at a time. 
3. Once the test is passed move on to the next test. (repeat to step 2)
4. If all test are passed, ur finished and have developed the requirements. (next steps would be refactoring)
This framework is something we’ll see in more concepts such as refactoring. Once something work we can do something on top of it, however we cannot improve and keep building until everything that we have already build is done. 


But how can we create those tests? What method should we follow for test creation? Right now we have only said that the requirements must be met, but what does that mean. It greatly depends on the type of testing we are performing.

# Testing levels: 
There are several different reasons why we can do testing: 
## Acceptance testing: 
Acceptance testing is performed so that the **client can assess if the product is to their liking. (requirements are met)** 
+ For the software development test we don’t really care about this
+ Software must work as they expected
+ Important to test this when developing (after all they are the ones that are gonna use it)
+ Try not to test the whole system but each change by itself

## System testing: 
Test **the whole system**. Check that everything together works. 
## Integration testing: 
Integration with the **environment where the system is going to be deployed**
There are two types of integration strategies, systems can be integrated in: 
+ **Top-Down integration**: High level modules testing first
+ **Bottom-up integration**: Low level modules are tested first. Integrate lastly the main program.

## Unit testing![Unit testing](20240501%20-%20123051%20-%20Unit%20testing.md)
# dis/Advantages:
+ Improving the QUALITY
+ Easier to understand and modify 
+ Creation of a documentation through test. 
+ Changes are made on versions, and each version works









