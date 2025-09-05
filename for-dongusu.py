# for => list


sayilar = [1,2,3,4,6,8,91,21]
isimler = ["Ali","Canan","Zeynep"]
isim = "Biltekin Kurtuluş"


for x in sayilar:
    print(x)
# """
# 1
# 2
# 3
# 4
# 6
# 8
# 91
# 21
# """

for x in sayilar:
    print("Merhaba AKADEMİ")

# """
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# Merhaba AKADEMİ
# """

for isim in isimler:
    print(isim)

# """
# Ali
# Canan
# Zeynep
# """

for i in isim:
    print(i)

# """
# B
# i
# l
# t
# e
# k
# i
# n

# K
# u
# r
# t
# u
# l
# u
# ş

# """

my_tuple = [(1,2),(3,4),(5,6)]

for i in my_tuple:
    print(i)

# """
# (1, 2)
# (3, 4)
# (5, 6)
# """

for a,b in my_tuple:
    print(a,b)

# """
# 1 2
# 3 4
# 5 6
# """

my_dict = {
    "41":"Kocaeli",
    "53":"Rize",
    "35":"İzmir"
}
for x in my_dict:
    print(x)   #burada key bilgisini alıyoruz 

# """
# 41
# 53
# 35
# """

for x in my_dict:
    print(my_dict[x])        #key bilgisine karşılık gelen value bilgisini alıyoruz       

# """
# Kocaeli
# Rize
# İzmir
# """

# value almanın kolay yolu

for x in my_dict.values():              
    print(x)                #Kocaeli
                            #Rize
                            #İzmir

#keylere ulaşmada aynışekilde
for x in my_dict.keys():
    print(x)
"""
41
53
35
"""


# while => koşullu