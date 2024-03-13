c = 10 
def add() :
    global c
    c = c + 2
    print(c)

add()
def outer_function() :
    global number
    number = 100

    def inner_function() :
        global number
        number = 125
    print(f"form outer function {number}")
    inner_function()
    print(f"after inner function calls {number}")

outer_function()
print(f"value of number variables after two function calls {number}")

z = 1000 

def add_function(x) :
    x = x + 100
    print(x)
print(f"value of z {z}")
add_function(z)
print(f"after calling add_function {z}")