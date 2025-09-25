---
aliases:
  - Unittest
tags:
  - softwareDev
"References:": 
DateCreated: 2024-03-31
sr-due: 2024-04-05
sr-interval: 3
sr-ease: 252
---
# Intro: 
+ Built-in tool in IDE's such as PyCharm
+ Default testing tool in PyCharm

# IDE's
+ [PyCharm Unittesting](PyCharm%20Unittesting.md)

# Detecting and solving problems and challenges: 
## Time differences and testing time values: 
When using some data the time values may not work with the system current time, this means that even though the data is correct, it is older or won't work on the current date. 
By using the [Freezegun](Freezegun.md) library we can freeze time so that all methods that should output the current date and time output the one specified.