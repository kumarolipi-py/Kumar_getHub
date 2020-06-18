strVar = "welcome to python session"
strVar2 = " Olipi Lavakumar"
print("a Charactor position of [5]:", strVar[5])
print('position 5 to 10 character:', strVar[5:10])
print('position 0 to 10 character:', strVar[:10])
print('position 10 to 0 character:', strVar[5:])
print('concatinate strVar + StrVar2 : ', strVar + strVar2)
print('Multiple the variable : ', strVar2 * 3)
print('A Character position of [-3] : ', strVar[-3])
print('Reverse a string : ', strVar2[::-1])
print('What was the string : ', strVar2[::])
print('Concatenate StrVar + StrVar 2 :', strVar , strVar2)
strCon = strVar, strVar2
print(strCon)
strVar3 = 'new Value'
strVar3 = strVar3 + ' Additional value'
print(strVar3)
strVar3 += ' Third value'
print(strVar3)