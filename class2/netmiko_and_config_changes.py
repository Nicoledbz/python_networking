from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": '192.168.1.222', 
    "username": 'Esther', 
   # "password": getpass(),
    "password": 'Nicole123',
    "device_type": 'cisco_ios'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

cfg = [
    'logging buffered 20000',
    'no logging console',
    'clock timezone EST -5 0',
]
output = net_connect.send_config_set(cfg)
print(output)

net_connect.disconnect()