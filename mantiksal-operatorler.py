# (yas >= 18) => true , false
# (mezuniyet == 'lise') ya da (mezuniyet == 'üniversite') => true, false 

#sonuc = (yas >=18) ve (mezuniyet == 'lise' veya mezuniyet == 'üniversite' )

x = 11
sonuc = (x > 5) and (x < 10)    #False


x = 9
sonuc = (x > 5) and (x < 10)    #True


# 1- And
#   True,Ture ==> True
#   True,False ==> False
#   False,False ==> False

# 2- Or

#   True,Ture ==> True
#   True,False ==> True
#   False,False ==> False
x = 10
sonuc = (x > 0) and (x % 2 == 0)    # x pozitif çift sayı
sonuc = (x > 0) or (x % 2 == 0)    # x pozitif  ya da çift sayı



# 2- Not

# False => True
# True => False ' a döndürür.

sonuc = not(x > 0)  #False

print(sonuc)