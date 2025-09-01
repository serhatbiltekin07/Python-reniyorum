#Bir aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
#benzin : 39.35
#dizel  : 41.71
#lpg    : 20.28


benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

toplamYakitFiyat = 0
ortalamaYakitFiyat = float(input("100 km' deki ortalama yakıt tüketimi: "))
gidilecekYol = float(input("Gidilecek Mesafe: "))
yakitTipi = input("Yakıt Tipini Seçiniz: ")

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitFiyat / 100)

if(yakitTipi == "benzin"):
    toplamYakitFiyat = benzinFiyat * toplamYakitTuketimi
    
elif(yakitTipi == "dizel"):
    toplamYakitFiyat = dizelFiyat * toplamYakitTuketimi
    
elif(yakitTipi == "lpg"):
    toplamYakitFiyat = lpgFiyat * toplamYakitTuketimi
    
else:
    print("Doğru yakıt tipi seçiniz")
    toplamYakitFiyat = 0

if(toplamYakitFiyat !=0):
    print(f"Gidilecek {gidilecekYol} km için toplam yakıt masrafı: {toplamYakitFiyat:.2f} Tl")


"""
100 km' deki ortalama yakıt tüketimi: 7.2
Gidilecek Mesafe: 50
Yakıt Tipini Seçiniz: benzin
Gidilecek 50.0 km için toplam yakıt masrafı: 141.66 Tl
"""



#   Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığını karşılık gelen değerlendirmeyi yazdırınız
not1 = float(input("1.notunuzu giriniz : "))
not2 = float(input("2.notunuzu giriniz : "))
sozlu = float(input("sözlü notunuzu giriniz : "))

ortalama = float((not1 + not2 + sozlu) / 3)

if(0 <= ortalama and ortalama < 25):
    print(f"notunuz : 0 --> ortalamanız: {ortalama}")
elif(25<= ortalama and ortalama < 45):
    print(f"notunuz: 1 --> ortalamanız: {ortalama}")
elif(45 <= ortalama and ortalama < 55):
    print(f"notunuz: 2 --> ortalamanız: {ortalama}")
elif(55 <= ortalama and ortalama < 70):
    print(f"notunuz: 3 --> ortalamanız: {ortalama}")
elif(70 <= ortalama and ortalama < 85):
    print(f"notunuz: 4 --> ortalamanız: {ortalama}")
elif(85 <= ortalama and ortalama <=100):
    print(f"notunuz: 5 --> ortalamanız: {ortalama}")
else:
    print("GEÇERSİZ NOT!!!")

#   0-24 => 0
#   25-44 =>1
#   45-54 =>2
#   55-69 =>3
#   70-84 =>4
#   85-100 =>5


"""1.notunuzu giriniz : 50
2.notunuzu giriniz : 60
sözlü notunuzu giriniz : 70
notunuz: 3 --> ortalamanız: 60.0

1.notunuzu giriniz : 80
2.notunuzu giriniz : 90
sözlü notunuzu giriniz : 90
notunuz: 5 --> ortalamanız: 86.66666666666667




1.notunuzu giriniz : -10
2.notunuzu giriniz : -10
sözlü notunuzu giriniz : -10
GEÇERSİZ NOT!!!
"""