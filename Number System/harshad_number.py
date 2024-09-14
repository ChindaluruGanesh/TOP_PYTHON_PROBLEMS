# An integer number in base 10 which is divisible by the sum of its digits is said to be a Harshad Number
# 21 --> 21 / (2 + 1)

num = int(input('Enter a number : '))
temp = num
sum_of_digits = 0

while temp:
    rem = temp % 10
    sum_of_digits += rem
    temp //= 10



if (num % sum_of_digits) == 0:
    print('Harshad Number')
else:
    print('Not a Harshad Number')
