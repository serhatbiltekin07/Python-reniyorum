sayilar = [3,5,7,2,12,32,45]

#   1- "sayilar" listesindeki her bir elemanı yazdırınız.
for x in sayilar:
    print(x)
"""
3
5
7
2
12
32
45    
"""
#   2- "sayilar" listesinde hangi sayılar 3'ün katıdır?
for i in sayilar:
    if(i % 3 == 0):
        print(i)
"""
3
12
45
"""

#   3- "sayilar" listesinde tüm sayıların toplamı nedir ?

toplam = 0
for sayi in sayilar:
    toplam += sayi
print(toplam)   #106

urunler = ["samsung s24","samsung s22","iphone 15","iphone 14"]

#   4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz.
for urun in urunler:
    index = urun.find("iphone")
    if(index > -1):
        print(urun)     #iphone 15, iphone 14


#   5- "urunler" listesinde kaç adet samsung ürünü vardır?
samsungSayisi = 0
for tel in urunler:
    index = tel.find("samsung")
    if(index > -1):
        samsungSayisi += 1
print(samsungSayisi)    #2