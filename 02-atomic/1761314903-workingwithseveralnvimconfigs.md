---
aliases:
- working with several nvim configs
tags:
- dotfiles
---
# working with several nvim configs
> [!info] Intro: 
> Nvim is superexpandable, there are a ton of plugins and infinite different configs that cna be created with them. Everyone can have their own setup but also use some distros like lazyvim. How can I work with several of this configurations. Whether it is for something like changing configs for each filetype or just testing new setups? 
> The solution is in the `$NVIM_APPNAME` env variable. 
> 

Just create or download a new config within some directory inside the `$XDG_CONFIG_DIR`. Lets use `$XDG_CONFIG_DIR/testnv` as an example. Then by starting nvim with: 

```bash
NVIM_APPNAME=testnv nvim
```

We pointed nvim to the testnv config and it'll boot from there on.
We can just put this into an alias: 
```bash
alias testnv='NVIM_APPNAME=testnv nvim'
```

I'm using this to try some new nvim distributions such as [[1761179757-lazyvim|lazyvim]] without completely breaking mine. 

***
### Up
### Down
***