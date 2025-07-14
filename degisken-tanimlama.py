#2000 + 2000 * %18


urunAfiyat = 4000
urunBfiyat = 3000
kdvOrani = 0.20
print(urunAfiyat + (urunAfiyat * kdvOrani))  # ürün A
print(urunBfiyat + (urunBfiyat * kdvOrani))  # ürün B


urunToplami = urunAfiyat+ urunBfiyat
print(urunToplami * kdvOrani)