from netmiko import ConnectHandler
from my_devices import rtr3, rtr4

net_connect = ConnectHandler(**rtr3)
print(net_connect.find_prompt())