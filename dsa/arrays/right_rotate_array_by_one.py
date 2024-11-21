arr = list(map(int,input('Enter numbers: ').split(' ')))
#12345
#23451
a = arr[-1]
for i in range(0,len(arr)-1):
    arr[i] = arr[i+1]
arr[0] = a
print(arr)