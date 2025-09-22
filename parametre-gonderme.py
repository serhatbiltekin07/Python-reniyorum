def selamlama(isim):
    return "Merhaba, " + isim

# print(selamlama("Biltekin")) #Merhaba, Biltekin
# print(selamlama("Mehmet"))  #Merhaba, Mehmet


def toplam(sayi1, sayi2):
    return sayi1 + sayi2

# print(toplam(10,20))    #30
# print(toplam(10,30))    #40

def yasHesapla(dogumYili):
    return 2025-dogumYili

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas
    if(kalanSure > 0 ):
        return f"{isim}, emekliliğinize {kalanSure} yıl kaldı"
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz"
    

print(emekliligeKacYilKaldi(1997,"Biltekin"))   #Biltekin, emekliliğinize 37 yıl kaldı
print(emekliligeKacYilKaldi(1980,"Ali"))    #Ali, emekliliğinize 20 yıl kaldı
print(emekliligeKacYilKaldi(1950,"Ayşe"))   #Ayşe, zaten 10 yıl önce emekli oldunuz

# print(yasHesapla(1997))   #28

# print(yasHesapla(1985))   #40
# print(yasHesapla(2003))   #22