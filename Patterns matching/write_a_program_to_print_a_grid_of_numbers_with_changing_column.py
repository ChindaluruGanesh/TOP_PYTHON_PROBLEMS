m = int(input('Enter no of rows : '))
n = int(input('Enter no of columns : '))

for i in range(m):
    for j in range(n):
        print((str(j + 1)), end=' ')
    print()