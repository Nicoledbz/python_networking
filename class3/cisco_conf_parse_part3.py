from ciscoconfparse import CiscoConfParse

cisco_obj = CiscoConfParse(r"C:\Users\nicol\Documents\code\python\python_networking\class3\cisco1.txt")
print(cisco_obj)

 
parent = cisco_obj.find_objects(r"^line vty 0 4")
parent = parent[0]

print(parent.is_parent)
print(parent.children)

children = parent.children
print(children[1])

a_child = children[1]
print(a_child.siblings)

# py -i cisco_conf_parse_part1.py
# dir(cisco_obj)
# help(cisco_obj.find_objects)
# help(cisco_obj.find_objects_w_child)