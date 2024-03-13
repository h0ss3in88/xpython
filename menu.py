import os
from colorama import Fore
from classes import Manager,Employee

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def subtractFunc() : 
    fNumber = int(input('please enter your first integer number \n'))
    lNumber = int(input('please enter your second integer number \n'))
    result = lNumber - fNumber
    print(result)
def sumFunc() :
        fNumber = int(input('please enter your first integer number \n'))
        lNumber = int(input('please enter your second integer number \n'))
        result = lNumber + fNumber
        print(f"{Fore.LIGHTCYAN_EX} sum of {fNumber} and {lNumber} is {result} + {Fore.WHITE}")
        input("for continue please press Enter ... \n")
        cls()
def divideFunc() :
        fNumber = float(input('please enter your first integer number \n'))
        lNumber = float(input('please enter your second integer number \n'))
        result = lNumber / fNumber
        print(result)        

def multiplyFunc() :
        fNumber = int(input('please enter your first integer number \n'))
        lNumber = int(input('please enter your second integer number \n'))
        result = lNumber * fNumber
        print(result)
def concatenatingFunc() : 
        fWord = input('please enter your first word \n')
        sWord = input('please enter your second word \n')
        result = f"{fWord} {sWord}";
        print(result)   
def workWithClasses() :
     print(" ---- Welcome To Classes Section ----")
     print(" ---- add new Manager ----")
     first_name = input("please enter manager's first name ")
     last_name = input("please enter manager's last name")
     age = int(input("please enter age of manager"))
     email = input("please enter email address of manager")
     social_medias = input("please enter social medias with , separation [instagram,twitter,tiktok, ...]").split(",")
     salary = float(input("enter salary for manager"))
     hire_date = input("please enter date of hire")

     manager = Manager(first_name,last_name,age,email,hire_date,social_medias,salary)

     print("---- Now Add One Employee who work for this manager ----")

     first_name = input("please enter employee's first name ")
     last_name = input("please enter employee's last name")
     age = int(input("please enter age of employee"))
     email = input("please enter email address of employee")
     social_medias = input("please enter social medias with , separation [instagram,twitter,tiktok, ...]").split(",")
     salary = float(input("enter salary for employee"))
     hire_date = input("please enter date of hire")
    
     employee = Employee(first_name,last_name,age,email,hire_date,social_medias,salary)
     manager.addEmployee(employee)

     print(f"{manager.fullName()} has {manager.getEmployeeCount()} employees")
     print(f"{manager.fullName()} employee's name is {manager.employees[0].fullName()}")
     input("for continue please press Enter ... \n")
     cls()
def showMenu() : 
    x = True
    while x == True : 
        i = 0
        print('1- subtract two integers\n')
        print('2- sum two decimal \n')
        print('3- divide two numbers \n')
        print('4- multiply two numbers \n')
        print('5- name concatenating \n')
        print('6- working with classes \n')
        print('7- exit \n')

        i = int(input('PLEASE SELECT YOUR OPTION \n'))
        match i:
            case 1:
                subtractFunc()
            case 2:
                sumFunc()
            case 3:
                divideFunc()
            case 4:
                multiplyFunc()
            case 5:
                concatenatingFunc()
            case 6:
                workWithClasses()
            case 7: 
                x = False
            case _ : 
                cls()
                print('choose one of above menu ....')
showMenu()