import yaml

filename = input("enter filename: ")
with open(filename, "r") as f:
    yaml_out = yaml.safe_load(f)
print(yaml_out[0])

# test1.yml