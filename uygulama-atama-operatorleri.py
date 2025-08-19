a,b,c = 4,8,(12,2)

# 1- Kullanıcıdan aldığınız 2 sayısının çapımı ile a,b,c toplamının farkı nedir ?
# sayi1 = int(input("1.sayıyı giriniz : "))
# sayi2 = int(input("2.sayıyı giriniz : "))
# carpim = sayi1 * sayi2
# toplam = a+b+sum(c)
# fark = carpim - toplam
# print(fark)
# 2- c' nin b'ye kalansız bölümünü hesaplayınız.
toplaC = sum(c)
sonuc = toplaC // b #1
# 3- (a,b,c) toplamının mod 7'si nedir?
topla = a+b+sum(c)
sonuc = topla % 7   #5
# 4- b'nin a.kuvvetini hesaplayınız.
sonuc = b ** a  #4096

# 5- a, *b, c = (2,4,6,8,13) işlemine göre c'nin küpü nedir ?

a, *b, c = (2,4,6,8,13)

print(a,b,c)    #2 [4, 6, 8] 13
print(c ** 3)  # 2197 c nin küpü

# 6- a, b, *c = (2,4,6,8,13) işlemine c'nin değerleri toplamı nedir ? 

a, b, *c = (2,4,6,8,13)
print(a,b,c)    #2 4 [6, 8, 13]
print(c[0]+c[1]+c[2])   #27

print(sonuc)