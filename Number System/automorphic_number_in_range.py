num1 , num2 = map(int,input('Enter a number : ').split())

while num1 != num2:
    temp = num1
    temp1 = num1 ** 2
    count = 0
    while temp:
        if (temp % 10) != (temp1 % 10):
            count = 1
            break
        temp = temp // 10
        temp1 = temp1 // 10
    if count == 0:
        print(num1,end=' ')
    num1 += 1


