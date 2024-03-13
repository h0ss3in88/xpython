from classes import Manager,Employee
import json
import os 


employees_path = "files/employees.json"
manager_file_path = "files/info.txt"
variables = {}
info_file = open(manager_file_path,'r')
for line in info_file : 
    x = line.split(":")
    key = x[0]
    value = x[1]
    variables[key.strip()] = value.strip()

print(variables.get("first_name"))
print(variables["last_name"])
print(variables)
social_medias = variables["social_medias"].split(",")
manager = Manager(variables["first_name"],variables["last_name"],variables["age"], variables["email"], variables["hire_date"],social_medias,variables["salary"])
manager.activeOrInActive(True)

if(os.path.exists(employees_path)) :
    with open(employees_path) as f :
        employees = json.load(f)
        for employee in employees : 
            print(employee.get("first_name"))
            print(employee.get("active"))

manager.addEmployees(employees)
print(f"Manager : {manager.fullName()} is active from {manager.hire_date} with annual salary of ${manager.salary} and {manager.getEmployeeCount()} employees")

