nth_num = int(input('Enter a number : ')) 

count = 0
number = 0

while count != nth_num:
    temp = number
    reverse_num = 0
    while temp:
        rem = temp % 10
        reverse_num = (reverse_num * 10) + rem
        temp //= 10
    if reverse_num == number:
        count += 1
        if count == nth_num:
            print(number)
    number += 1