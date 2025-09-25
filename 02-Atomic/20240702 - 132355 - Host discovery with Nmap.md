---
aliases:
  - Host discovery with Nmap
tags:
  - cyber
"References:":
  - "[[20240701 - 181920 - Nmap|Nmap]]"
cssclasses:
---
# Host discovery with nmap: 
Host discovery is the act of searching for online targets we can work with.

## Scan ranges: 
**By default Nmap uses the ICMP echo request** to search for active host, however before sending an ICMP request it tries with an **ARP request**. To ensure that the scan is being done with ICMP use the `--disable-arp-ping flag`. 


Most of these scans disable the port scanning (-sn) this is because we don’t really care about the state of each port, only if the machine is online. 
### Scanning the network range:
Used to see which hosts are active inside a network.
```shell
sudo nmap <IP-range> -sn -oA <fileName> | grep for | cut -d" " -f5
```
+ The grep and cut commands are used to simplify the output. 
+ If the target firewalls don’t allow the scan it wont work
### Scanning multiple addresses: 
+ Use the `-iL <filePath>` flag to input a list of target hosts.
+ The notation `<address>.<number-number>`can be used to define multiple targets. 
	+ **f.e:** `192.168.0.18-20` defines 192.168.0.18, 192.168.0.19,192.168.0.20. 
## Single IP:
First use a basic scan to know if it is active: 
```shell
sudo nmap <targetIP> -sn -oA host 
```

**Then:**
+ To force the scan with ICMP: `-PE` and `--disable-arp-ping` 

Once we find if the target is alive we can proceed to perform a port scan: [[20240820 - 201355 - Port scanning with Nmap|Port scanning with Nmap]]