import json

#dict to json
person = {
    "name" : "kaung min khant",
    "age" : 21
}
j_person = json.dumps(person)
print(j_person)

x = '{"name" : "kaung Min Khant", "age" : 21}'
y = json.loads(x)
print(y)