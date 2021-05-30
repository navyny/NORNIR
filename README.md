# NORNIR

Sep 2020 --->Nornir 3.0 came out.  (previousy it was 2.0)
https://nornir.tech/nornir/plugins/

NORNIR can be run on:
1)Pycharm
2)Linux

NORNIR is only a framework...there is no trasnport
For transport we can use {netmiko,napalam,scrapli,Ansible,Netbox,Pramiko}

Nornir does nto have its own config...
...if we use NORNIR_NETMIKO......use .send_command

The advantage of using Nornir...is : PARALLEL CONNECTION
-->So instead of NETMIKO making 3 conenctions 1 after another--->
--We can use NORNIR-NETMIKO....All 3 conenctions can happen at same time parallelly...
NORNIR does multi-threading...i.e multiple connections 

