---
aliases:
- generating a GPG key
tags:
- 
---
# generating a GPG key
> [!NOTE] Intro: 
> How to create a GPG signing key

We'll be using the Open GPG command `gpg`.  
```bash
gpg --quick-generate-key "Name Surname <my.mail@example.com>" rsa4096 default 1y
```
where: 
- The key is created with 1year expiration. **Don't have infinite keys, infinite time means it can be broken**


Now for sharing the key as ASCII text we need to export it with the `--armor` flag. 
```bash
gpg --export --armor KEY > public-key.asc
```
***
### Up
### Down
- [[1759344682-whyhaveagpgkey|why have a gpg key]]
- https://www.monperrus.net/martin/protocol-developer-gpg-key
***
