from ciscoconfparse import CiscoConfParse

cisco_obj = CiscoConfParse(r"C:\Users\nicol\Documents\code\python\python_networking\class3\cisco1.txt")
print(cisco_obj)

my_config = """

interface GigabitEthernet1
 ip dhcp client client-id ascii cisco-5254.000f.f4a3-Gi1
 ip address 192.168.1.222 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet3
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
 """
print(CiscoConfParse(my_config.splitlines()))  
intf = cisco_obj.find_objects(r"^interface")

for child in intf[0].children:
    print(child.text)


# py -i cisco_conf_parse_part1.py
# dir(cisco_obj)
# help(cisco_obj.find_objects)