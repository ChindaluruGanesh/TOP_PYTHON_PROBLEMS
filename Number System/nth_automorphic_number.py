nth_num = int(input('Enter a number : '))
count = 0
number = 0
while count != nth_num:
    temp = number
    temp1 = number ** 2
    c = 0
    while temp:
        if (temp % 10) != (temp1 % 10):
            c += 1
        temp //= 10
        temp1 //= 10
    if c == 0:
        count += 1
        if nth_num == count:
            print(number)
    number += 1
