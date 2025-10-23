This note contains a summary of what the STDOUT; STDIN, and STDERR are. Pipes and simple redirections: 

**Def:** A file descriptor is an indicator of a connection maintained by the kernel to perform I/O operations. 
Basic file descriptors: 
1. Data stream for input: [STDIN - 0](STDIN%20-%200.md) (code 0 when referring to it)
2. Data stream for output: [STDOUT - 1](STDOUT%20-%201.md) (code 1)
3. Data stream for errors: [STDERR - 2](STDERR%20-%202.md)

### Redirections: 
A redirection is when data is taken from a file and given into a program or from a program and put into a file. 
+ `>` Move the [STDOUT - 1](STDOUT%20-%201.md) or [STDERR - 2](STDERR%20-%202.md) into the provided file. To specify the FD use their codes prior to the redirector. 
+ `<` Use whatever is provided as [STDIN - 0](STDIN%20-%200.md) for the command
+ **Problem:** If we specify a file to move the STDOUT to, all its contents are deleted (without warning). We can use `>>` to append the contents to the file. 
+ To use as input all what is written in console we use `<<`. We use this along the End-Of-File (EOF) function. So that the terminal knows when to stop reading. 

Another way of redirecting is through the use of [Pipes](Pipes.md)


