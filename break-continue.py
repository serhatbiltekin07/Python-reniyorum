# isim = "Biltekin Kurtuluş"

# for harf in isim:
#     if(harf == "t"):
#         break
#     print(harf)

# i=0
# while(i<5):
#     i +=1
#     if (i == 2):
#         continue
#     print(i)

"""
1
3
4
5
"""

i=0
while(i<5):
    i +=1
    if (i == 2):
        break
    print(i)    #1

i =0 
toplam = 0
while(i <=100 ):
    i += 1
    if(i % 2 == 0 ):
        continue
    toplam += i
print(toplam)