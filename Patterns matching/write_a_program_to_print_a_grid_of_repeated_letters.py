m = int(input('Enter no of rows : '))
n = int(input('Enter no of columns : '))

for i in range(m):
    print(((chr(65 + i)) + ' ' ) * n)  # 65 is ASCI Value of A