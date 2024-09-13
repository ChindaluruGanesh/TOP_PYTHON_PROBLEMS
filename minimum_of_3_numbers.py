num1 , num2 , num3 = map(int,input('Enter 3 numbers : ').split())

if num1 < num2 and num1 < num3:
    print(num1, 'is minimum')
elif num2 < num3:
    print(num2, 'is minimum')
else:
    print(num3, 'is minimum')