urunler = [
    {"urunAdi":"Hp Victus 1", "fiyat":32999},
    {"urunAdi":"Lenova ThinkPad", "fiyat":25499},
    {"urunAdi":"Apple Macbook", "fiyat":49999},
    {"urunAdi":"Huawei Matebook", "fiyat":26999},
    {"urunAdi":"Casper Nirvana", "fiyat":20000},
    {"urunAdi":"Hp Victus 2", "fiyat":30000},
]

#   1-Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#   "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."

for x in urunler:
    ad = x["urunAdi"]
    fiyat = x["fiyat"]
    print(f"{ad} marka ürünün fiyatı {fiyat} Türk Lirası.")

"""
Hp Victus 1 marka ürünün fiyatı 32999 Türk Lirası.
Lenova ThinkPad marka ürünün fiyatı 25499 Türk Lirası.
Apple Macbook marka ürünün fiyatı 49999 Türk Lirası.
Huawei Matebook marka ürünün fiyatı 26999 Türk Lirası.
Casper Nirvana marka ürünün fiyatı 20000 Türk Lirası.
Hp Victus 2 marka ürünün fiyatı 30000 Türk Lirası.
"""


#   2- Ürünlerin fiyatları toplamı nedir ?
fiyatToplam = 0
for sayi in urunler:
    fiyat = sayi["fiyat"]
    fiyatToplam +=fiyat
print(fiyatToplam)  #185496


#   3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.
for urun in urunler:
    fiyat = urun["fiyat"]
    if(25000 <=fiyat and fiyat <= 40000):
        print(fiyat)
"""
32999
25499
26999
30000
"""
#   4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz
arama = input("Marka İsmi giriniz: ").lower()
for deger in urunler:
    ad = deger["urunAdi"].lower()
    if(arama in ad):
        print(f"{deger["urunAdi"]} --> {deger["fiyat"]} TL")
else:
    print("Marka bulunamadı !!!!")