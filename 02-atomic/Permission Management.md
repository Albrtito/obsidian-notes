### Types and owners: 

For any file certain permissions are set, this permissions can be of three types: 

+ (r) - Read
+ (w) - Write
+ (x) - Execute 
	+ The execute permission let's the specified groups or users run the file. For directories, it is impossible to open a directory without the x permission over it. 

In order to see the permissions that a file has we can simply use the [ls](ls) command with the flag `-l` . 

```shell-session
cry0l1t3@htb[/htb]$ ls -l

drw-rw-r-- 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:30 scripts
```

There are three types of owners for a file's permissions. The **owner**, the **group**, and **others**.
+ Representation of permissions.
```shell-session
cry0l1t3@htb[/htb]$ ls -l /etc/passwd

- rwx rw- r--   1 root root 1641 May  4 23:42 /etc/passwd
- --- --- ---   |  |    |    |   |__________|
|  |   |   |    |  |    |    |        |_ Date
|  |   |   |    |  |    |    |__________ File Size
|  |   |   |    |  |    |_______________ Group
|  |   |   |    |  |____________________ User
|  |   |   |    |_______________________ Number of hard links
|  |   |   |_ Permission of others (read)
|  |   |_____ Permissions of the group (read, write)
|  |_________ Permissions of the owner (read, write, execute)
|____________ File type (- = File, d = Directory, l = Link, ... )
```

### Changing permissions and owners: 
+ In order to change the permission types of a file use the [chmod](chmod.md) command. 
+ In order to change the owner/s of a file use the [chown](chown) command. 
+ 