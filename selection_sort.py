arr = [5,6,3,2,8,7,11]

for i in range(len(arr)-1):
    min_pos = i
    for j in range(i,len(arr)):
        if arr[j] < arr[min_pos]:
            min_pos = j
    temp = arr[i]
    arr[i] = arr[min_pos]
    arr[min_pos] = temp
    print(arr)