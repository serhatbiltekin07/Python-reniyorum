a,b,c,d = 2,2,10,5


eposta = "info@biltekinkurtulus.com"
parola = "135790"

sonuc = (a == b)    #True
sonuc = (a == c)    #False
sonuc = (a != c)    #True
sonuc = (a != b)    #False


#sonuc = (eposta == input("eposta: "))   # True değeri döner yanlış girilirse ise ==> False değeri döner
#sonuc = (parola == input("parola: "))   # True değeri döner yanlış girilirse ise ==> False değeri döner

sonuc = (a > b) #False 
sonuc = (c > a) #True 
sonuc = (a >= b) #True 
sonuc = (a < b) #False 
sonuc = (a <= b) #True 
sonuc = (a < c) #True 

sonuc = (True == 1) #True  
sonuc = (False == 0) #True  

sonuc = int(True)   # 1

print(sonuc)