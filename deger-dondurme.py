def toplam():
    return 10+20 

sonuc = toplam() #30

#print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year

def saat():
    import datetime
    return datetime.datetime.now().hour

def yasHesapla():
    return yil() - 1997

sonuc = yasHesapla()    #28
print(sonuc)

def selamlama():
    if(saat() < 12):
        return "Günaydın"
    else:
        return "Merhaba"
    
print(selamlama())  #Merhaba şuan saat 14:00 o yüzden merhaba dedi