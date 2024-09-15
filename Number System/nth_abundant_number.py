# a positive integer for which the sum of its proper divisors is greater than the number
nth_num = int(input('Enter a number : '))
count = 0
number = 1

while count != nth_num:
    abundant_num = 0
    for i in range(1,number):
        if (number % i) == 0:
            abundant_num += i
    if abundant_num > number:
        count += 1
        if count  == nth_num:
            print(number)
    number += 1
