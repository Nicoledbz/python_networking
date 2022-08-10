from netmiko import ConnectHandler
from getpass import getpass
import ntc_templates
from pprint import pprint

device1 = {
    "host": '192.168.1.222', 
    "username": 'Esther', 
   # "password": getpass(),
    "password": 'Nicole123',
    "device_type": 'cisco_ios'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief", use_textfsm=True)
pprint(output[-4]['ipaddr'])
output = net_connect.send_command("show ip arp", use_textfsm=True)
pprint(output[1])

net_connect.disconnect()