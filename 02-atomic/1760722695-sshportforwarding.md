---
aliases:
- ssh port forwarding
tags:
- 
---
# ssh port forwarding
> [!NOTE] Intro: 
> ssh port forwarding is used to directly connect one of the local hosts to another remote one thorough an ssh conection. 
```bash
ssh -L [local_port]:[destination_host]:[destination_port] user@ip
```
This means that whatever is send though the local port is then sent though ssh to the jumphost that forwards it to the target machine and same thing in reverse. 

***
### Up
### Down
***
