import json

imdata = """{
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]"
                 }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]"
                }
            }
        }
    ]
}"""

print("Interface Status")
print("=" * 50)
print(f"{"DN":<50} {"Description"}")
print("-" * 50)

data = json.loads(imdata)

for i  in data["imdata"]:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    print(dn)
