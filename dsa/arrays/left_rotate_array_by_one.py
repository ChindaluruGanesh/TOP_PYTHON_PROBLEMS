arr = list(map(int,input('Enter numbers: ').split(' ')))

a = arr[len(arr)-1]
for i in range(len(arr)-1,-1,-1):
    arr[i] = arr[i-1]
arr[0] = a
print(arr)