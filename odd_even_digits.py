num = int(input('Enter a number : '))

odd_digits = 0
even_digits = 0

while num:
    rem = num % 10
    if (rem % 2) == 0:
        even_digits += 1
    else:
        odd_digits += 1
    num = num // 10

print('no of odd digits :',odd_digits,'no of even digits :',even_digits)