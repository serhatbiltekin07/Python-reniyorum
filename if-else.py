if(True):
    print("merhaba")    # merhaba

login = True
if(login):
    print("Login olundu")   #Login olundu


email = "info@biltekinkurtulus.com"
parola = "12345"
login = (email == "info@biltekinkurtulus.com") and (parola =="12345")
if(not(login)):
    print("login girişi yapıldı.")  #login girişi yapıldı.
else:
    print("email ya da parola yanlış")  #email ya da parola yanlış

email = "info@biltekinkurtulus.com"
parola = "12345"

if(email == "info@biltekinkurtulus.com"):
    if(parola == "12345"):
        print("Login olundu")
    else:
        print("parola yanlış")
else:
    print("email yanlış")


# soru
    #soru
    #diğer
#diğer