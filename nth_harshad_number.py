# it is divisible by the sum of its digit
nth_num = int(input('Enter a number : '))
count = 0
number = 1
while nth_num != count:
    sum_of_num = 0
    temp = number
    while temp:
        rem  = temp % 10
        sum_of_num += rem
        temp //= 10
    if (number % sum_of_num) == 0:
        count += 1
        if count == nth_num:
            print(number)
    number += 1


