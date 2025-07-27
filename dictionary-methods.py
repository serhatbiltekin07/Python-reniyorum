#   Dictionary Metotları

yemekTarifi ={
    "yemekAdi":"Musakka",
    "yemekTarifi":"tarif açıklaması",
    "resim":"1.jpg"
}

# access items
sonuc = yemekTarifi["yemekTarifi"]           #tarif açıklaması
sonuc = yemekTarifi.get("yemekAdi")          #Musakka

sonuc = yemekTarifi.keys()                   #dict_keys(['yemekAdi', 'yemekTarifi', 'resim'])
sonuc = yemekTarifi.values()                 #dict_values(['Musakka', 'tarif açıklaması', '1.jpg'])
sonuc = yemekTarifi.items()                  #dict_items([('yemekAdi', 'Musakka'), ('yemekTarifi', 'tarif açıklaması'), ('resim', '1.jpg')])

# update items


#yemekTarifi["yemekAdi"] = "Mantı"           #{'yemekAdi': 'Mantı', 'yemekTarifi': 'tarif açıklaması', 'resim': '1.jpg'}

yemekTarifi.update({"yemekAdi":"Mantı"})     #{'yemekAdi': 'Mantı', 'yemekTarifi': 'tarif açıklaması', 'resim': '1.jpg'}
yemekTarifi.update({"yemekAdi2":"Yeni Mantı"})#{'yemekAdi': 'Mantı', 'yemekTarifi': 'tarif açıklaması', 'resim': '1.jpg', 'yemekAdi2': 'Yeni Mantı'}
sonuc = yemekTarifi

#   DELETE İTEMS

#yemekTarifi.pop("yemekAdi")                 #{'yemekTarifi': 'tarif açıklaması', 'resim': '1.jpg', 'yemekAdi2': 'Yeni Mantı'}
yemekTarifi.popitem()   # listeye son eklenen elemanı siler "yeni mantı" siler ==> {'yemekAdi': 'Mantı', 'yemekTarifi': 'tarif açıklaması', 'resim': '1.jpg'}
yemekTarifi.clear()     #liste içerisindeki bütün elemanları siler ==> {}
sonuc = yemekTarifi

print(sonuc)