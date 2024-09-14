# A number n is said to be an Abundant Number 
# if the sum of all the proper divisors of the number denoted by sum(n) is greater than the value of the number n.

num = int(input('Enter a number : '))
temp = num
abund_num = 0
while temp:
    rem = temp % 10
    abund_num += 10
    temp //= 10

if abund_num > num:
    print('Abundant Number')
else:
    print('Not a Abundant Number')