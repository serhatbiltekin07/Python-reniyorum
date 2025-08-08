# value types

# x = 10
# y = 20
# x = y   #20 20
# y=30    #20 30
# print(x,y)  

# reference
a = ["elma","armut"]
b = ["elma","armut"]

a = b       #adres kopyaladınız.
a[0] = "üzüm"
print(a,b)  #['üzüm', 'armut'] ['üzüm', 'armut']

#Liste kopyalama

# listeA = [10,20]
# listeB = listeA
# listeB[0] = 30      #[30, 20] [30, 20]
#print(listeA,listeB)

listeA = [10,20]
listeB = listeA.copy()      # [10, 20] [30, 20] bunu yaptığımız da artık listeA da bir değişiklik olmaz. Ama yukarıda listeA ile listeB  de her ikisinde de değişiklik olur.
listeB = list(listeA)       # [10, 20] [30, 20] aynısını verir 2. yöntem kopyalama
listeB[0] = 30
print(listeA,listeB)