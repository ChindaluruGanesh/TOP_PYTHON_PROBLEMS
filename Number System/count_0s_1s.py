num = int(input('Enter a number : '))
count_num = 0
while num:
    rem = num % 10
    if rem == 0 or rem == 1:
        count_num += 1
    num = num // 10
print(count_num)