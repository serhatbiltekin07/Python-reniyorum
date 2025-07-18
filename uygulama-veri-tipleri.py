"""
    Uygulama 1 : Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: pi*(r**2)
    çevre: 2 * pi * r
    uygulama 2: klavyeden girinlen km bilgisini mil cinsinden hesaplayınız.
    mil= km / 1.609344
"""
pi = 3.14

r = float(input("Yarı çap : "))
alan = pi*(r**2)
cevre = 2 * pi * r

print("Alan : " + str(alan))
print("Çevre: " + str(cevre))

km = input("km giriniz : ")
mil = float(km)/ 1.609344
mil = round(mil,2) ## yuvaladık 
print(km + " Km: "+ "Mil: "+ str(mil))