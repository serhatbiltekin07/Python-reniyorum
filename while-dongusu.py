#   while-Döngüsü---> koşullu durumda kullanılır

# i = 0
# while i < 10:
#     print("Merhaba Akademi")
#     i +=1

"""
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
Merhaba Akademi
"""

# i = 1
# while i <= 10:
#     print(i)
#     i +=1

"""
1
2
3
4
5
6
7
8
9
10

"""

sayilar = [1,2,3,4,5,6,7,8,9]

i = 0
while(i < len(sayilar)):
    print(sayilar[i])
    i +=1

"""
1
2
3
4
5
6
7
8
9
"""

for sayi in sayilar:
    print(sayi)


"""
1
2
3
4
5
6
7
8
9
"""