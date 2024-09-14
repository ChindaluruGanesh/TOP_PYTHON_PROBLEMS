num = int(input('Enter a number : '))
reverse_num = 0

while num:
    rem = num % 10
    reverse_num = reverse_num * 10 + rem
    num = num // 10
print(reverse_num)