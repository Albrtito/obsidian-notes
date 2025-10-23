### Insert: 
+ Insert new rows into the database
+ It can be specified the concrete variables in the table that need to be changed
#### Example: 
```sql
**insert into table values ("value1",value2,"Value3")**
insert into table(Variable1,Variable2) values ("value1","value2")
```

### Update: 
+ Update from a table all the values of one variable
#### Example: 
```sql
update table set variable = newvalue where variable = somevalue and variable2 = someOtherValue
```

### Delete: 
+ 