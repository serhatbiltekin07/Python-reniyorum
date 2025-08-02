meyveler = {"elma","armut","kiraz"}      #elemanları tekrarlanmaz elma mesela bir defa yazılır
meyveler2 = {"elma","armut","kiraz","kavun"}
sonuc = meyveler[0] # hata verir set lere index numarası ile erişilemez.
sonuc = meyveler    #{'armut', 'elma', 'kiraz'}

for x in meyveler:
    print(x)       
# elma
# kiraz
# armut


#sonuc = "elma" in meyveler  #liste içerisinde "elma" ' nın olup olamadığını söyleyebiliriz ===> True değeri döner.

meyveler.add("karpuz")      #{'elma', 'karpuz', 'armut', 'kiraz'}
meyveler.update(meyveler2)  #{'armut', 'karpuz', 'kiraz', 'elma', 'kavun'} ==>  "kavun" ' u ekledi
meyveler.remove("elma")     #{'armut', 'kavun', 'karpuz', 'kiraz'} ==> "elma" silindi ==> olamayan key değerini silmeye kalkarsak #raise an error gösterir
meyveler.discard("armut")   #{'kavun', 'kiraz', 'karpuz'}==> "armut" silindi
meyveler.pop()  # bir indexleme olamadığı için sondaki elemanı silmez rastgele siler    {'elma', 'kiraz', 'kavun'}
meyveler.clear()    # set() tamamen siler
sonuc = meyveler
print(sonuc) 