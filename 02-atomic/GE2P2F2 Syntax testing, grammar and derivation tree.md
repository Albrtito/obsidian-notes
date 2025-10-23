# Grammar: 

```
File ::= StartObj Data EndObj
StartObj ::= {
EndObj ::= }
Data ::= Field1 Separator Field2
Field1 ::= Data_Label1 Equality Data_Value1
Field2: ::= Data_Label2 Equality Data_Label2
Equality ::= =
Separator::= ,
Data_Label1 ::= Quotes tag_Value1 Quotes
tag_Value1 ::= Localizer
Data_Value1 ::= Quotes Value1 Quotes
Value1 ::= a|b|c|d|e|f|0|1|...|9| {32}
Quotes = "
Data_Label2 ::= Quotes Tag_Value2 Quotes
Tag_Value2 ::= IdCard
Data_Value2 ::= Quotes Value2 Quotes
Value2 ::= 0-9 {8} a-z {1}

```

# Derivation tree 

![Pasted image 20240401143908](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240401143908.png)
![Pasted image 20240401144301](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240401144301.png)

Numbered derivation tree: 
![Pasted image 20240401144739](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240401144739.png)
![Pasted image 20240401181326](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240401181326.png)
#  
