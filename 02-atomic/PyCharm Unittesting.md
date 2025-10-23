---
aliases: 
tags:
  - softwareDev
"References:": 
DateCreated: 2024-03-31
---
In order to run tests with unittest  in pycharm the method **assert** is used in the following way: 

```python 
assert(condition)

```

If the condition is met then no error appears else an assertion error is shown. 

# Class definition and structure: 
Unittest based classes must have the following structure: 
+ Inheritance from the unittest.TestCase class
+ Use assertion methods defined in the unittest.TestCase, the following methods are given: 

![Pasted image 20240331145020](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240331145020.png)

The structure for **each of the test classes** is the following: 
This structure is an example. The importance lays in the assert and inheritance

```python
import unittest
class TestclassExample(unittest.Testcase): 
	def test_method1(self):
		self.assertEqual(variable,value)
	def test_method2(self): 
		self.assertTrue(function())

```

## Generation of structure: 
In pycharm the structure for the unittest class can be directly generated with the generate function of the IDE. 
+  This function is under the code menu. 
+ As of today I don't really know how to use this function. 