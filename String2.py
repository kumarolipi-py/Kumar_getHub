#isalnum() method

str = "this2016"
print(str.isalnum())
str = "this is string example....wow!!!"
print(str.isalnum())

print(100 * '-')
str = "this"  # No space in this string
print(str.isalpha())
str = "this is string example....wow!!!"
print(str.isalpha())

print(100 * '-')
#isalnum() method

str = "this2016"
print(str.isalnum())
str = "this is string example....wow!!!"
print(str.isalnum())

print(100 * '-')
# isdigit() method
str = "2016"  # No space in this string
print (str.isdigit())
str = "this is string example....wow!!!"
print (str.isdigit())

print(100 * '-')
# islower() Method

str = "this is string example....wow!!!"
print (str.islower())
str = "this is string example....wow!!!"
print (str.islower())
print(100 * '-')
# isnumaric() Method
str = "this2016"
print (str.isnumeric())
str = "23443434"
print(str.isnumeric())

print(100 * '-')
s = "-"
seq = ("a", "b", "c")
print (s.join( seq ))
print(100 * '-')
# Lenth() method
str = "this is string example....wow!!!"
print ("Length of the string: ", len(str))

print(100 * '-')
#istrip() method
str = "     this is string example....wow!!!"
print (str.rstrip())
str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))

print(100 * '-')
intab = 'aeiou'
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print (str.translate(trantab))

print(100 * '-')
# max() Method
str = "This is lavakumar..............Really!!!!!"
print("Max Char: " + max(str))
str = "This is lavakumar..............Wow!!!!!!"
print("Max Char : " + max(str))
print(100 * '-')
# Min() Method
str = "www.tutorialspoint.com"
print("Min Char: " + min(str))
str = "SLKJLSLKSJLJGFLFKDJGLKJDFF"
print("Min Char : " + min(str))

print(100 * '-')
#replace() Method
str = "This is Lavakumar......! This is my project"
print(str.replace("is", "was"))
print(str.replace("is", "was", 3))

print(100 * '-')
str = "this is string example....wow!!!"
print (str.ljust(50, '*'))

print(100 * '-')
# rfind, find, rindex, index methods same sample it will refernce that method will be change
str = "This is Lavakumar project"
str1 = "is"
print(str.rindex(str1))
print(str.rindex(str1, 0 , 10))
print(str.rindex(str1, 10 , 0))
print(str.index(str1))
print(str.index(str1, 0, 5))
print(str.index(str1, 10, 0))

print(100 * "-")
str3 = "This is lavakumar project.............wow!!!"
print(str3.rjust(50 , "*"))

