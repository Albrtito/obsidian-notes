### Check table data: 
Using the describe command we can see what properties a table has. 
```OracleSQL
describe tablename
```

+ Can be shortened to DESC
In order to see what are the actual entries of a table the **select** command can be used: 
```sql
select * from table
```
This command in this form selects and displays every entry of the table chosen
### Show all tables: 
```sql
show tables;
```

### ORACLE SQL: 
Oracle has the **user_tables** as a place to store all tables, this means that the following can be used. 
```sql 
select table_name from user_tables;
desc user_tables;
```
The same way that all tables are saved under that variable we can check both **user_tab_columns and user_constrains** 
#### Selecting a column: 
```sql
SELECT column_name, data_type, data_length, nullable FROM USER_TAB_COLUMNS WHERE table_name='tableName';
```
### Selecting constrains: 
```sql
SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE FROM USER_CONSTRAINTS WHERE table_name='referencing’;
```
Constraint types are the following: 
+ C: Check 
+ P: Primary K
+ U: Unique
+ R: Referential : **This is the foreign key**
+ V: View's CO
+ O: view's RO