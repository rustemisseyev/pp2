import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")

print("=" * 80)

print(f"{'DN':<60} {'Description':<20} {'Speed':<10} {'MTU':<5}")

print("-" * 80)

for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]: # every imdata[i] is dictionary
            print(imdata[i][j]["dn"],"\t", "\t\t\t"  , imdata[i][j]["speed"] ,"\t\t" , imdata[i][j]["mtu"])