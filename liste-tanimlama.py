programlama_diller = ["Python","C#","Java","Javascript"]
sonuc = programlama_diller         # ['Python', 'C#', 'Java', 'Javascript']
sonuc = type(programlama_diller)   # <class 'list'>
sonuc = programlama_diller[0:2]    #['Python', 'C#']
sonuc = programlama_diller[:2]     #['Python', 'C#']
sonuc = programlama_diller[0:]     #['Python', 'C#', 'Java', 'Javascript']
sonuc = programlama_diller[-1]     #Javascript
sonuc = programlama_diller[-3:-1]  #['C#', 'Java']
sonuc = programlama_diller[-3:]    #['C#', 'Java', 'Javascript']

#güncelleme

programlama_diller[-1] = "Php"                 #['Python', 'C#', 'Java', 'Php']
sonuc = programlama_diller
sonuc = len(programlama_diller)                # kaç eleman olduğunu söyler ==> 4
sonuc = programlama_diller + ["Go","Delphi"]   #['Python', 'C#', 'Java', 'Php', 'Go', 'Delphi']

sonuc = "Python" in programlama_diller          # programlama_dilleri içerisinde "Python" var  mı yok mu ona bakar true yada false döner ==> True
sonuc = "React" in programlama_diller          # False ==> koşul ifadeleri aslında



# elemanı nasıl sileriz
del programlama_diller[0]  #Python sildik burada
for dil in programlama_diller:
    print(dil)      #Python
                    # C#
                    #Java
                    #Php
print(sonuc)