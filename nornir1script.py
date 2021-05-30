from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result                          # nornir_utils is a must to print


                                                                                 #https://github.com/ktbyers/nornir_netmiko/tree/master/nornir_netmiko/tasks
  nr123 = InitNornir(config.yml)
  output123 = nr123.run(netmiko_Send_command, command_string = "show ip int br")
  print_result(output123)
