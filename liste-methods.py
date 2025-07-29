sayilar = [4,6,8,2,56,78,90,4,4]
isimler = ['ahmet','canan','zeynep','gökhan','ali']
sonuc = min(sayilar)    # 2
sonuc = min(isimler)    # ahmet
sonuc = max(isimler)    # zeynep
sonuc = max(sayilar)    # 90


    # ekleme

sayilar.append(12)                     # listenin sonuna ekledi ==> [4, 6, 8, 2, 56, 78, 90, 12]
isimler.append('çınar')                # listenin sonuna ekledi ==> ['ahmet', 'canan', 'zeynep', 'gökhan', 'ali', 'çınar']

sayilar.insert(0,100)                  # 0. index e 100 bilgisini ekler nereye eklemek istersek o olur.==> [100, 4, 6, 8, 2, 56, 78, 90, 12]
sayilar.insert(-1,100)                 # -1. index e 100 bilgisini ekler nereye eklemek istersek o olur.==> [100, 4, 6, 8, 2, 56, 78, 90, 100, 12]
sayilar.insert(-3,100)                 # -3. index e 100 bilgisini ekler nereye eklemek istersek o olur.==> [100, 4, 6, 8, 2, 56, 78, 100, 90, 100, 12]
sayilar.insert(len(sayilar),100)       # Listenin sonuna eklemek için kullanırız.==> [100, 4, 6, 8, 2, 56, 78, 100, 90, 100, 12, 100]

#   silme

sayilar.pop()                            #Listenin son elemanı silinir ==> [4, 6, 8, 2, 56, 78] ==> 90 silindi
sayilar.pop(0)                           #Listenin başındaki elemanı silinir ==> [6, 8, 2, 56, 78]

isimler.remove('canan')                  # "canan silindi" ==> ['ahmet', 'zeynep', 'gökhan', 'ali']

#   sıralama

sayilar.sort()                           #  [2, 6, 8, 56, 78] sıraladı küçükten büyüğe doğru
isimler.sort()                           # ['ahmet', 'ali', 'gökhan', 'zeynep'] alfabetik sıraya göre sıraladı
sayilar.reverse()                        # tersten sıralar  ==> [78, 56, 8, 6, 2]

#    eleman sayma metodu

sonuc = sayilar.count(4)                # 4 rakamından 3 defa tekrar ettiğini buluruz ==> 3
sonuc = isimler.count('canan')          # canandan 1 tane olduğunu gösterir ettiğini buluruz ==> 1


#   Arama

sonuc = sayilar.index(4)                 # 4 rakamını bulduğu ilk index numarasını verir ==> 0 .indexdir.


sonuc = sayilar
sonuc = isimler                         


print(sonuc)