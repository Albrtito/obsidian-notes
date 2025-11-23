---
aliases:
  - PythonFiles
tags:
  - softwareDev
"References:": 
DateCreated: 2024-03-31
sr-due: 2024-04-21
sr-interval: 15
sr-ease: 290
---
# main instructions: 
Python can manage files as any other programming language, in order to open and alter files we use the following instructions:

## Open: 

```python 
open(file,mode = "", buffereing = -1, encoding = None, errors = None, newline = None, closefd = True, opener = None)
```

The possible **modes** in order to open are: 
![Pasted image 20240331165059](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240331165059.png)

It is recommended to use the **with statement** this goes as the following: 

```python 
# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')
```

```python
# file handling

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
	file.write('hello world')
finally:
	file.close()
```

Using with statement makes the code cleaner  as with with statement **the file is closed when the with statement is completed, even if an exception occurs**

+ If **not using with** remember to **close the file**

# Types of files: 

Python can manage a ton of filetypes, some of them: 

## Json
Json files are use to stored data in a serialise way. With python the conversion between python variables and the data in the Json files goes in the following way: 

### Reading and writing into a json: Load and dump.

#### Load: (Read)
**json.load** : Deserialises the contests of a Json into a python object. According to this table. 
![Pasted image 20240331172145](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240331172145.png)

Basic code learned in softwareDev to read: (Example)

```python 
try: 
	with open(file_store, "r", encoding = "utf-8", newline =
	"") as file: 
		data_list = json.load(file)
except: FileNotFoundError as ex: 
	data_list = []
except json.JSONDecodeError as ex:
	raise HotelManagementException("JSON Decode Error- Wrong
	JSON Format")
	

```
+ If the files does not exist raise an error
+ If the Json cannot be properly decoded raise an error
+ **See that is not always useful to raise an exception when an error occurs** in this example if the json is not there, just output an empty list.

#### Dump(write)
**json.dump** : Serialises the contents of a python object and converts it into a json formatted string according to this table: 
![Pasted image 20240331172158](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240331172158.png)

The following code example can be used as reference: 
```python
try: 
	with open(file_store, "w", encoding = "utf-8", newline =
	"") as file:
		json.dump(data_list,file,indent = 2)
	
except FileNotFounderror as ex:
	raise HotelManagementExceptio("Wrong file or file path")
```
+ **Remark:** The indent can be changed, so if working with tab = 4 spaces maybe indent should be 4.

### Check for existence and add data or create: 

### Deleting Json files: 
We'll need the operating system to perform the deletion of the file, import os for it. We'll also be using pathlib, a python library to collect the path value of our home directory. 

```python 
import os
from pathlib import path
# Get the path of where the Json files are stored
JSON_FILES_PATH = str(Path.home()) `"/PycharmProjects/..../src/JsonFiles"

#Look for a particular json file
file_store = JSON_FILES_PATH + "store_patient.json"
# check if the file actuallyexist
if os.path.isfile(file_store):
	os.remove(file_store)

```

+ Using the pathlib library makes it so that the code can work on any computer as the path will be the relative one to the project root. (not the one stored from ur computer)