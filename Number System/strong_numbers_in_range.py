# sum of the factorial of its digit is equal to number itself

num1 , num2 = map(int,input('Enter a number : ').split())

while num1 != num2:
    temp = num1
    strong_num = 0
    while temp:
        r = temp % 10
        factorial = 1
        while r:
            factorial *= r
            r -= 1
        strong_num += factorial 
        temp = temp // 10
    if strong_num == num1:
        print(strong_num,end=' ')
    num1 += 1

        