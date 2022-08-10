from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    "host": '192.168.1.222', 
    "username": 'Esther', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    "fast_cli": True, 
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip arp")
pprint(output)
net_connect.disconnect()