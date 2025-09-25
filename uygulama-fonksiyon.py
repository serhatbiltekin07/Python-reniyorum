#   1- Kendisine gönderilen bir kelimeyi belirten kez ekranda gösteren fonksiyonu yazınız.

def gonderilenKelime(kelime,tekrar):
    i = 1
    while(i <= tekrar):
        print(kelime)
        i +=1
kelime = input("Lütfen bir kelime girin: ")
tekrar = int(input("Bu kelimeyi kaç kez tekrar etmek istersiniz? "))

gonderilenKelime(kelime, tekrar)
# """
# Lütfen bir kelime girin: merhaba biltekin
# Bu kelimeyi kaç kez tekrar etmek istersiniz? 5
# merhaba biltekin
# merhaba biltekin
# merhaba biltekin
# merhaba biltekin
# merhaba biltekin

# """


#   2- Dikdörtgen alan çevresini hesaplayan fonksiyonu yazınız.
def hesapla(kisa,uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)
    return f"alan: {alan}  çevre: {cevre}"

print(hesapla(8,5)) #alan: 40  çevre: 26

#   3- Yazı tura uygulamasını fonksiyon kullanarak yapınız.(Random modülü)
def yaziTura():
    import random
    sayi = random.random()
    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazı"

sonuc = yaziTura()
print(sonuc)

#   4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if(sayi1 > 1):
            for i in range(2, sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)
asalSayilariBul(10,20)
"""
11
13
17
19
asal sayılardaır

"""
#   5- Kendisine gönderilen bir sayının tam bölenlerini bir  liste şeklinde döndüren fonksiyon yazınız.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))  #[2, 4, 5, 10]