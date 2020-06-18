seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))
dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict))
print("-----------Get Method----------------")
dict = {'Name': 'Manni', 'Age': 7, 'Class': 'MCA'}
print(dict.get('Name'))
print(dict.get('Age'))
print(dict.get('Class'))
print('----------------Iteam() Method----------------------')
print(dict.items())
print(dict.keys())
print(dict.values())
print('----------------set default--------------------')
dict2 = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict2.setdefault('Age', None))
print ("Value : %s" %  dict2.setdefault('Sex', None))
print (dict2)
print("-----------Upadte method-------------------------")
dict3 = {'Name': 'Zara', 'Age': 7}
dict4 = {'Class':'MCA'}
dict3.update(dict4)
print(dict3)
print('---------------Values----------------')
print(list(dict3.values()))

