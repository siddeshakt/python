def reversearry(list, d):
    list = list[d:] + list[:d]
    return list


list = [1,2,5,8,9]
d=3
print(reversearry(list,d))


#list = list[2:] + list[:2]
#print(list)