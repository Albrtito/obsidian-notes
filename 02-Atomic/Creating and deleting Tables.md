---
Date: 2024-02-22
tags:
  - filesAndDB
"References:":
---
### Before creating the table
 Have as little data as possible, ex: do not have age and birthdate

When writing relations we need to note what is done to each relation on delete nd on update ([Referential Integrity](Referential%20Integrity.md))
**Convention**: 
+ Names always  go in singular, the table will contain courses. But it's name will be course.
# Query:
```sql
CREATE TABLE table_name(
table_element type(),
table_element type(), 
...

CONSTRAINT ck_value CHECK(condition)
CONSTRAINT ck_value CHECK(condition)	
);
```
### Restrictions: 
Restrictions during the creation of tables are part of the simple [Semantic restrictions](Semantic%20restrictions.md) . They take the form in the last part of the query. And are such as:
```sql 
CONSTRAINT ck_value CHECK(condition)
CONSTRAINT ck_value CHECK(condition)	
````
#### Example:
```sql
CREATE TABLE Course ( 
subject VARCHAR2(100), 
degree VARCHAR2(50), 
credits NUMBER(2) NOT NULL, 
lecturer VARCHAR2(50), 
CONSTRAINT pk_course PRIMARY KEY(subject, degree),
CONSTRAINT valid_ttl CHECK (credits>0) );
```

max_size : 
+ or all but for text (it doesn't have one)
+ always use a bigger value

### Deleting tables: 
Using the drop command: 
```sql
drop table_name;
```


### Showing all the tables there are

```sql
select table_name from user_tables order by table_name ASC;
```

