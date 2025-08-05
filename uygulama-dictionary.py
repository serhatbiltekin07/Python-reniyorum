# Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız.
    #   101 Yiğit Bilgi 2010 (40,80,90)
    #   102 Ada Bilgi 2012 (80,80,80)
    #   103 Çınar Turan 2017 (70,70,70)

#   Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.
    #101 numaralı Yiğit Bilgi ismindeki öğrencinin yaşı 14 ve not ortalaması 70.

ogrenciler = {
    101:{
        "Ad":"Yiğit",
        "Soyad":"Bilgi",
        "DogumYili": 2012,
        "Notlar":(40,80,90)
    },
    102:{
        "Ad":"Ada",
        "Soyad":"Bilgi",
        "DogumYili": 2010,
        "Notlar":(80,80,80)
    },
    103:{
        "Ad":"Çınar",
        "Soyad":"Turan",
        "DogumYili": 2017,
        "Notlar":(70,70,70)
    }
}

ogrenciNo = int(input('öğrenci no: '))
ogrenci = ogrenciler[ogrenciNo]
ortalama = (ogrenci["Notlar"][0] + ogrenci["Notlar"][1] + ogrenci["Notlar"][2]) / 3

print(f"{ogrenciNo} numaralı {ogrenci["Ad"]} {ogrenci["Soyad"]} ismindeki öğrencinin yaşı {2025 - ogrenci["DogumYili"]} ve not ortalaması {ortalama}.")

#öğrenci no: 101
#101 numaralı Yiğit Bilgi ismindeki öğrencinin yaşı 13 ve not ortalaması 70.0.
#öğrenci no: 102
#102 numaralı Ada Bilgi ismindeki öğrencinin yaşı 15 ve not ortalaması 80.0.
#öğrenci no: 103
#103 numaralı Çınar Turan ismindeki öğrencinin yaşı 8 ve not ortalaması 70.0.