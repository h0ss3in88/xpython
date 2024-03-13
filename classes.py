class Person :
    def __init__(self, fname, lname, age, email,social_medias = ["" for x in range(7)]) -> None:
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.email = email
        self.social_medias = social_medias
        self.active = False
    def changeEmail(self, email) :
        self.email = email
    def fullName(self) -> str: 
        return self.first_name + " " + self.last_name
    def _get_social_medias(self) :
        return len(self.social_medias)
    def activeOrInActive(self, active) : 
        self.active = active
class Employee(Person) : 
    def __init__(self, fname, lname, age, email,hire_date, social_medias=["" for x in range(7)], salary = 0) -> None:
        super().__init__(fname, lname, age, email, social_medias)
        self.salary = salary
        self.hire_date = hire_date
def showInfo(person: Person) : 
    print(person.fullName())
    print("her/his social medias :" ,person._get_social_medias())
    if(hasattr(person,"salary")) :
        print(f"Employee Salary {person.salary}")
def init() :     
    fname = "Hussein"
    lname = "Taherian"
    age = 35
    email = "husseinTaherian@gmail.com"
    person = Person(fname,lname,age,email,["instagram.com/husseinTaherian","twitter.com/husseinTaherian","linkedIn.com/husseinTaherian"])
    showInfo(person= person)
    new_employee = Employee("Alireza","taherian",24,"alireza2020taherian@gmail.com","2024-03-05",["instagram.com/ali1378","twitter.com/alirezaTaherian","telegram.me/ali1378"],1758907.00)
    showInfo(new_employee)
init()


class Manager(Employee): 
    def __init__(self, fname, lname, age, email, hire_date, social_medias=["" for x in range(7)], salary=0) -> None:
        super().__init__(fname, lname, age, email, hire_date, social_medias, salary)
        self.employees = []

    def addEmployees(self, employees) :
        self.employees = employees
        
    def addEmployee(self, employee: Employee) -> int :
        self.employees.append(employee)
        return len(self.employees)

    def removeEmployee(self, employee) -> int : 
        self.employees.remove(employee)
        return len(self.employees)
    
    def getEmployeeCount(self) :
        return len(self.employees)