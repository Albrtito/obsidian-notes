---
id: 1741617249 - File structures
aliases:
  - What is a file?
tags:
  - filesAndDB
---
# What is a file? 

> [!example] Dictionary: 
> + **Record**: A record is a bunch of bytes together
> + **Expanded record:** When the logical record is larger than one block
> + **Blocking:** When the block is larger than the record. 
>   > One block may have several records
> + **Blocking factor:** How many logical records fit in a row. 
> + **FMS**: File Management System
>

> [!NOTE] Intro:
> A file is basically a bunch of bytes together, the difficult part is how to group and call those bytes.
> File bytes are packed into records, which are **block sequences**. 
> When an user whants to operate on a byte the FMS looks for the block that contains that byte and then performs that operation.
> * This means that we allways need the block to operate on a single byte in any form

### Up
- [[Files&DB]]
### Down
- [[1748247290-records-blocks-and-buckets|Records, blocks and buckets]]








***
