import json

with open("servers.json", 'r') as file:
    json_srt = file.read()
    # read() method loads file contents as a string

servers = json.loads(json_srt)
# json.loads() converts valid json string to dict

print(type(servers),"\n")
print(servers["server1"],"\n")
print(servers["server2"],"\n")
for key in servers:
    print(f"Key and value: '{key}' = '{servers[key]}'")
    for subkey in servers[key]:
        print(f"\tRecord key and sub value: '{subkey}' = '{servers[key][subkey]}'")
