def selamlama(isim="Kullanıcı", mesaj ="iyi Günler"):
    return f"{mesaj} {isim}"

sonuc = selamlama("Biltekin", "Merhaba")    # default yapmadığımız zaman ==Merhaba Biltekin
sonuc = selamlama("Biltekin")    # default yapdığımız zaman ==iyi Günler Biltekin
sonuc = selamlama()    # default yapdığımız zaman ==iyi Günler Kullanıcı


def usAlma(taban, us):
    return taban ** us

sonuc= usAlma(2,3)  #8 üssünü aldık

#default


def usAldik(taban, us = 2):
    return taban ** us

sonuc = usAldik(5)  #25 üs aldık 


def toplam(a,b):
    return a + b

def cikarma(a,b):
    return a - b

# def islem(a,b,fn):
#     return fn(a,b)

def islem(a,b,fn = toplam):
    return fn(a,b)

sonuc = islem(10,20,toplam)    #30
print(sonuc)