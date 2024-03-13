import calendar
import datetime

year = 2024
month = 10 
page = calendar.month(year, month)
stringVar = "your dick is the most beautiful dick of the world!"
print("hello World!")
print("----- incoming message ------")
print(stringVar)
print("----- Calendar of october ------")
print(page)

# calculate sum of two numbers
def calculator(a , b ) : 
    return a+b;


# exponents two numbers
def power_a_number(num, pow) :
    return num**pow;

# concatenate two strings
def concat_two_strings(phraseOne, phraseTwo) : 
    return phraseOne + phraseTwo;

# repeat a phrase n times
def repeat_n_times(phrase, n): 
    return phrase*n;

# this function returns minutes from midnight
def number_of_min_from_hour() :
    min = datetime.datetime.now().minute;
    hour = datetime.datetime.now().hour;
    return hour*60+min;
def show_types_of_value(val) :
    return type(val);

def convert_string_to_number(val) :
    return int(val);

print(calculator(10, 15))
print(power_a_number(2, 3))
print(power_a_number(2, 8))
print(concat_two_strings("hello ", "world!"))
print(repeat_n_times("aida ", 10))
print(number_of_min_from_hour())
print("type of :", show_types_of_value(3.14895497))
print("type of :", show_types_of_value("hello World!"))
print("type of :", show_types_of_value(3))
print("convert \"3287954\" to int", convert_string_to_number("3287954"))