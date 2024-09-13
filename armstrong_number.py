num = int(input('Enter a number : '))
temp2 = num
temp = num
count_num = 0
armstrong_number = 0
while temp:
    temp = temp // 10
    count_num += 1

while temp2:
    rem = temp2 % 10
    armstrong_number += rem ** count_num
    temp2 = temp2 // 10

if num == armstrong_number:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')