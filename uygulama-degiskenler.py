"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde sakklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Sadık Turan
0532 1234567
info@sadikturan.com
Kocaeli

Satın alınan ürünler

ürün adı: Kablosuz Mouse
Fiyatı : 550 Tl

ürün adı: Kablosuz Klavye
Fiyatı : 560 Tl

ürün adı: Dizüstü Bilgisayar
Fiyatı : 55.000 Tl
"""

musteriAdi =  "Sadık"
musteriSoyad = "Turan"
musteriTelefon = "05321234567"
musteriEmail= "info@sadikturan.com"
musteriAdres = "Kocaeli"

urun1Adi = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Adi = "Kablosuz Klavye"
urun2Fiyat = 560

urun3Adi = "Dizüstü Bilgisayar"
urun3Fiyat = 55000

tolamOdenenUcret = urun1Fiyat+urun2Fiyat+urun3Fiyat
print("Toplanan ödenen miktar : "+ str(tolamOdenenUcret))

print("Toplam kdv oranı: " + str(tolamOdenenUcret *0.18))

"""str(100)=> "100"+ "ali"=>100ali"""