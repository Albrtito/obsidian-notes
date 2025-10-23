---
aliases: 
tags:
  - softwareDev
"References:": 
DateCreated: 2024-03-29
---
****# Intro: 
A virtual environment is a mechanism that allows managing **isolated spaces** for different python programs and packages.
Is like having the whole python in one single folder. When building a project that will be later shared it is needed for all the users to be able to use all the capabilities. This means we cannot depend on anything external to the folder we are currently working on. 
+ Scripts are isolated

==it is important to notice that the virtual environment cannot be shared as it contains specifications for each computer== 
## What is it? 
+ A directory tree that contains: 
	+ Python executable
	+ Scripts
	+ Libraries
	+ Config files 

# Moving between machines: 
Using [[pip freeze]]