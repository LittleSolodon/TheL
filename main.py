import json
print("hello world")

print("тут я чето поменял в мейне")

with open("nothing here.json", 'r', encoding='utf-8') as file:
    print(json.loads(file.read()))