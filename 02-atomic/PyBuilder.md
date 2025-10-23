---
aliases: 
tags:
  - softwareDev
"References:":
  - "[SoftwareDev_Resources_GE2_Presentation_PyBuild_Unittest](../00.References/SoftwareDev_Resources_GE2_Presentation_PyBuild_Unittest.pdf)"
  - https://pybuilder.io/documentation/tutorial
DateCreated: 2024-03-31
---
# Intro:
PyBuilder is an automation python tool to release code. 
+ Official tutorial and page in references. This guide has a lot of info that hasn't been described in this note. This is because the description is really well explained and I saw no need to summarise
# Installation: 
Installation is done through [pip](pip.md)
```zsh
pip install pybuilder
```

Notice that during the installation the following folders must be added into the ignored git folders (if the project is saved in a repo)

==.pybuilder and target must be ignored in the .gitignore file==

If using some requirements.txt update them using [pip freeze](pip%20freeze) so that pybuilder is stored. 

The default command for pybuilder actions is **pyb**
# Config: 

To start a new pybuilder project we execute the command: 

```shell
pyb --start-project

```

+ After this execution mainly the project name will be changed, the rest of values depend on the specific project. 

After this the following files and folders appear int he project: 
+ build.py
+ pyproject.toml
+ setup.py
+ target: Folder containing logs and reports from the pybuilder. For example, if one of the builds does not work the log and report goes there. 
I have no idea what they're used for. 

Now in order to configure the pybuilder project we need to create the following file structure. 
- root
	- src
		- main
			- python
				- main.py

### For PyCharm:
Set it up such as src/main/python is sourced. 
![Pasted image 20240331153806](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240331153806.png)

# Adding test files: 
In order to add any test file remember that ==all tes files must have a name such as==

```
test_\<whatever>\_test.py
```

+ Without this naming convention pybuilder wont recognise shit. 

# Using pybuilder: 
In order to use pybuilder there is only one main command: 

```
pyb
```

This shell command tells pybuilder to build the project. This means executing all possible test and making sure that everything looks good. 
For projects during the SoftwareDev course, and possibly other future projects. Before making any push to git a correct build must be done to ensure no fails. 

## Solving errors: 
+ Logs and reports of the unittest are stored inside the /target folder. 
+ There must be a certain coverage for each piece of code. At least 70%. This coverage is computed with another python package. (see official page)