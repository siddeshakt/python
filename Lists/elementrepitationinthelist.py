list1 = [5,4,3,2,1]
list2= []
for i in list1:
    list2.extend([i, i])
    
#can also achive the same using list comprehension    
#list2 = [i for i in list1 for x in (0, 1)]
    
print(list2)    