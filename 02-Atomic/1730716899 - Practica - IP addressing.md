---
aliases:
  - IP Address Assignment
  - Practica - IP Addressing
tags:
  - net
References: 
cssclasses:
---
# IP Address Assignment - Branch 75 

> Author: Alberto Pascau Sáez 

## 1. Network Requirements 
### 1.1 Global network properties:
- Enterprise network range: 10.0.0.0/16
- Backbone network range: 10.0.0.0/24
- Branch network range: 10.0.75.0/24 (Using 75 as X value from the NIA 100495775)

### 1.2 Requirements for the branched network:

1. Office 1: 120 terminal devices
2. Office 2: 27 terminal devices
3. Server Room: 12 hosts
   
**Note:** The range used for this subnets **will be the minimal necessary one.**

4. Point-to-point connections between:
   + Backbone Router - Server Router
   + Server Router  -  Office 1 Router
   - Server Router  -  Office 2 Router
   - Office 1 Router - Office 2 Router

## 2. Network Address Assignment

### 2.1 LAN Networks (Ordered by size)

1. **Office 1 Network** (Needs 120 hosts, 128 possible addresses are given)
   - Network: 10.0.75.0/25
   - Usable range: 10.0.75.1 - 10.0.75.126
   - Broadcast: 10.0.75.127
   - Router interface: 10.0.75.1

2. **Office 2 Network** (Needs 27 hosts)
   - Network: 10.0.75.128/27
   - Usable range: 10.0.75.129 - 10.0.75.158
   - Broadcast: 10.0.75.159
   - Router interface: 10.0.75.129

3. **Server Network** (Needs 12 hosts)
   - Network: 10.0.75.160/28
   - Usable range: 10.0.75.161 - 10.0.75.174
   - Broadcast: 10.0.75.175
   - Router interface: 10.0.75.161

### 2.2 Connections between routers:

1. **Backbone Router - Server Router*. 
   - Network: 10.0.75.252/30
   - Backbone Router: 10.0.75.253
   - Server Router: 10.0.75.254

3. **Server Router -  Office 1 Router**
   - Network: 10.0.75.248/30
   - Server Router: 10.0.75.249
   - Office 1 Router: 10.0.75.250

4. **Server Router  - Office 2 Router**
   - Network: 10.0.75.244/30
   - Server Router: 10.0.75.245
   - Office 2 Router: 10.0.75.246

5. **Office 1 Router -  Office 2 Router**
   - Network: 10.0.75.240/30
   - Office 1 Router: 10.0.75.241
   - Office 2 Router: 10.0.75.242


## 3. Network Topology Design

+ [[1730713851 - Practica - Addressing Exercise - Topology Design#Diagram]]

![[IP Addressing and Routing Schemej-1.png|center|600]]
## 4. Routing Tables

### 4.1 Backbone Router (R_BB)

| Destination Network | Next Hop    | Interface |
| ------------------- | ----------- | --------- |
| 10.0.75.0/25        | 10.0.75.254 |           |
| 10.0.75.128/27      | 10.0.75.254 |           |
| 10.0.75.160/28      | 10.0.75.254 |           |

### 4.2 Server Router (R_S)

| Destination Network | Next Hop    | Interface |
| ------------------- | ----------- | --------- |
| 10.0.75.0/25        | 10.0.75.250 |           |
| 10.0.75.128/27      | 10.0.75.246 |           |
| 10.0.75.161         | Servers     |           |

### 4.3 Office 1 Router (R_O1)

| Destination Network | Next Hop    | Interface |
| ------------------- | ----------- | --------- |
| 10.0.75.128/27      | 10.0.75.242 |           |
| 10.0.75.160/28      | 10.0.75.249 |           |
| 10.0.75.1           | Office 1    |           |


### 4.4 Office 2 Router (R_O2)

| Destination Network | Next Hop    | Interface |
| ------------------- | ----------- | --------- |
| 10.0.75.0/25        | 10.0.75.241 |           |
| 10.0.75.160/28      | 10.0.75.245 |           |
| 10.0.75.129         | Office 2    |           |

***