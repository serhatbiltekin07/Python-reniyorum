def full_name(firstname: str,lastname: str, age: int) -> str:
    return f"You name is {firstname} {lastname}"

sonuc = full_name("Biltekin","Kurtulus")    #You name is Biltekin Kurtulus
sonuc = full_name(lastname="Kurtulus", firstname="Biltekin")    #You name is Biltekin Kurtulus
sonuc = full_name(firstname="Biltekin", lastname="Kurtulus")

print(sonuc)