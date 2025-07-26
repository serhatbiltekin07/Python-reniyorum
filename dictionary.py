sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

print(plakalar[0],sehirler[0])  #41 kocaeli
print(plakalar[1],sehirler[1])  #34 istanbul

print(plakalar[sehirler.index('istanbul')]) #34
print(plakalar[sehirler.index('kocaeli')]) #41



# dictionary

plakalar = {
    'kocaeli':41,
    'istanbul':34,
    'izmir':36
    }

plakalar['izmir'] = 35  # burada düzeltme ya da güncelleme işlemi yaparız

print(plakalar['kocaeli'])     # 41
print(plakalar['istanbul'])    #34
print(plakalar['izmir'])       #35

