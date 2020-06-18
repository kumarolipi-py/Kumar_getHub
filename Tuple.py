tup = ('Physiscs', 'Maths','Chemistry')
tup1 = (1,2,3,4,5,6,7,8,9)
print("Value is :", tup[2])
print("Value is :",tup1[1:5])
print("-----------------------UPdateing the value in tuple-------------------")
# tuples are immutable that means we connot to update or change the value in tuple

tup2 = (12, 36.78, 45, 89)
tup3 = ('Lava', 'kumar', 'Baby')
tup4 = tup2 + tup3
print(tup4)
print(tup2)

print(tup2)

print("-----------------Buid in functions in python----------------")
# Len()Method
print("Lenth of the tuple: ", len(tup2))
print("Lenth of the Tuple: ", len(tup3))
# MAX() Method()
print("Maxmum value in tuple: ", max(tup2))
# Min() Method()
print("Minmum value in Tuple: ", min(tup3))
#Tuple() Method()
list = ['lava', 'kumar','raja',23 , 24, 78]
tup5 = tuple(list)
print(tup5)
list1 = tuple(tup2)
print(list1)
print("---------------------------------------------------------------")

