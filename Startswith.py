strVar = "This is Lavakumar"
print(strVar.startswith(strVar))
print(strVar.endswith(strVar, 9 , 10))


print("-" * 100)

strVar1 = "Welcome to Python"
print(strVar1.expandtabs(15))

print("-" * 100)

# Capitalize();
strvar2 = 'welcome'
print(strvar2.capitalize())

print("-" * 100)

# Center();

StrVar3 = "welcome"
print(StrVar3.center(100 , '*'))
str4 = StrVar3.capitalize()
print(str4.center(20 , '-'))
print(str4.center(50 , "<"))

print("-" * 100)

str1 = "This is lavakumar"
strchar = str1.upper()
Cstr = 'a'
print("String Count is : ", str1.count(strchar))
print("String Count () : ", str1.count(Cstr, 0 , 20))

print(100 * '-')

#Endswith()

str2 = "Python is programming language 2314"
print(str2.count(str2))
print("Ending with : " , str2.endswith(str2 , 0 , 25))

print(100 * '-')

str2 = "Python is programming language 2314"

print("Starting with : " , str2.startswith(str2 , 0 , 25))


print(200 * '*')

Str='this is string Lavakumar....wow!!!'
suffix='!!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix , 0 , 20))
suffix='Lava'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))

print(100 * '-')

#Expandtab:

str = "This is lavakuma working as \t software engineer"
print("Default String : " + str)
print("Default string is : " + str.expandtabs())
print("Origal string : " + str.expandtabs(16))
print(100 * '-')

# Find();

str2 = "This is pythan programming language"
str3 = 'pythan'
print(" find : ", str2.find(str3))
print("Find : ", str2.find(str3))

# index() Method:
print(100 * '-')
str5 = "This is programing language"
str6 = "T"
print("FInd the Index: ", str5.index(str6))
print("Find the index :", str5.index(str6 , 10))
print("the index : ", str5.index(str6 , 40))


print(100 * '-')
#isalnum:

str7 = 'welcome to python'
print(str7.isalnum())
