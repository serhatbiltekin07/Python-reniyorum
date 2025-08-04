my_list = [1,2,3]
my_tuple = (1,2,3,1)  #değiştirilemez ve değer ataması yapılamaz==> bellekte daha az yer kaplar 

print(type(my_list))    #<class 'list'>
print(type(my_tuple))   #<class 'tuple'>

sonuc = my_list[0]  #1
sonuc = my_tuple[0]  #1

my_list.append(3)   #[1, 2, 3, 3]
sonuc= my_list
#my_tuple.apped(3)   # burada hata verir ekleme yapılamaz o yüzden

# tuple için count ve index metotlarını kullanabilirsin diğer metotları kullanmazsın 


sonuc = my_tuple.count(1)   #2

my_tuple2 = tuple([2,3,4])

print(type(my_tuple2))      #<class 'tuple'>