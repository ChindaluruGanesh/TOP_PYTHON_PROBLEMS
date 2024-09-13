num = int(input('Enter a number : '))
temp = num
reverse_num = 0

while num:
    rem = num % 10
    reverse_num = reverse_num * 10 + rem
    num = num // 10

if temp == reverse_num:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')


