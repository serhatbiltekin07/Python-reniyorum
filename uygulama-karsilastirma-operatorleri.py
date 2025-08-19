# 1- Girilen 2 sayıdan hangisi büyüktür ? 
# a = int(input("a: "))
# b = int(input("b: "))
# sonuc = (a > b)
# print(f"a: {a} b:{b} den büyüktür: {sonuc}")
#a: 8
#b: 5
#a: 8 b:5 den büyüktür: True



# 2- Girilen bir sayının tek çift kontrolünü yazınız.
# sayi = int(input("sayi: "))
# tekcift = (sayi % 2 == 0)
# print(f'girilen sayı çift olma durumu: {tekcift}')


# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstüne başarılı.

not1 = int(input("not 1 : "))
not2 = int(input("not 2 : "))
not3 = int(input("not 3 : "))

ortalama = (not1 + not2 + not3) / 3

print(f"öğrencinin not ortalaması : {ortalama}, başarı durumu {ortalama >= 50}")

# not 1 : 50
# not 2 : 50
# not 3 : 50
# öğrencinin not ortalaması : 50.0, başarı durumu True

# not 1 : 70
# not 2 : 50
# not 3 : 40
# öğrencinin not ortalaması : 53.333333333333336, başarı durumu True

# not 1 : 30
# not 2 : 40
# not 3 : 20 
# öğrencinin not ortalaması : 30.0, başarı durumu False