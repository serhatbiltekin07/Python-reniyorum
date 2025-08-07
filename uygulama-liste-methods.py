customers = ["biltekinkurtulus","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]


# 1- 'biltekinkurtulus' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.

order_totals.append(5000)
sonuc = order_totals    #[12000, 13000, 5000, 15000, 5000]

# 2- Son eklenen siparişi siliniz

order_totals.pop()      #[12000, 13000, 5000, 15000]
sonuc = order_totals

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız
    # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır.

for i in range(len(customers)):
    print(f"'{customers[i]} isimli müşterinin sipariş toplamı '{order_totals[i]} liradır.'")

    #'biltekinkurtulus isimli müşterinin sipariş toplamı '12000 liradır.'
    #'ahmetyilmaz isimli müşterinin sipariş toplamı '13000 liradır.'
    #'cinarturan isimli müşterinin sipariş toplamı '5000 liradır.'
    #'yigitbilgi isimli müşterinin sipariş toplamı '15000 liradır.'


# 4- Müşterileri alfebetik olarak sıralayınız.
customers.sort()    #['ahmetyilmaz', 'biltekinkurtulus', 'cinarturan', 'yigitbilgi']
sonuc = customers

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()     # burada önce küçükten büyüğe sıraladık sonra reverse() ile büyükten küçüğe azalan şekilde sıraldık
order_totals.reverse()     # [15000, 13000, 12000, 5000]
sonuc = order_totals

# 6- En düşük sipariş hangisidir?
sonuc = min(order_totals)   #5000

# 7- 'biltekinkurtulus' isimli kullanıcının kaç tane siparişi vardır ?
sonuc = customers.count('biltekinkurtulus')         # 1

# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.

customers.remove('ahmetyilmaz')     #['biltekinkurtulus', 'cinarturan', 'yigitbilgi']
sonuc = customers

# 9- Listelerdeki tüm içerikleri siliniz.

# customers.clear()
# sonuc = customers   #[]
# order_totals.clear()
# sonuc = order_totals    #[]

# 10- Kullanıcıdan aldığımız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

userName = input("müşteri adı: ")
toplam = input("toplam: ")
customers.append(userName)
order_totals.append(toplam)
                            #müşteri adı: serhatbiltekin
                            #toplam: 7000

print(customers)        #['biltekinkurtulus', 'cinarturan', 'yigitbilgi', 'serhatbiltekin']
print(order_totals)     #[15000, 13000, 12000, 5000, '7000']


print(sonuc)