m = int(input('Enter no of rows : '))
n = int(input('Enter no of columns : '))

for i in range(m):
    for j in range(n):
        print((chr(65+j)),end=' ')
    print()