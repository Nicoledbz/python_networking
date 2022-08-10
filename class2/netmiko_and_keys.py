from netmiko import ConnectHandler

device1 = {
    "device_type": 'cisco_ios',
    "host": '192.168.1.222', 
    "username": 'Esther', 
    "use_keys": True,
    #"key_file": r'C:\Users\nicol\.ssh\known_hosts'
    #"key_file": r"C:\Users\nicol\AppData\Roaming\VanDyke\Config\KnownHosts\192.168.1.222[192.168.1.222]22.pub"
    "key_file": r"C:\Users\nicol\AppData\Roaming\VanDyke\Config\KnownHosts\HostKeyDB.txt"
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
net_connect.disconnect()