#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

password = getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.172",
    "username": "admin",
    "password": password,
}

#source_file = r"C:\Users\nicol\Documents\code\python\python_networking\testx.txt"
source_file = "testx.txt"
dest_file = "testaa.txt"
direction = "get"
file_system = "bootflash:"

# create the netmiko SSH connection
ssh_conn = ConnectHandler(**nxos1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)
print(transfer_dict)