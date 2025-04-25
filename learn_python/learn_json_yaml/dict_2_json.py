import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

servers_json_string = json.dumps(servers_dict)

with open("servers_created.json", "w") as json_file:
    json_file.write(servers_json_string)

file = open("servers_created.json", "r")
json.load(file)
file.close()