---
tags:
  - filesAndDB
---
Keeping with the idea of elements in sql and generalising commands. In order to make some changes in an element we use the amendment command: 
```sql 
alter <element> <name> 
{ADD|ALTER|DROP} <element> [<definition>];
```
+ Specify the element to alter
+ Specify the alteration
**f.e.**
```sql 
ALTER TABLE example ADD CONSTRAINT max_age CHECK (age<100);
```
