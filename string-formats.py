# string concat
ad = "Serhat"
soyad = "Kurtuluş"
yas = 27
#msj= "My name is "+ ad+" "+ soyad+ "."+ "I'm "+ str(yas)+" years old."

# string format
#msj="My name {} {}. I'm {} years old.".format(ad,soyad,yas)
#msj="My name {0} {1}. I'm {2} years old.".format(ad,soyad,yas)
#msj="My name {a} {s}. I'm {y} years old.".format(a=ad, s=soyad, y=yas)



# f-string
#msj=f"My name {ad} {soyad}. I'm {yas} years old."
#print(msj)



#UYGULAMA

title = "Python ile Programlama Dersleri"

# 1- 'title' değişkeni içerisindeki karakter sayısı nedir ?
adet = len(title) #31 karakter var
print(adet)
# 2- 'title' içerisindeki 'Python' kelimesini alın
print(title[:6])#Python

# 3- 'title' değişkeninin ilk 5 ve son 5 karakterini alın.
ilkBes = title[:5] # İlk 5 karakter
sonBes = title[-5:] # Son 5 karakter

print("ilk beş : "+ ilkBes) # Pytho
print("son beş : "+ sonBes) # sleri

# 4- 'title' değişkenini tersten yazdırınız.
print(title[::-1]) #irelsreD amalmargorP eli nohtyP

# 5- Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
# Örnek: Çınar Turan isimli öğrencinin 1. notu 60, 2.notu 50 ve not ortalaması 60 olarak hesaplanmıştır.

not1 = input("1. notunuzu giriniz : ")
not2 = input("2. notunuzu giriniz : ")
notOrtalama = (float(not1)+ float(not2)) /2
print("not ortalamanız " + str(notOrtalama)+ " olarak hesaplanmıştır.")