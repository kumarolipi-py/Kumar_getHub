#Decode Method
import base64
Str = "this is string example....wow!!!"
Str=base64.b64encode(Str.encode('utf-8',errors='strict'))
print ("Encoded String: " , Str)

print(100 * '-')
#EndsWith() Method

Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))

print(100 * '-')
#Expendtab() method
str = "This is Lava\t kumar olipi...................!"
print("Origenal string: " + str)
print("Defalut Tab: " + str.expandtabs())
print("Double Tab: " + str.expandtabs(16))
print(100 * '-')
#find() Method

str1 = "this is string example....wow!!!"
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))
print(100 * '-')
#index() method
str1 = "this is string example....wow!!!"
str2 = "exam";
print (str1.index(str2))
print (str1.index(str2, 10))
print (str1.index(str2, 40))

print(100 * '-')
