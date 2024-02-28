list=[1,2,3,5]
target = 5
# seen_values = {}

# for i, num in enumerate(list):
    
#     required = target - num
#     if required in seen_values:
#         print([seen_values[required], i])
#     else:
#         seen_values[num] = i
        
result = [(i,j) for i in range(len(list)) for j in range(i+1, len(list)) if list[i] + list[j]==target]  
print(result)         


