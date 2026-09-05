import json
from werkzeug.security import check_password_hash

with open("config.json") as json_file:
    params = json.load(json_file)["params"]

password = input("Enter your admin password: ")

print()
print("Username:", params["admin_user"])
print("Hash type:", params["admin_password"].split(":")[0])
print("Hash length:", len(params["admin_password"]))
print("Hash pass:", params["admin_password"])

result = check_password_hash(
    params["admin_password"],
    password
)

print("PASSWORD MATCH:", result)