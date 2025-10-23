---
aliases:
  - john the ripper
tags:
  - tool
  - cyber
---
# john the ripper
> [!NOTE] Intro: 
> John the ripper (john) is a hash password cracker. It takes a hash file and then starts hashing passwords until one the hash matches.
> - **github:**[john the ripper](https://github.com/openwall/john)
> 

It needs the hash, so usually first get the hash file (with root priviledges). In linux this means having access to the `\etc\shadow` file where the encripted passwords live. 
	
- One of the nice things is that it can **detect the hashing algorithm used automatically**
## install
**OSX**
It can be installed via Homebrew

```bash
brew install john
```
***
### Up
### Down
- [[1760051983-passwd|passwd]]
***
