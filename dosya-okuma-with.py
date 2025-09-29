file = open("log.txt", encoding="utf-8")
print(file.read())

file.close()

#Kolay yolu şimdi altta yapacaz


with open("log.txt", encoding="utf-8") as file:
    print(file.read())

"""
1.satır
2.satır
3.satır

"""

with open("log.txt",encoding="utf-8") as file:
    for i in file:
        print(i,end="")

"""
1.satır
2.satır
3.satır
"""


try:
    with open("log2.txt",encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatası")

"""dosya okuma hatası"""