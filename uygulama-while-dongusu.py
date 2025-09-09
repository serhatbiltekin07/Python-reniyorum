#   1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
sayi1 = int(input("Başlangıç değeri girin: "))
sayi2 = int(input("Bitiş değeri girin: "))
baslangic = min(sayi1,sayi2)
bitis = max(sayi1,sayi2)
print("Çift sayılar: ")

while(baslangic <= bitis):
    if(baslangic % 2 == 0):
        print(baslangic)
    baslangic +=1

"""
Başlangıç değeri girin: 10
Bitiş değeri girin: 1
Çift sayılar: 
2
4
6
8
10
"""
#   2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.
i = 100
while(i >=1):
    print(i)
    i -=1

"""
100
99
98
97
96
95
94
93
92
91
90
89
88
87
86
85
84
83
82
81
80
79
78
77
76
75
74
73
72
71
70
69
68
67
66
65
64
63
62
61
60
59
58
57
56
55
54
53
52
51
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1

"""
#   3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

numbers = []
i = 1
while(i <= 5):
    sayi = int(input("sayı değeri giriniz : "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)

"""
sayı değeri giriniz : 2
sayı değeri giriniz : 5
sayı değeri giriniz : 8
sayı değeri giriniz : 90
sayı değeri giriniz : 34
[2, 5, 8, 34, 90]

"""
#   4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.


usurname = ""
while not usurname:
    usurname = input("Kullanıcı adı:")
print("Girilen usurname: " + usurname)

"""
Kullanıcı adı:
Kullanıcı adı:
Kullanıcı adı:biltekin
Girilen usurname: biltekin

"""