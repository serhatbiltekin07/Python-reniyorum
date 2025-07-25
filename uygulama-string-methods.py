kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

# 1- ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.

sonuc = kursAdi.strip() #Btk Akademi Python ile Programlama Dersleri


# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
sonuc = kursAdi.lower() #btk akademi python ile programlama dersleri

# 3- website değişkeninde kaç tane '.' karakteri vardır?

sonuc = website.count('.') # 3

# 4- website değişkeni 'https' ile mi başlıyor?

sonuc = website.startswith("https") #True

# 5- website 'tr' ile mi bitiyor?

sonuc = website.endswith("tr")  #False

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor ?

sonuc = kursAdi.isalpha() #False

# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiniz

sonuc = kursAdi.replace(" ","-") #Btk-Akademi-Python-ile-Programlama-Dersleri

# 8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştiriniz.

sonuc = kursAdi.replace("Python","ReactJs") #Btk Akademi ReactJs ile Programlama Dersleri

# 9- website değişkeni 'www' içeriyor mu ?

sonuc = website.find("www") !=-1 #True

# 10- kursAdi değişkenini listeye çeviriniz.

sonuc = kursAdi.split() #['Btk', 'Akademi', 'Python', 'ile', 'Programlama', 'Dersleri']

print(sonuc)