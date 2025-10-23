---
id: 1748247290-records-blocks-and-buckets
aliases:
  - Records, blocks and buckets
tags:
  - #FilesAndDB
---

# Records, blocks and buckets
We put records into blocks and blocks into  buckets: 
$$
bucket > block > record
$$

## Records into blocks:
In order to group records blocks are created, one block can have several records:

+ If a record is larger than a block we call it expanded
+ If a record fits into the block then we call that blocking

Because we want to do blocking we need to know how many records will fit into one block, we call this the **blocking factor**:

$$
f_b = \frac{S_{bk}}{Sr}
$$
+ $S_{bk}$: Size of the block
+ $S_r$ : Size of the record 

When records are put into blocks we have consecutive organization:
- **Consecutive organization**: We dont care when a block ends, we put records in between blocks if necesary. 

## Records and blocks into buckets:
Blocks save records, buckets save blocks. Buckets are used to save a lot of blocks and not only save raw data but also have reserved space for headers, operations, pointers, etc.

- Data inside the blocks of a bucket will be saved consecutivelly, but the blocks themselves will be stored in a non-consecutive way:
> [!NOTE] Def:
> **Non-Consecutive**: We only put data in if it'll fit inside the space left in the group
- Buckets have a a **max occupation(extent)** and **min occupation(space)**

**Remarks:**

- The groups of blocks that conform a bucket are more efficient when they belong to: ${2^n: \forall n \in N}$
> **Oracle:** Only lets us have buckets of $2^1$ to $2^4$ blocks. 
- A file is made out of some number of buckets
- A bucket size can be given out in blocks or bytes


As with blocks and the blocking factor, with buckets in order to know how many records can fit in a bucket we compute the **bucket extend**. 

- The size of records is still used instead of the one of blocks because the organization is non-consecutive. 
- We take the lower bound, we want whole records here

$$
\mathrm{BE}=\left\lfloor\frac{\mathrm{BS}}{\mathrm{~S}_{\mathrm{r}}}\right\rfloor
$$

- **BS** : Size of the bucket
+ $S_r$ : Size of the record 

But buckets are not just records, they have other data for control and reserved space for operations and management, because of this the bucket extend formula is adapted to:
$$
\mathbf{B E}=\left\lfloor\frac{\left(\mathbf{B S}-\mathbf{S}_{\mathrm{ctrl} \mathrm{inf}}\right) \cdot(1-d f s)}{\mathbf{S}_{\mathrm{rec}}}\right\rfloor
$$

