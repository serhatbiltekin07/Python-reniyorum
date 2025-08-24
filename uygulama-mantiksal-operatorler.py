#   1- Yaşı 18'den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.
yas = int(input("yaşının giriniz: "))
izin = input("veli izni var mı ? (evet/hayır)").lower() =="evet"
calisabilir = (yas >= 18) or (yas < 18 and izin)
print(f"Kişinin yaşı: {yas}, veli izni: {izin}, çalışabilir mi ? : {calisabilir}")


#   2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.

giris = int(input("Ders notunuzu giriniz : "))
notlar = (giris >= 50) and (giris <= 100)

print(f"Kişinin notu : {giris}, geçti mi? kaldı mı ?{notlar}")


#   3-  Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.

not1 = int(input("not1 : "))
not2 = int(input("not2 : "))
not3 = int(input("not3 : "))

ortalama = (not1 + not2 + not3) / 3 
zayifVarMi = (not1 < 50) or (not2 < 50) or (not3 < 50)
sonuc = (ortalama >= 70) and (not zayifVarMi)
print(f"Not ortalaması : {ortalama}, zayıf var mı ? : {zayifVarMi}, Teşekkür belgesi alır mı ? : {sonuc} ")

#   4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu

mezuniyet = input("Mezun durumunuz (önlisans/lisans): ").lower()
diploma = (mezuniyet == "önlisans") or (mezuniyet == "lisans")
sigaraKullanma = input("Sigara kullanıyor musunuz? (evet/hayır): ").lower() == "evet"
iseGirme = (diploma and not(sigaraKullanma))

print(f"Mezun durumu : {diploma}, sigara kullanma durumu : {sigaraKullanma},  işe girme durumu : {iseGirme} ")

#   5- Uygulamaya giriş kontrolünü "username ya da email" ve "parola" için yapalım.

email = "info@biltekinkurtulus.com"
usurname = "biltekinkurtulus"
password = "12345"

girilen_bilgi = input("email ya da usurname: ")
girilen_parola = input("parola: ")

sonuc = (email == girilen_bilgi or usurname == girilen_bilgi) and (password == girilen_parola)