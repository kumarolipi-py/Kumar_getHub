print(100 * "-")
str3 = "This is lavakumar project.............wow!!!"
print(str3.rjust(50 , "*"))
print(100 * "-")
print(str3.ljust(50, "*"))
print(100 * "-")
# Strip, LStrip, rstrip() method in string
str = "     This is Lavakumar       "
print(str.rstrip())
str = "**********This is Lavakumar****************"
print(str.rstrip("*"))
print(str.lstrip("*"))
print(str.strip("*"))
print(100 * "-")
# Split() Function
str = "this is Example python program..........wow!!! "
print(str.split( ))
print(str.split("i", 2))
print(str.split("w"))
str1 = "this is \nExample python program..........\nwow!!! "
print(str1.splitlines())
print(str.rsplit("is"))
print(100 * "-")
# startwith, endswith method
str4 = "This is lavakumar program for python"
print(str4.startswith("This "))
print(str4.startswith("lava", 8))
print(str4.startswith("Lava", 0, 20))
print(str4.endswith("thon"))
print(str4.endswith("for", 50))

print(100 * "-")
#Swapcase() method
str5 = "this is lavakumar program for python"
print(str5.swapcase())
str5 = "This Is Lavakumar Program For Python"

print(str5.swapcase())
print(100 * "-")
#titile, istitile methods
print(str.title())
print(str.isidentifier())
print(str5.istitle())
print(100 * "-")
#translate()
# this method imports from markstrans
# Rereuired to call marketrans function.
intab = "aeiou"
outtab = "78945"
trantab = str.maketrans(intab, outtab)
str = "this is lavakumar program .........wow"
print(str.translate(trantab))
print(100 * "-")
#Upper() Method
print(str.upper())
print(str.isupper())
print(str.islower())
print(str.istitle())

print(100 * "-")
#zfill()
str6 = "this is string example programm.....................wow!!!"
print(str6.zfill(50))

print(100 * "-")
str7 = "this 2020"
print(str7.isdecimal())
str8 = "12042020123456"
print(str8.isdecimal())



