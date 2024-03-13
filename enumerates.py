first_list = []
first_list.insert(0,1)
first_list.insert(-1,2)

second_list = []
second_list.append(3)
second_list.append(4)

third_list = []

person_one_dic = {
    "first_name": "hussein",
    "last_name": "taherian",
    "gender": "Male",
    "age": 35 ,
    "active": True,
    "email": "husseinTaherian67@gmail.com"
}
person_two_dic = {
    "first_name": "aida",
    "last_name": "Vahabi",
    "gender": "Female",
    "age": 30 ,
    "active": False,
    "email": "aidaVahabi72@gmail.com"
}
third_list.append(person_one_dic)
third_list.insert(1,person_two_dic)

forth_list = ["hussein","alireza","aida","sepideh","john","kenna","alison","harrison","alice"]
print(first_list)
print("**************************")
print(second_list)
print("**************************")
print(third_list)
for item in first_list : 
    print(item)

for item in second_list : 
    print(item)

for person in third_list:
    if(person["active"] == True) : 
        print(person)

for person in third_list :
    if(person["age"] >= 30) :
        print(person)
total_name = 0
for name in forth_list : 
    if(name.startswith('a')) : 
        total_name += 1
        print(name)
        forth_list.pop(forth_list.index(name))

print(total_name)
print(forth_list)

for key,val in person_one_dic.items() :
    print(f"{key} : {val}")

for item in third_list :
    for key,val in item.items() :
        print(f" {key} : {val}")