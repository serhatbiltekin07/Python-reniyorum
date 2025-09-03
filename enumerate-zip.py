markalar = ["opel","bmw","togg"]

index = 1
for marka in markalar:
    print(f"{index}-{marka}")       # 
    #1-opel
    #2-bmw
    #3-togg
    index +=1


obj1 = enumerate(markalar)
print(type(obj1))   #<class 'enumerate'>
print(list(obj1))   #   [(0, 'opel'), (1, 'bmw'), (2, 'togg')]

obj1 = enumerate(markalar,1)

print(type(obj1))
print(list(obj1))   #[(1, 'opel'), (2, 'bmw'), (3, 'togg')]

for marka in enumerate(markalar):
    print(marka)

# """
# (0, 'opel')
# (1, 'bmw')
# (2, 'togg')

# """

for marka in enumerate(markalar,1):
    print(marka)

# """
# (1, 'opel')
# (2, 'bmw')
# (3, 'togg')

# """

for index,marka in enumerate(markalar,1):
    print(f"{index}-{marka}") 

# """
# 1-opel
# 2-bmw
# 3-togg
# """



#   ZİP


numara = [100,200,300]
ogrenci = ["Ali","Ayşe","Canan"]
sonuc = list(zip(numara,ogrenci))   #[(100, 'Ali'), (200, 'Ayşe'), (300, 'Canan')]
print(sonuc)

for no,isim in zip(numara,ogrenci):
    print(no,isim)

"""
100 Ali
200 Ayşe
300 Canan
"""