num = int(input('Enter a Number : '))
temp = num
perfect_num = 0
while temp:
    rem = temp % 10
    perfect_num += rem
    temp //= 10

if perfect_num == num:
    print('Perfect Number')
else:
    print('Not a Perfect Number')
