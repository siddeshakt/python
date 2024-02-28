arr = [[1,2,3], [4,5,6], [7,8,9]]
#total_sum = [sum(row) for row in arr]
num_elements = sum(len(row) for row in arr)
#average = total_sum / num_elements if num_elements else 0
print(num_elements)



arr = [[1,2,3], [4,5,6]]
row_index = 1
max_value = max(arr[row_index])
print(max_value)