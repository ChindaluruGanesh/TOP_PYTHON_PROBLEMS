nth_num = int(input('Enter a number : '))

count = 0
number = 0
while count != nth_num:
    temp = number
    temp1 = number
    count_digits = 0
    arm_strong = 0
    while temp:
        rem = temp % 10
        count_digits += 1
        temp //= 10
    while temp1:
        rem = temp1 % 10
        arm_strong += (rem ** count_digits)
        temp1 //= 10
    if arm_strong == number:
        count += 1
        if count == nth_num:
            print(number)
    number += 1

