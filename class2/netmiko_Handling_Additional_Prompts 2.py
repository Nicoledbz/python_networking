from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": '192.168.1.222', 
    "username": 'Esther', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    #"session_log": 'my_session.txt' 
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'delete bootflash:nicole.txt'
output = net_connect.send_command_timing(command, 
                                  strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('nicole.txt',  
                                   strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('y', 
                                   strip_prompt=False, strip_command=False)                                   
print(output)