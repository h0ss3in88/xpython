import json
import os 
from datetime import datetime
import uuid
from faker import Faker

file_path = os.path.abspath("files/persons.json")
dict = [{
    "id" : str(uuid.uuid4()),
    "first_name" : "Hussein",
    "last_name" : "Taherian",
    "age" : 35,
    "email" : "husseinTaherian67@gmail.com",
    "active": True,
    "registered_at" : datetime.now().isoformat(),
    "updated_at" : datetime.now().isoformat()
},{
    "id" : str(uuid.uuid4()),
    "first_name" : "Alireza",
    "last_name" : "Taherian",
    "age" : 24,
    "email" : "alireza2020taherian@gmail.com",
    "active" : False,
    "registered_at" : datetime.now().isoformat(),
    "updated_at" : datetime.now().isoformat()
}]
fake = Faker()
for _ in range(100) :
    dict.append({
        "id" : str(uuid.uuid4()),
        "first_name" : fake.first_name(),
        "last_name" : fake.last_name(),
        "email" : fake.email(),
        "age" : fake.random.randint(25, 55),
        "active": True,
        "registered_at" : datetime.now().isoformat(),
        "updated_at" : datetime.now().isoformat()
    })
if os.path.exists(file_path) :
    f = open(file_path, "r+")
    f.truncate(0)

with open(file_path,"w") as outfile:
    json.dump(dict, outfile)


#  reading json file 
with open(file_path, "r") as file_reader :
    js_reader = json.load(file_reader)

print(len(js_reader))
print(type(js_reader))
for obj in js_reader : 
    print(f"name : {obj.get("first_name")} {obj.get("last_name")} \t  age {obj.get("age")} \t email : {obj.get("email")} \t registered at : {obj.get("registered_at")}")
    