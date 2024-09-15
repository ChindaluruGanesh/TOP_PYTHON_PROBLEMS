# An integer divisible by the sum of its digits is said to be a Harshad number.

num1,num2 = map(int,input('Enter a number : ').split())

while num1 != num2:
    temp = num1
    sum_of_digits = 0
    while temp:
        rem = temp % 10
        sum_of_digits += rem
        temp //= 10

    if (num1 % sum_of_digits) == 0:
        print(num1,end=' ')
    num1 = num1 + 1
