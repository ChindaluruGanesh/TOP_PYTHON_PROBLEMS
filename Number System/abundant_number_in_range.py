num1 , num2 = map(int,input('Enter a number : ').split())

while num1 != num2:
    temp = num1
    abundant_num = 0
    c = 1
    while temp != c:
        if (temp % c) == 0:
            abundant_num += c
        c += 1
    if abundant_num > num1:
        print(num1,end=' ')
    num1 += 1

