---
aliases:
- ensemble base models
tags:
- review
- ms
References:
cssclasses:
---
# ensemble base models
> [!NOTE] Intro: 
> How can we train base models for ensemble methods? 
> Remeber we want them to be: 
> - Independent
> - Have a better error than a random choice model

 So the models could be train:
- Using different training data
	- [[1757410900-bagging|bagging]]
- Using different variables 
	 - Works good with variables with overlapping features
- Using different classes
	 - Transform the problem into a binary classification problem with one class only per classifier. (Each agent takes one class i and basically trains to say if a value is or not from class i)
- Creating different base models:
	- Use different classifier methods
	- Include some randomnes during model creation. Creating models using the same method but with some variable parameters. 




***
### Up
- [[1757407129-ensemblemethods|ensemble methods]]
### Down
- [[1757410900-bagging|bagging]]
***
