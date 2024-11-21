arr = list(map(int,input('Enter numbers: ').split(' ')))
c = 1
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
        c = 0
        break
if c:
    print('Array is sorted')
else:
    print('Array is not sorted')