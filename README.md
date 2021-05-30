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


NORNIR INSTALLATION:
1.On LINUX:
  -pip install nornir
  -pip install nornir_napalm
  -pip install nornir_netmiko
  -pip install nornir_utils.  [all print functions, processors are on this]
  
  
  NORNIR FORLDER :
  -nornir_script.py.  {this will look for config file}
  -config.yml.      (this will point to locations of HOSTS/GROUPS/DEFAULTS )
  -host.yml
  -groups.yml
  -defaults.yml
  
  HOSTS --->will have ips
  GROUPS --->password will be here/If there is unique config specific to some boxes only.. 
  DEFAULTS--->passwords will be here {if there is same passowrd for 100s of devices}
  
  
  .py-->CONFIG----->HOSTS/GROUPS/DEFAULT
  
