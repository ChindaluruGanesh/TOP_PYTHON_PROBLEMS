a = [3,11,2,7,12,17,9,1,8]

for i in range(1,len(a)):
    temp = a[i]
    j = i - 1
    while (j>=0 and a[j] > temp):
        a[j+1] = a[j]
        j -= 1
    a[j+1] = temp
print(a)