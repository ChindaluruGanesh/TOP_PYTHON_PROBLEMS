# a positive integer that is equal to the sum of its proper divisors
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.

num = int(input('Enter a number : '))
temp = num
strong_num = 0
while temp:
    rem = temp % 10
    fact = 1
    while rem:
        fact = fact * rem
        rem -= 1
    strong_num += fact
    temp //= 10

if num != strong_num:
    print('Not a Strong Number')
else:
    print('Strong Number')
