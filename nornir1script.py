from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result                          # nornir_utils is a must to print


                                                                                 #https://github.com/ktbyers/nornir_netmiko/tree/master/nornir_netmiko/tasks
  nr123 = InitNornir("config.yml")
  output123 = nr123.run(netmiko_Send_command, command_string = "show ip int br")
  print_result(output123)


  ########*******################
  
  from nornir_napalm.plugins.tasks import napalm_get,napalm_cli
  
  output123 = nr123.run(napalm_get, getters=["get_factts"])
  output123 = nr123.run(napalm_cli, commands=["show clock", "show ip int br", "show cdp nei"])
  print_result
  print_result(output123)
  
  
  ====> FOR PYNTC & NAPALM output will be in dictionary format
          in PYNTC it was converting output to strings 
  
  ===> FOR NETMIKO output will be cleaner as we could use  JSON
