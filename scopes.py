#   Local scope
#   Global scope

x = "global scope"

def my_func():
    x = "local scope"
    print(x)

my_func()   #local scope
print(x)    #global scope

name = "Çınar"
def change_name(newname):
    name = newname
    print(name)

change_name("Ada")  #Ada
print(name) #Çınar


name = "Çınar"
def change_name(newname):
    global name
    name = newname
    print(name)

change_name(name)   #Çınar
print(name) #Çınar


def greeting():
    name = "Çınar"

    def hello():
        name = "Ada"
        print("hello", name)
    hello()

greeting()  #hello Ada

x = 50

def test(x):
    print(f"x: {x}")    #x: 50

    x = 100
    print(f"changed x to {x}")  #changed x to 100

test(x) #changed x to 100
print(x)    #50