num = int(input('Enter the number : '))
sum_of_digits = 0

while num:
    rem = num % 10
    sum_of_digits += rem
    num = num // 10
print(sum_of_digits)

