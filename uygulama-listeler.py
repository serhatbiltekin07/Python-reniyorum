# 1- "Toyota, Bmw, Renault, Mercedes" elamanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota","Bmw","Renault","Mercedes"]
# 2- Listeler kaç elemanlıdır?
sonuc = len(markalar)   #4

# 3- Listenin ilk ve son elemanı nedir?
sonuc = markalar[0]     #Toyota
sonuc = markalar[-1]    #Mercedes

# 4- "Renault" markasını "Togg" ile güncelleyiniz.

markalar[2] = "Togg"
sonuc = markalar    #['Toyota', 'Bmw', 'Togg', 'Mercedes']

# 5- "Togg" Listenin bir elemanı mı dır ? 

sonuc = "Togg" in markalar  #True

# 6- Listenin ilk 2 elemanını alınız.

sonuc = markalar[:2]    #['Toyota', 'Bmw']

# 7- listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.

sonuc = markalar + ["Ford","Citroen"]   #['Toyota', 'Bmw', 'Togg', 'Mercedes', 'Ford', 'Citroen']

# 8- Listenin son elemanını siliniz.

del sonuc[-1]   #['Toyota', 'Bmw', 'Togg', 'Mercedes', 'Ford']


# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi 2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenciler =[
    ["Yiğit","Bilgi",2010,[70,80,90]],
    ["Ada","Bilgi",2011,[70,70,80]],
    ["Çınar","Turan",2017,[60,60,90]]
]

# 10- Öğrencilerin yaşlarını hesaplayınız.,
simdikiYil = 2025
for ogrenci in ogrenciler:
    ad,soyad,dogumYili,notlar =ogrenci
    yas = simdikiYil -dogumYili
    print(f"{ad} {soyad} şuan {yas} yaşında")   #Yiğit Bilgi şuan 15 yaşında
                                                #Ada Bilgi şuan 14 yaşında
                                                #Çınar Turan şuan 8 yaşında


# 11- Öğrencilerin not ortalamalarını hesaplayınız.

for ogrenci1 in ogrenciler:
    ad,soyad,dogumYili,notlar = ogrenci1
    ortalama = sum(notlar) / len(notlar)
    print(f"{ad} {soyad} adlı öğrencinin not ortalaması: {ortalama}")   #Yiğit Bilgi adlı öğrencinin not ortalaması: 80.0
                                                                        #Ada Bilgi adlı öğrencinin not ortalaması: 73.33333333333333
                                                                        #Çınar Turan adlı öğrencinin not ortalaması: 70.0
print (sonuc)
