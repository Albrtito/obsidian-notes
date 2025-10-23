---
aliases: 
tags:
  - softwareDev
"References:":
  - "[pip](pip.md)"
  - https://pypi.org/project/freezegun/
DateCreated: 2024-03-31
---
# Intro: 
**Problem to solve** we cannot expect some value with a time that's changing

Freezegun is a python package  used to set a time for test and prevent them from having different outputs based on the current time. 

It mocks the time methods of python so that they all return the time u have set.

