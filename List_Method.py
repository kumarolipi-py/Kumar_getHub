# Append():  list.append(obj)
lt = ['kumar','lava', 'lasya']
print(lt)
lt.append("Lavakumar, 22, 24")
print("Updated Value   : ", lt)
print("------------Count Method----------------------")
# count() Method..................
# List.count(obj)
lt1  = ['kumar','kumar', 125, 'raja', 125 ]
print("Count of the Object  :", lt1.count(125))
print("Count of the objects : ", lt1.count('kumar'))

# extended() Method
# list.extended(seq):
print("-----------------------list.Extended(Seq)-----------------------")
lt2 = ['physics', 'Chemistry','Maths']
lt3 = list(range(10))
lt2.extend(lt3)
print(lt2)
# Index () method
# list.index(obj)
print('---------------------list.index(obj)----------------------------')
lt4 = ['Physics','Chemistry','Maths']
print("Index   :", lt4.index('Physics'))
print("Index   : ", lt4.index('Maths'))
print('------------------list.insert()---------------------------------')
# insert() Method
lt5 = ['physics','chemistry','maths']
lt5.insert(3, 'Biology')
print("Inserted List : ", lt5)
# Pop Method()
print("-----------------------list.pop()-------------------------------")
lt6 = ['Physics','Chemistry','Biology', 'Maths']
lt6.pop()
print("Old List :", lt6)
lt6.pop(2)
print("New List: ", lt6)
# Remove () Method
print("--------------------list.remove()--------------------------------")
list1 = ['kumar','lava','lavakumnar', 25, 26, 89]
list1.remove(26)
print("List Values Now: ", list1)
list1.remove('lava')
print("List Values Now: ", list1)
print("---------------------list.revers()------------------------------")
#list Revers() Method
list1.reverse()
print(list1)
# Sort() Method
print("------------------------list.sort()-----------------------------")
list2 = ['Phython','Chemistry','Physics','Maths']
list2.sort()
print(list2)

