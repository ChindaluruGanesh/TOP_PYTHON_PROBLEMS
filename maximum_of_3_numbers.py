num1 , num2 , num3 = map(int,input('Enter 3 numbers : ').split())

if num1 > num2 and num1 > num3:
    print(num1, 'is maximum')
elif num2 > num3:
    print(num2, 'is maximum')
else:
    print(num3, 'is maximum')