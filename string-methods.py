mesaj = "BTK akademi python Kursu"

sonuc = mesaj.upper()   # bütün harfleri büyük harfe çevirir ==> BTK AKADEMI PYTHON KURSU
sonuc = mesaj.lower()   # bütün harfleri Küçük harfe çevirir ==> btk akademi python kursu
sonuc = mesaj.title()   # bütün kelimelerin ilk  harflerini büyük harfe çevirir ==> Btk Akademi Python Kursu
sonuc = mesaj.capitalize() # sadece ilk kelimenin ilk harfini büyük yapar geri kalanı küçük olur ==> Btk akademi python kursu

sonuc = "abc".isupper() # büyük harf mi bool türünde sorar ==>  False
sonuc = "abc".islower() # büyük harf mi bool türünde sorar ==> True

print(mesaj)
sonuc = mesaj.strip()  # başında veya sonundaki boşluk karakterilerini temizler
sonuc =  mesaj.split()   # ['BTK', 'Akademi', 'python', 'Kursu']
sonuc = mesaj.split()[0] # 'BTK' sadece döndü
sonuc = mesaj.split()[1] # 'Akademi' sadece döndü

sonuc = mesaj.index("akademi") #kelimesi kaçıncı index den başladığını söyler ==> o da 5 dir.
sonuc = mesaj.startswith("b")   # bu liste "b" ile mi başlıyor onu söyler ya true ya da false döner ==> "false" döndü sonuc
sonuc = mesaj.endswith("u")       # bu liste "u" ile mi bitiyor onu söyler ya true ya da false döner ==> "true" döndü sonuc

sonuc = mesaj.replace("python","Javascript") # "Python" kelimesini bulacak bunun yerine "Javascript" kelimesini eklicek ==> BTK akademi Javascript Kursu

print(sonuc)