from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": '192.168.1.222', 
    "username": 'Esther', 
    "password": 'Nicole123',
    "device_type": 'cisco_ios'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_config_from_file(config_file=r'C:\Users\nicol\Documents\code\python\python_networking\config_file.txt')
print(output)

save_out = net_connect.save_config()
print(save_out)
