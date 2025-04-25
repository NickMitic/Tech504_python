import requests, json

json_body = json.dumps({"postcodes":["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type":"application/json"}

post_codes_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_codes_req.json()["result"])
