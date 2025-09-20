# def display_user(*args):
#     print(type(args))
#     print(args)

# display_user()      #<class 'tuple'>
#                     #()

# def display_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# display_user()   #<class 'dict'>
#                 #{}


# def display_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# display_user(username = "biltekinkurtulus")
# """
# <class 'dict'>
# {'username': 'biltekinkurtulus'}
# """
# display_user(username = "biltekinkurtulus",email = "info@biltekinkurtulus.com") #{'username': 'biltekinkurtulus', 'email': 'info@biltekinkurtulus.com'}



def display_user(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

display_user(username = "biltekinkurtulus")
display_user(username = "biltekinkurtulus",email = "info@biltekinkurtulus.com")
display_user(username = "biltekinkurtulus",email = "info@biltekinkurtulus.com", country = "Türkiye")

"""
username: biltekinkurtulus


username: biltekinkurtulus
email: info@biltekinkurtulus.com


username: biltekinkurtulus
email: info@biltekinkurtulus.com
country: Türkiye

"""



def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1 = "value1", key2 = "value2")

"""
10
20
30
(40, 50, 60)
{'key1': 'value1', 'key2': 'value2'}

"""