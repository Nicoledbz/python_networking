from sqlite3 import connect
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

output = net_connect.send_command("show ip arp")
print(output)