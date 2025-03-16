import json
"""
json format bicimi
{
    name : Ahmet,
    age : 30,
    job:Job
}   
"""

data = {
    "name" : "Ahmet",
    "age" : "30",
    "job" : "Engineer"
}

json_to_string = json.dumps(data)

print(data,type(data))
print(json_to_string,type(json_to_string))

with open("persons.json","a") as fd:
    fd.write(json_to_string)

data = json.loads(json_to_string)
print(data,type(data))

with open("persons2.json","w") as fd:
    json.dump(data,fd)

with open("persons2.json","r") as fd:
    data2 = json.load(fd)

print(data2, type(data2))
