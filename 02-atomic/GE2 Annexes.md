---
aliases: 
tags:
  - softwareDev
"References:":
  - "[SoftwareDev_Resources_GE2_Annex](../00.References/SoftwareDev_Resources_GE2_Annex.pdf)"
DateCreated: 2024-03-29
---
# Used tools: 
+ **IDE:** PyCharm
+ **Package Management:** Automatically install update and configure software packages. [pip](pip.md) is the preferred manager.
+ **Code analyser:** [Pylint](Pylint.md). 
	+ We'll use [PEP8](PEP8_%20https://www.python.org/dev/peps/pep-0008/) standard. One of the most used guides
	+ Pylint runs integrated in PyCharm
+ **Git:** Version control to work on; for more info see [Git](Git.md)
	+ Create a .gitignore file and **UNCOMMENT THE .IDEA** we need venv and .idea as ignored directories. 
	+ A README.md file is also created in order to explain project documentation
 ![Virtual Environment (venv)](venv)).md)
## Dealing with the virtual environment: 
+ gitignore is really important
	+ It must be on the root dir of the project
	+ Comments with # 
	+ Wildcard characters are accepted

In order to configure a virtual environment in another machine that works with the code that has been developed it is useful to use the **freeze** library with pip and get the output of the command into a requirements.txt document. This way anyone knows what it's needed and can later install all the requirements.

```bash
# To obtain the requirements
pip freeze > requirements.txt

# To install the requirements
pip install -r requirements.txt

```


# Steps to establish a coding regulation: 

## Organisation of files:
### Source code files: 
Standard with the copyright legend
+ A comment with something such as the date, author and developers (or more things if it seems useful)
Files are managed through github

### Class files: 
+ A standard should establish whether a separate file is used for each class. Consider the name of those files
+ Standard: Class names contain a header or provide some info?

## Names and variables
### Classes and Members of Classes: 
+ Naming of classes
+ Naming of interfaces
+ Naming of data types
+ Naming of fields
+ Naming of methods
+ Naming of properties and constants

### Visibility: 
+ Establish whether a property can be public or needs to be private 
+ How should the source code be formatted
+ Where to initialise the fields or variables. 
+ Consider if the index for a for loop must be initialise or not 
+ Add **this** as a keyword inside classes

## Standard for methods: 
### Method structure: 
+ Do we have a máximum size for methods? Comments and logical blocks on methods
### Indentation and braces: 
+ Type of indentation to apply
+ Recommendations on placing ',' in loops and sentences. 
### Method definitions 
+ How to declare parameters
+ Rules for description of a method

## Exception handling: 
+ How are the exceptions handled and the errors detected
+ Rules for dealing with methods with high possibilities of throwing an exception 
## Other standards: 
### Parameters splitting: 

## Standard for the application design: 
How to implement each of the patters and instructions for the use of the patters. 
**Include a PDF document named CodingStandard.pdf**
### Organisation of the CodingStandard.pdf.
+ Must be in the root directory of the project
+ Sections with each rule
+ Examples for each rule
+ If the rule can be implemented in pylint it has to be included or modified. 


# Modifying pylint configuration files: 

+ Screen shot before and after the modification
+ Every rule followed before commit