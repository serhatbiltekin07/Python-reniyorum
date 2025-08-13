x = [2,4,6]
y = [2,4,7]

z=y

print(x==y) #False
print(x is not y)#True
print(z is y)   # z, y midir? ==>True aynı nesne olduğu için
print(z is not y)#False


# Membership

print(2 in x) #  burada şunu söylüyor 2 , x'in içerisinde var mıdır diye soruyor ? ==> #True
print(20 in x) #  burada şunu söylüyor 20 , x'in içerisinde var mıdır diye soruyor ? ==> #False