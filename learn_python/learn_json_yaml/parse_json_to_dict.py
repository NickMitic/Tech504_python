import json

with open("servers.json", 'r') as file:
    servers = json.load(file)

print(type(servers),"\n")
print(servers["server1"],"\n")
print(servers["server2"],"\n")
for key in servers:
    print(f"Key and value: '{key}' = '{servers[key]}'")
    for subkey in servers[key]:
        print(f"\tRecord key and sub value: '{subkey}' = '{servers[key][subkey]}'")
