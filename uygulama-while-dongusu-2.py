#   Klavyeden girilen n sayıdaki öğrenci bilgisini liste içersine saklayınız.
#   ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun
#   ** Öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.

ogrenciler = []

sayi = int(input("Kaç öğrenci kayıt yapacaksınız:"))
i=0
while(i<sayi):
    number = int(input("Öğrenci No :"))
    name = input("Öğrenci Ad: ")
    surname = input("Öğrenci soyad: ")
    ogrenciler.append({
        'number':number,
        'name':name,
        'surname':surname
    })
    i+=1

for ogrenci in ogrenciler:
    print(f"Öğrenci No: {ogrenci["number"]}, Öğrenci Ad: {ogrenci["name"]}, Öğrenci Soyad: {ogrenci["surname"]}")

"""
Kaç öğrenci kayıt yapacaksınız:2
Öğrenci No :1234
Öğrenci Ad: biltekin
Öğrenci soyad: kurtuluş 
Öğrenci No :9876
Öğrenci Ad: serhat
Öğrenci soyad: kar
Öğrenci No: 1234, Öğrenci Ad: biltekin, Öğrenci Soyad: kurtuluş
Öğrenci No: 9876, Öğrenci Ad: serhat, Öğrenci Soyad: kar
"""